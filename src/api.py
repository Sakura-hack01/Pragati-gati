"""Helpers for Indian infrastructure APIs, open data portals, and synthetic golden data feeds.

Connects to MoRTH/NHAI data, PM Gati Shakti multi-modal portal, LGD,
and provides robust ingestion generators for the PragatiGati Lakehouse pipeline.
"""

import json
import os
import random
import time
from collections.abc import Generator
from typing import Any

import requests

from src import config

HEADERS = {"User-Agent": config.USER_AGENT}


def check(url: str) -> str:
    """Return 'OK', 'HTTP <code>' or 'BLOCKED (<error>)' for one endpoint."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        return "OK" if response.ok else f"HTTP {response.status_code}"
    except requests.RequestException as error:
        return f"BLOCKED ({type(error).__name__})"


def get_json(
    url: str, params: dict | None = None, tries: int = 3, timeout: int = 60
) -> tuple[bytes, dict]:
    """Get a JSON reply with retries. Returns raw bytes and parsed dict."""
    for attempt in range(1, tries + 1):
        try:
            response = requests.get(
                url, params=params, headers=HEADERS, timeout=timeout
            )
            response.raise_for_status()
            data = response.json()
            return response.content, data
        except (requests.RequestException, ValueError):
            if attempt == tries:
                raise
            time.sleep(3 * attempt)


def download(url: str, destination_path: str) -> str:
    """Download a file with streaming to prevent memory pressure."""
    os.makedirs(os.path.dirname(destination_path), exist_ok=True)
    temp_path = f"{destination_path}.tmp"
    with requests.get(url, headers=HEADERS, stream=True, timeout=120) as r:
        r.raise_for_status()
        with open(temp_path, "wb") as f:
            f.writelines(r.iter_content(chunk_size=65536))
    if os.path.exists(destination_path):
        os.remove(destination_path)
    os.rename(temp_path, destination_path)
    return destination_path


# --- REALISTIC REFERENCE DATA FOR INDIAN INFRASTRUCTURE ---

INDIAN_STATES_DATA = [
    {
        "state_code": "MH",
        "state_name": "Maharashtra",
        "zone": "Western",
        "lgd_code": 27,
        "capital": "Mumbai",
    },
    {
        "state_code": "UP",
        "state_name": "Uttar Pradesh",
        "zone": "Northern",
        "lgd_code": 9,
        "capital": "Lucknow",
    },
    {
        "state_code": "TN",
        "state_name": "Tamil Nadu",
        "zone": "Southern",
        "lgd_code": 33,
        "capital": "Chennai",
    },
    {
        "state_code": "KA",
        "state_name": "Karnataka",
        "zone": "Southern",
        "lgd_code": 29,
        "capital": "Bengaluru",
    },
    {
        "state_code": "GJ",
        "state_name": "Gujarat",
        "zone": "Western",
        "lgd_code": 24,
        "capital": "Gandhinagar",
    },
    {
        "state_code": "RJ",
        "state_name": "Rajasthan",
        "zone": "Northern",
        "lgd_code": 8,
        "capital": "Jaipur",
    },
    {
        "state_code": "WB",
        "state_name": "West Bengal",
        "zone": "Eastern",
        "lgd_code": 19,
        "capital": "Kolkata",
    },
    {
        "state_code": "MP",
        "state_name": "Madhya Pradesh",
        "zone": "Central",
        "lgd_code": 23,
        "capital": "Bhopal",
    },
    {
        "state_code": "AP",
        "state_name": "Andhra Pradesh",
        "zone": "Southern",
        "lgd_code": 28,
        "capital": "Amaravati",
    },
    {
        "state_code": "TG",
        "state_name": "Telangana",
        "zone": "Southern",
        "lgd_code": 36,
        "capital": "Hyderabad",
    },
    {
        "state_code": "BR",
        "state_name": "Bihar",
        "zone": "Eastern",
        "lgd_code": 10,
        "capital": "Patna",
    },
    {
        "state_code": "OR",
        "state_name": "Odisha",
        "zone": "Eastern",
        "lgd_code": 21,
        "capital": "Bhubaneswar",
    },
    {
        "state_code": "KL",
        "state_name": "Kerala",
        "zone": "Southern",
        "lgd_code": 32,
        "capital": "Thiruvananthapuram",
    },
    {
        "state_code": "AS",
        "state_name": "Assam",
        "zone": "North-Eastern",
        "lgd_code": 18,
        "capital": "Dispur",
    },
    {
        "state_code": "JH",
        "state_name": "Jharkhand",
        "zone": "Eastern",
        "lgd_code": 20,
        "capital": "Ranchi",
    },
    {
        "state_code": "PB",
        "state_name": "Punjab",
        "zone": "Northern",
        "lgd_code": 3,
        "capital": "Chandigarh",
    },
    {
        "state_code": "HR",
        "state_name": "Haryana",
        "zone": "Northern",
        "lgd_code": 6,
        "capital": "Chandigarh",
    },
    {
        "state_code": "CT",
        "state_name": "Chhattisgarh",
        "zone": "Central",
        "lgd_code": 22,
        "capital": "Raipur",
    },
    {
        "state_code": "JK",
        "state_name": "Jammu & Kashmir",
        "zone": "Northern",
        "lgd_code": 1,
        "capital": "Srinagar",
    },
    {
        "state_code": "UT",
        "state_name": "Uttarakhand",
        "zone": "Northern",
        "lgd_code": 5,
        "capital": "Dehradun",
    },
    {
        "state_code": "HP",
        "state_name": "Himachal Pradesh",
        "zone": "Northern",
        "lgd_code": 2,
        "capital": "Shimla",
    },
    {
        "state_code": "TR",
        "state_name": "Tripura",
        "zone": "North-Eastern",
        "lgd_code": 16,
        "capital": "Agartala",
    },
    {
        "state_code": "ML",
        "state_name": "Meghalaya",
        "zone": "North-Eastern",
        "lgd_code": 17,
        "capital": "Shillong",
    },
    {
        "state_code": "MN",
        "state_name": "Manipur",
        "zone": "North-Eastern",
        "lgd_code": 14,
        "capital": "Imphal",
    },
    {
        "state_code": "NL",
        "state_name": "Nagaland",
        "zone": "North-Eastern",
        "lgd_code": 13,
        "capital": "Kohima",
    },
    {
        "state_code": "GA",
        "state_name": "Goa",
        "zone": "Western",
        "lgd_code": 30,
        "capital": "Panaji",
    },
    {
        "state_code": "AR",
        "state_name": "Arunachal Pradesh",
        "zone": "North-Eastern",
        "lgd_code": 12,
        "capital": "Itanagar",
    },
    {
        "state_code": "MZ",
        "state_name": "Mizoram",
        "zone": "North-Eastern",
        "lgd_code": 15,
        "capital": "Aizawl",
    },
    {
        "state_code": "SK",
        "state_name": "Sikkim",
        "zone": "North-Eastern",
        "lgd_code": 11,
        "capital": "Gangtok",
    },
    {
        "state_code": "DL",
        "state_name": "Delhi (NCT)",
        "zone": "Northern",
        "lgd_code": 7,
        "capital": "New Delhi",
    },
]

CONTRACTORS_SAMPLE = [
    {
        "name": "Larsen & Toubro Ltd (L&T)",
        "cin": "L99999MH1946PLC004768",
        "rating": "AAA",
        "headquarters": "Mumbai",
    },
    {
        "name": "Dilip Buildcon Limited",
        "cin": "L45201MP2006PLC018689",
        "rating": "AA",
        "headquarters": "Bhopal",
    },
    {
        "name": "Tata Projects Limited",
        "cin": "U45200MH1979PLC021287",
        "rating": "AAA",
        "headquarters": "Mumbai",
    },
    {
        "name": "G R Infraprojects Ltd",
        "cin": "L45201RJ1995PLC009862",
        "rating": "AA+",
        "headquarters": "Udaipur",
    },
    {
        "name": "PNC Infratech Ltd",
        "cin": "L45201DL1999PLC195937",
        "rating": "AA",
        "headquarters": "Agra",
    },
    {
        "name": "Afcons Infrastructure Ltd",
        "cin": "U45200MH1976PLC019335",
        "rating": "AA+",
        "headquarters": "Mumbai",
    },
    {
        "name": "Hindustan Construction Co (HCC)",
        "cin": "L45200MH1926PLC001228",
        "rating": "BBB+",
        "headquarters": "Mumbai",
    },
    {
        "name": "IRB Infrastructure Developers",
        "cin": "L65910MH1998PLC115960",
        "rating": "AA-",
        "headquarters": "Mumbai",
    },
    {
        "name": "NCC Limited",
        "cin": "L72200AP1990PLC011146",
        "rating": "A+",
        "headquarters": "Hyderabad",
    },
    {
        "name": "KNR Constructions Ltd",
        "cin": "L74210DL1995PLC130833",
        "rating": "AA",
        "headquarters": "Hyderabad",
    },
]

FLAGSHIP_PROJECTS = [
    {
        "title": "Delhi-Mumbai Expressway Package 14 (Vadodara-Kim Section)",
        "agency": "NHAI",
        "sector": "Roads & Expressways",
        "engine": "Roads",
        "state": "Gujarat",
        "district": "Vadodara",
        "budget_crores": 3450.0,
        "spent_crores": 3210.0,
        "progress_pct": 94.5,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "Larsen & Toubro Ltd (L&T)",
        "concession_model": "HAM",
        "lat": 22.3072,
        "lon": 73.1812,
        "completion_month": 4,
    },
    {
        "title": "Western Dedicated Freight Corridor (Rewari-Madar CTP-1)",
        "agency": "DFCCIL / Railways",
        "sector": "Heavy Freight Rail",
        "engine": "Railways",
        "state": "Rajasthan",
        "district": "Jaipur",
        "budget_crores": 6800.0,
        "spent_crores": 6500.0,
        "progress_pct": 98.0,
        "status": "Completed",
        "clearance": "Cleared",
        "contractor": "Tata Projects Limited",
        "concession_model": "EPC",
        "lat": 26.9124,
        "lon": 75.7873,
        "completion_month": 12,
    },
    {
        "title": "Mumbai-Ahmedabad High-Speed Rail (Bullet Train) C4 Package",
        "agency": "NHSRCL",
        "sector": "High-Speed Mass Transit",
        "engine": "Railways",
        "state": "Gujarat",
        "district": "Surat",
        "budget_crores": 24985.0,
        "spent_crores": 14200.0,
        "progress_pct": 52.0,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "Larsen & Toubro Ltd (L&T)",
        "concession_model": "EPC",
        "lat": 21.1702,
        "lon": 72.8311,
        "completion_month": 8,
    },
    {
        "title": "Zojila Tunnel Bypass All-Weather Connectivity (NH-1)",
        "agency": "NHIDCL",
        "sector": "Strategic Mountain Tunnel",
        "engine": "Roads",
        "state": "Jammu & Kashmir",
        "district": "Ganderbal",
        "budget_crores": 4500.0,
        "spent_crores": 2100.0,
        "progress_pct": 48.0,
        "status": "On-Going",
        "clearance": "Stage_II_Pending",
        "contractor": "Afcons Infrastructure Ltd",
        "concession_model": "EPC",
        "lat": 34.2810,
        "lon": 75.4850,
        "completion_month": 11,
    },
    {
        "title": "Vadhavan Mega Deep-Draft Port Coastal Connectivity Corridor",
        "agency": "JNPA / MoPSW",
        "sector": "Greenfield Deep Port & Sagarmala",
        "engine": "Ports",
        "state": "Maharashtra",
        "district": "Palghar",
        "budget_crores": 76220.0,
        "spent_crores": 3200.0,
        "progress_pct": 8.5,
        "status": "Not Yet Started",
        "clearance": "CRZ_Review",
        "contractor": "Hindustan Construction Co (HCC)",
        "concession_model": "BOT",
        "lat": 19.9700,
        "lon": 72.6900,
        "completion_month": 7,
    },
    {
        "title": "Bengaluru-Chennai Expressway (Phase-2 Chittoor Section)",
        "agency": "NHAI",
        "sector": "Roads & Expressways",
        "engine": "Roads",
        "state": "Andhra Pradesh",
        "district": "Chittoor",
        "budget_crores": 2890.0,
        "spent_crores": 2600.0,
        "progress_pct": 89.0,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "Dilip Buildcon Limited",
        "concession_model": "HAM",
        "lat": 13.2172,
        "lon": 79.1003,
        "completion_month": 5,
    },
    {
        "title": "Namami Gange Barrage & Riverfront Flood Embankment Protection",
        "agency": "Ministry of Jal Shakti / NMCG",
        "sector": "River Flood Mitigation & Drainage",
        "engine": "Waterways",
        "state": "Bihar",
        "district": "Patna",
        "budget_crores": 1850.0,
        "spent_crores": 1540.0,
        "progress_pct": 78.0,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "G R Infraprojects Ltd",
        "concession_model": "HAM",
        "lat": 25.5941,
        "lon": 85.1376,
        "completion_month": 6,
    },
    {
        "title": "Bhopal Metro Purple Line Rail Corridors (Phase 1)",
        "agency": "MPMRCL / MoHUA",
        "sector": "Urban Mass Transit",
        "engine": "Mass Transport",
        "state": "Madhya Pradesh",
        "district": "Bhopal",
        "budget_crores": 6940.0,
        "spent_crores": 4510.0,
        "progress_pct": 66.0,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "Dilip Buildcon Limited",
        "concession_model": "EPC",
        "lat": 23.2599,
        "lon": 77.4126,
        "completion_month": 3,
    },
    {
        "title": "Navi Mumbai International Airport Phase 1 Multi-Modal Hub",
        "agency": "CIDCO / Adani Airports",
        "sector": "Aviation Logistics Hub",
        "engine": "Airports",
        "state": "Maharashtra",
        "district": "Raigad",
        "budget_crores": 19600.0,
        "spent_crores": 15800.0,
        "progress_pct": 82.0,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "Larsen & Toubro Ltd (L&T)",
        "concession_model": "PPP",
        "lat": 18.9894,
        "lon": 73.0722,
        "completion_month": 10,
    },
    {
        "title": "Bahraich-Shravasti Border Flood Mitigation & Embankment Works",
        "agency": "UP Irrigation / FMBAP",
        "sector": "Flood Control & Embankment",
        "engine": "Waterways",
        "state": "Uttar Pradesh",
        "district": "Bahraich",
        "budget_crores": 720.0,
        "spent_crores": 410.0,
        "progress_pct": 51.0,
        "status": "On-Going",
        "clearance": "Stage_I_Pending",
        "contractor": "PNC Infratech Ltd",
        "concession_model": "EPC",
        "lat": 27.5744,
        "lon": 81.5976,
        "completion_month": 7,
    },
    {
        "title": "Bhubaneswar-Puri NH-316 Coastal Economic Corridor Upgradation",
        "agency": "NHAI",
        "sector": "Roads & Tourism Corridor",
        "engine": "Roads",
        "state": "Odisha",
        "district": "Puri",
        "budget_crores": 1650.0,
        "spent_crores": 1390.0,
        "progress_pct": 84.0,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "NCC Limited",
        "concession_model": "HAM",
        "lat": 19.8135,
        "lon": 85.8312,
        "completion_month": 9,
    },
    {
        "title": "Guwahati Inland Water Transport Terminal & NW-2 Brahmaputra Hub",
        "agency": "IWAI / MoPSW",
        "sector": "Inland Waterways Freight Hub",
        "engine": "Waterways",
        "state": "Assam",
        "district": "Kamrup",
        "budget_crores": 920.0,
        "spent_crores": 310.0,
        "progress_pct": 34.0,
        "status": "On-Going",
        "clearance": "Wildlife_Sanction_Pending",
        "contractor": "Afcons Infrastructure Ltd",
        "concession_model": "EPC",
        "lat": 26.1445,
        "lon": 91.7362,
        "completion_month": 8,
    },
    {
        "title": "Kochi Metro Phase-2 Extension (JLN Stadium to Kakkanad Infopark)",
        "agency": "KMRL / MoHUA",
        "sector": "Urban Mass Transit",
        "engine": "Mass Transport",
        "state": "Kerala",
        "district": "Ernakulam",
        "budget_crores": 1957.0,
        "spent_crores": 620.0,
        "progress_pct": 31.0,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "Afcons Infrastructure Ltd",
        "concession_model": "EPC",
        "lat": 9.9816,
        "lon": 76.2999,
        "completion_month": 7,
    },
    {
        "title": "Wayanad Tunnel Bypass Route (Anakkampoyil-Meppadi Twin Tube)",
        "agency": "KRFB / MoRTH",
        "sector": "Hill Highway Tunnel",
        "engine": "Roads",
        "state": "Kerala",
        "district": "Wayanad",
        "budget_crores": 2134.0,
        "spent_crores": 250.0,
        "progress_pct": 12.0,
        "status": "On-Going",
        "clearance": "Stage_II_Pending",
        "contractor": "Hindustan Construction Co (HCC)",
        "concession_model": "EPC",
        "lat": 11.5540,
        "lon": 76.1320,
        "completion_month": 8,
    },
    {
        "title": "Ranchi-Varanasi Economic Corridor Expressway (Package 4)",
        "agency": "NHAI",
        "sector": "Bharatmala Expressway",
        "engine": "Roads",
        "state": "Jharkhand",
        "district": "Ranchi",
        "budget_crores": 2420.0,
        "spent_crores": 1820.0,
        "progress_pct": 72.0,
        "status": "On-Going",
        "clearance": "Cleared",
        "contractor": "G R Infraprojects Ltd",
        "concession_model": "HAM",
        "lat": 23.3441,
        "lon": 85.3096,
        "completion_month": 11,
    },
]


def generate_nhai_projects(total_projects: int = 250) -> list[dict[str, Any]]:
    """Generates comprehensive Indian National Highways and Bharatmala infrastructure projects."""
    random.seed(42)
    projects = []

    # Pre-load flagship projects
    for idx, p in enumerate(FLAGSHIP_PROJECTS):
        contract_id = f"NHAI/BHARAT/{2024 + (idx % 3)}/{1000 + idx}"
        projects.append(
            {
                "contractId": contract_id,
                "projectName": p["title"],
                "executingAgency": p["agency"],
                "sector": p["sector"],
                "gatishaktiEngine": p["engine"],
                "state": p["state"],
                "district": p["district"],
                "budgetInCrores": p["budget_crores"],
                "amountPaidInCrores": p["spent_crores"],
                "physicalProgressPct": p["progress_pct"],
                "status": p["status"],
                "pariveshClearanceStatus": p["clearance"],
                "contractorName": p["contractor"],
                "concessionModel": p["concession_model"],
                "latitude": p["lat"],
                "longitude": p["lon"],
                "startDate": "2023-01-15",
                "targetCompletionDate": f"2026-{p['completion_month']:02d}-30",
            }
        )

    # Generate additional projects across Indian States and Districts
    statuses = [
        "Completed",
        "On-Going",
        "On-Going",
        "On-Going",
        "Not Yet Started",
        "Terminated",
    ]
    concessions = ["HAM", "EPC", "EPC", "BOT-Toll"]
    clearances = [
        "Cleared",
        "Cleared",
        "Cleared",
        "Stage_I_Pending",
        "Stage_II_Pending",
        "Wildlife_Sanction_Pending",
    ]

    while len(projects) < total_projects:
        idx = len(projects) + 1
        state_info = random.choice(INDIAN_STATES_DATA)
        contractor = random.choice(CONTRACTORS_SAMPLE)
        status = random.choice(statuses)
        budget = round(random.uniform(150.0, 4800.0), 2)

        if status == "Completed":
            progress = 100.0
            paid = round(budget * random.uniform(0.95, 1.0), 2)
            clearance = "Cleared"
        elif status == "Not Yet Started":
            progress = 0.0
            paid = round(budget * random.uniform(0.0, 0.08), 2)
            clearance = random.choice(
                ["Stage_I_Pending", "Stage_II_Pending", "Land_Acquisition_Dispute"]
            )
        elif status == "Terminated":
            progress = round(random.uniform(5.0, 35.0), 1)
            paid = round(budget * 0.40, 2)
            clearance = "Land_Acquisition_Dispute"
        else:  # On-Going
            progress = round(random.uniform(15.0, 92.0), 1)
            # Inject occasional front-loading disparity for anomaly detection
            disparity_factor = random.choice([1.0, 1.0, 1.0, 1.25, 0.85])
            paid = min(
                budget, round((budget * (progress / 100.0)) * disparity_factor, 2)
            )
            clearance = random.choice(clearances)

        # Geographic coordinates within India bounding box
        lat = round(random.uniform(9.0, 32.5), 4)
        lon = round(random.uniform(72.0, 89.0), 4)

        contract_id = f"NHAI/TECH/{2023 + (idx % 4)}/{2000 + idx}"
        name = f"Four-laning & Upgradation of NH-{random.randint(10, 900)} {state_info['state_name']} Corridor Pkg-{idx % 8 + 1}"

        projects.append(
            {
                "contractId": contract_id,
                "projectName": name,
                "executingAgency": random.choice(["NHAI", "MoRTH", "NHIDCL"]),
                "sector": "National Highways & Expressways",
                "gatishaktiEngine": "Roads",
                "state": state_info["state_name"],
                "district": f"{state_info['state_name']} District-{idx % 20 + 1}",
                "budgetInCrores": budget,
                "amountPaidInCrores": paid,
                "physicalProgressPct": progress,
                "status": status,
                "pariveshClearanceStatus": clearance,
                "contractorName": contractor["name"],
                "concessionModel": random.choice(concessions),
                "latitude": lat,
                "longitude": lon,
                "startDate": "2023-04-01",
                "targetCompletionDate": f"2026-{random.randint(1, 12):02d}-28",
            }
        )

    return projects


def nhai_pages(
    page_size: int = config.NHAI_PAGE_SIZE,
) -> Generator[tuple[int, bytes, int, int], None, None]:
    """Yields paginated JSON replies of NHAI/MoRTH infrastructure projects."""
    projects = generate_nhai_projects(250)
    total = len(projects)
    for page_num, offset in enumerate(range(0, total, page_size), start=1):
        batch = projects[offset : offset + page_size]
        reply_dict = {
            "status": "success",
            "data": {
                "pagination": {
                    "page": page_num,
                    "limit": page_size,
                    "totalCount": total,
                    "hasNext": (offset + page_size) < total,
                },
                "projects": batch,
            },
        }
        raw_bytes = json.dumps(reply_dict, ensure_ascii=False).encode("utf-8")
        yield page_num, raw_bytes, len(batch), total


def flood_control_pages(
    page_size: int = config.JAL_SHAKTI_PAGE_SIZE,
) -> Generator[tuple[int, bytes, int, int], None, None]:
    """Yields paginated JSON replies of Jal Shakti and FMBAP flood mitigation assets."""
    flood_projects = [
        p
        for p in FLAGSHIP_PROJECTS
        if p["engine"] == "Waterways" or "Flood" in p["title"]
    ]
    # Add synthesized river basin assets
    river_basins = [
        "Ganga",
        "Brahmaputra",
        "Godavari",
        "Mahanadi",
        "Kosi",
        "Yamuna",
        "Narmada",
    ]
    while len(flood_projects) < 50:
        idx = len(flood_projects) + 1
        basin = random.choice(river_basins)
        st = random.choice(INDIAN_STATES_DATA)
        flood_projects.append(
            {
                "title": f"{basin} Basin Anti-Erosion & Flood Embankment Structure Pkg-{idx}",
                "agency": "Ministry of Jal Shakti / FMBAP",
                "sector": "River Flood Control",
                "engine": "Waterways",
                "state": st["state_name"],
                "district": f"{st['state_name']} District-{idx % 15 + 1}",
                "budget_crores": round(random.uniform(40.0, 850.0), 2),
                "spent_crores": round(random.uniform(20.0, 700.0), 2),
                "progress_pct": round(random.uniform(25.0, 95.0), 1),
                "status": "On-Going",
                "clearance": "Cleared",
                "contractor": random.choice(CONTRACTORS_SAMPLE)["name"],
                "concession_model": "EPC",
                "lat": round(random.uniform(22.0, 28.5), 4),
                "lon": round(random.uniform(77.0, 92.0), 4),
                "completion_month": 6,
            }
        )

    features = []
    for idx, fp in enumerate(flood_projects, start=1):
        features.append(
            {
                "type": "Feature",
                "attributes": {
                    "ObjectId": idx,
                    "ContractID": f"JAL/FMBAP/{2024}/{3000 + idx}",
                    "ProjectTitle": fp["title"],
                    "State": fp["state"],
                    "District": fp["district"],
                    "ContractCostCrores": fp["budget_crores"],
                    "AmountPaidCrores": fp["spent_crores"],
                    "PhysicalProgressPct": fp["progress_pct"],
                    "TypeofWork": "Flood Mitigation & Embankment Structure",
                    "ExecutingAgency": fp["agency"],
                    "ClearanceStatus": fp["clearance"],
                    "Latitude": fp["lat"],
                    "Longitude": fp["lon"],
                },
                "geometry": {"x": fp["lon"], "y": fp["lat"]},
            }
        )

    total = len(features)
    for page_num, offset in enumerate(range(0, total, page_size), start=1):
        batch = features[offset : offset + page_size]
        reply_dict = {
            "spatialReference": {"wkid": 4326},
            "count": total,
            "features": batch,
        }
        raw_bytes = json.dumps(reply_dict, ensure_ascii=False).encode("utf-8")
        yield page_num, raw_bytes, len(batch), total
