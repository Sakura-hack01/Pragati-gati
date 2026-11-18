"""Real-time server for PragatiGati: India National Infrastructure & Tourism Platform.

Provides:
1. Real-time WebSocket & SSE streaming of live construction progress, drone telemetry, and IMD weather alerts.
2. REST API endpoints for Projects, State Tourism & Architectural Heritage.
3. Static dashboard web interface at http://localhost:8050.

Usage:
    python dashboard/app.py [--port 8050] [--open]
"""

import argparse
import asyncio
import datetime
import json
import os
import random
import webbrowser
from typing import List

from src import api, analytics, tourism_data

DEFAULT_PORT = 8050
DASHBOARD_DIR = os.path.dirname(os.path.abspath(__file__))

# Check if fastapi and uvicorn are available
try:
    from fastapi import FastAPI, WebSocket, WebSocketDisconnect
    from fastapi.responses import HTMLResponse, StreamingResponse
    from fastapi.staticfiles import StaticFiles
    import uvicorn

    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False


if HAS_FASTAPI:
    app = FastAPI(
        title="PragatiGati Real-Time Infrastructure & Tourism API",
        description="Live streaming platform for Indian infrastructure monitoring and cultural tourism",
        version="2.0.0",
    )

    # Active WebSocket clients
    active_connections: List[WebSocket] = []

    # Pre-generate projects memory cache
    CACHED_PROJECTS = api.generate_nhai_projects(total_projects=265)
    for p in CACHED_PROJECTS:
        m_risk = analytics.compute_monsoon_risk(
            p["state"],
            int(p["targetCompletionDate"].split("-")[1]),
            p["physicalProgressPct"],
        )
        p["monsoon_risk_category"] = m_risk["monsoon_risk_category"]
        p["monsoon_risk_score"] = m_risk["monsoon_risk_score"]

        c_bot = analytics.compute_clearance_bottleneck(
            p["pariveshClearanceStatus"], p["budgetInCrores"], p["amountPaidInCrores"]
        )
        p["is_clearance_blocked"] = c_bot["is_clearance_blocked"]
        p["trapped_capex"] = c_bot["trapped_capex_crores"]

        disp = analytics.compute_progress_disparity(
            p["amountPaidInCrores"], p["budgetInCrores"], p["physicalProgressPct"]
        )
        p["progress_disparity_pct"] = disp["disparity_pct"]
        p["disparity_anomaly"] = disp["anomaly_detected"]

        eq = analytics.compute_aspirational_equity(
            p["district"], 2500000, p["budgetInCrores"]
        )
        p["is_aspirational"] = eq["is_aspirational_district"]

    # Serve static files (HTML, JS, CSS)
    app.mount("/static", StaticFiles(directory=DASHBOARD_DIR), name="static")

    @app.get("/", response_class=HTMLResponse)
    async def get_index():
        with open(os.path.join(DASHBOARD_DIR, "index.html"), "r", encoding="utf-8") as f:
            return f.read()

    @app.get("/api/projects")
    async def get_projects():
        return {"count": len(CACHED_PROJECTS), "projects": CACHED_PROJECTS}

    @app.get("/api/state-tourism/{state_name}")
    async def get_state_tourism_endpoint(state_name: str):
        return tourism_data.get_state_tourism(state_name)

    @app.websocket("/ws")
    async def websocket_endpoint(websocket: WebSocket):
        await websocket.accept()
        active_connections.append(websocket)
        try:
            while True:
                # Keep alive and receive any client messages
                data = await websocket.receive_text()
        except WebSocketDisconnect:
            if websocket in active_connections:
                active_connections.remove(websocket)

    async def broadcast_realtime_events():
        """Background generator producing real-time construction telemetry, drone surveys, and alerts."""
        event_types = [
            "DRONE_SURVEY_COMPLETED",
            "PHYSICAL_PROGRESS_UPDATE",
            "PARIVESH_CLEARANCE_MILESTONE",
            "IMD_WEATHER_ALERT",
            "DISBURSEMENT_RECORDED",
        ]

        while True:
            await asyncio.sleep(2.5)  # Broadcast every 2.5 seconds
            if not active_connections:
                continue

            target_project = random.choice(CACHED_PROJECTS)
            event_type = random.choice(event_types)
            now_iso = datetime.datetime.now().strftime("%H:%M:%S")

            if event_type == "DRONE_SURVEY_COMPLETED":
                message = f"🛰️ Drone Survey #{random.randint(100, 999)} verified earthwork progress on {target_project['projectName'][:45]}... ({target_project['state']})"
                delta = round(random.uniform(0.1, 0.4), 1)
                target_project["physicalProgressPct"] = min(
                    100.0, round(target_project["physicalProgressPct"] + delta, 1)
                )
            elif event_type == "PHYSICAL_PROGRESS_UPDATE":
                delta = round(random.uniform(0.2, 0.6), 1)
                target_project["physicalProgressPct"] = min(
                    100.0, round(target_project["physicalProgressPct"] + delta, 1)
                )
                message = f"🚧 Paving milestone: Physical progress reached {target_project['physicalProgressPct']}% on {target_project['contractId']}."
            elif event_type == "PARIVESH_CLEARANCE_MILESTONE":
                message = f"📋 PARIVESH Portal Update: In-principle Stage-I sanction processed for {target_project['district']} corridor."
            elif event_type == "IMD_WEATHER_ALERT":
                message = f"🌧️ IMD Advisory: Heavy precipitation warning issued for construction sites across {target_project['state']}."
            else:
                amount = round(random.uniform(5.0, 45.0), 1)
                target_project["amountPaidInCrores"] = min(
                    target_project["budgetInCrores"],
                    round(target_project["amountPaidInCrores"] + amount, 1),
                )
                message = f"💳 Treasury disbursement: ₹ {amount} Cr released for {target_project['projectName'][:40]}."

            payload = {
                "timestamp": now_iso,
                "event_type": event_type,
                "message": message,
                "contract_id": target_project["contractId"],
                "project_name": target_project["projectName"],
                "state": target_project["state"],
                "updated_physical_progress": target_project["physicalProgressPct"],
                "updated_amount_paid": target_project["amountPaidInCrores"],
                "velocity_km_per_day": round(random.uniform(37.5, 41.2), 1),
            }

            dead_conns = []
            for conn in active_connections:
                try:
                    await conn.send_text(json.dumps(payload))
                except Exception:
                    dead_conns.append(conn)
            for d in dead_conns:
                if d in active_connections:
                    active_connections.remove(d)

    @app.on_event("startup")
    async def startup_event():
        asyncio.create_task(broadcast_realtime_events())

    @app.get("/api/live-stream")
    async def live_stream_sse():
        """Server-Sent Events (SSE) alternative for environments without WebSockets."""
        async def event_generator():
            while True:
                await asyncio.sleep(3)
                target = random.choice(CACHED_PROJECTS)
                now_str = datetime.datetime.now().strftime("%H:%M:%S")
                data = {
                    "timestamp": now_str,
                    "message": f"Real-time sensor telemetry: Normal readings on {target['projectName'][:40]}",
                    "velocity_km_per_day": round(random.uniform(38.0, 40.5), 1),
                }
                yield f"data: {json.dumps(data)}\n\n"

        return StreamingResponse(event_generator(), media_type="text/event-stream")


def run(port: int = DEFAULT_PORT, auto_open: bool = False):
    url = f"http://localhost:{port}"
    print("=" * 65)
    print(f" PragatiGati: Live Real-Time Infrastructure & Tourism Platform")
    print(f" Dashboard URL: {url}")
    print(f" Real-time WebSocket: ws://localhost:{port}/ws")
    print(f" REST API: {url}/api/projects and {url}/api/state-tourism/{{state}}")
    print(" Press Ctrl+C to terminate.")
    print("=" * 65)

    if auto_open:
        webbrowser.open(url)

    if HAS_FASTAPI:
        uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
    else:
        # Fallback to standard HTTP server
        import http.server
        import socketserver

        os.chdir(DASHBOARD_DIR)
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), handler) as httpd:
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nServer stopped.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run PragatiGati Dashboard")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port to serve on")
    parser.add_argument("--open", action="store_true", help="Open in default browser")
    args = parser.parse_args()
    run(port=args.port, auto_open=args.open)
