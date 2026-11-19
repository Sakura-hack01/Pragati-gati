"""Novelty analytics engine for PragatiGati: India National Infrastructure Monitoring.

Implements unique features:
1. IMD Monsoon & Seasonal Disruption Risk Engine
2. PARIVESH 2.0 Clearance Bottleneck & Trapped Capex Index
3. NITI Aayog Aspirational Districts Infrastructure Equity Deficit
4. "Ghost Progress" & Financial-to-Physical Disparity Detector
5. PM Gati Shakti Multi-Modal Engine Alignment & Synergy Classifier
"""

from typing import Any

from src import config


def compute_monsoon_risk(
    state: str,
    target_completion_month: int | None = None,
    physical_progress: float = 0.0,
) -> dict[str, Any]:
    """Calculates seasonal disruption risk based on IMD (India Meteorological Dept) rainfall zones.

    During peak southwest monsoon (June-September), heavy precipitation halts earthwork,
    bridge piers, and bituminous paving. Projects in high-rainfall terrain with <75% progress
    face substantial slippage risks.
    """
    is_high_monsoon = state in config.IMD_HIGH_RAINFALL_STATES
    in_critical_window = (
        target_completion_month in [6, 7, 8, 9] if target_completion_month else False
    )

    # Risk factor: 0.0 to 1.0
    risk_score = 0.1
    reasons = []

    if is_high_monsoon:
        risk_score += 0.45
        reasons.append("Located in IMD High-Hazard / Fragile terrain rainfall zone")

    if physical_progress < 60.0:
        risk_score += 0.25
        reasons.append("Critical earthwork/structural stage vulnerable to washouts")
    elif physical_progress < 85.0:
        risk_score += 0.15
        reasons.append("Surface finishing/paving vulnerable to rain delays")

    if in_critical_window:
        risk_score += 0.2
        reasons.append(
            "Target deadline falls within peak monsoon moratorium window (Jun-Sep)"
        )

    risk_score = min(round(risk_score, 2), 1.0)
    category = (
        "CRITICAL" if risk_score >= 0.7 else "MODERATE" if risk_score >= 0.4 else "LOW"
    )

    return {
        "monsoon_risk_score": risk_score,
        "monsoon_risk_category": category,
        "risk_factors": reasons,
    }


def compute_clearance_bottleneck(
    clearance_status: str,
    total_budget_crores: float,
    financial_spent_crores: float,
) -> dict[str, Any]:
    """Evaluates regulatory delays across PARIVESH gates (Forest Stage I/II, EC, Wildlife, Land Sec 19).

    Quantifies 'Trapped Capex' - capital allocated or partially disbursed in projects
    frozen by pending statutory sanctions.
    """
    is_pending = clearance_status in [
        "Stage_I_Pending",
        "Stage_II_Pending",
        "Wildlife_Sanction_Pending",
        "Land_Acquisition_Dispute",
        "CRZ_Review",
    ]

    trapped_capex = total_budget_crores if is_pending else 0.0
    bottleneck_severity = (
        "SEVERE_BOTTLENECK"
        if (is_pending and total_budget_crores > 500.0)
        else "MODERATE_BOTTLENECK"
        if is_pending
        else "CLEARED"
    )

    return {
        "is_clearance_blocked": is_pending,
        "clearance_gate": clearance_status,
        "bottleneck_severity": bottleneck_severity,
        "trapped_capex_crores": round(trapped_capex, 2),
    }


def compute_aspirational_equity(
    district_name: str,
    district_population: int,
    total_capex_crores: float,
    state_avg_per_capita_inr: float = 25000.0,
) -> dict[str, Any]:
    """Evaluates NITI Aayog Aspirational District infrastructure deficit.

    Answers the core question: Which areas have high population and vulnerability
    but receive disproportionately low public infrastructure investment?
    """
    is_aspirational = district_name in config.ASPIRATIONAL_DISTRICTS_SAMPLE

    # Per capita spend in INR (1 Crore = 10,000,000 INR)
    if district_population > 0:
        per_capita_inr = round((total_capex_crores * 1e7) / district_population, 2)
    else:
        per_capita_inr = 0.0

    equity_ratio = (
        round(per_capita_inr / state_avg_per_capita_inr, 2)
        if state_avg_per_capita_inr > 0
        else 1.0
    )

    is_underserved = per_capita_inr < (0.5 * state_avg_per_capita_inr)
    deficit_score = round(
        max(
            0.0, (state_avg_per_capita_inr - per_capita_inr) / state_avg_per_capita_inr
        ),
        2,
    )

    return {
        "is_aspirational_district": is_aspirational,
        "per_capita_capex_inr": per_capita_inr,
        "equity_ratio": equity_ratio,
        "is_critically_underserved": is_underserved,
        "infrastructure_deficit_score": deficit_score,
    }


def compute_progress_disparity(
    financial_spent_crores: float,
    total_budget_crores: float,
    physical_progress_pct: float,
) -> dict[str, Any]:
    """Detects 'Ghost Progress' or Financial Front-loading anomalies.

    If the percentage of financial outlay disbursed significantly exceeds reported
    physical milestone progress (e.g., >15% disparity), flags potential contractor
    cash diversion or certification misalignment.
    """
    if total_budget_crores <= 0:
        return {
            "financial_progress_pct": 0.0,
            "physical_progress_pct": physical_progress_pct,
            "disparity_pct": 0.0,
            "anomaly_detected": False,
            "alert_level": "NORMAL",
        }

    financial_progress_pct = round(
        (financial_spent_crores / total_budget_crores) * 100.0, 2
    )
    disparity = round(financial_progress_pct - physical_progress_pct, 2)

    if disparity > 25.0:
        alert = "CRITICAL_FRONT_LOADING"
        anomaly = True
    elif disparity > 15.0:
        alert = "MODERATE_DISPARITY"
        anomaly = True
    elif disparity < -25.0:
        alert = "UNPAID_PHYSICAL_ADVANCE"
        anomaly = False
    else:
        alert = "BALANCED"
        anomaly = False

    return {
        "financial_progress_pct": financial_progress_pct,
        "physical_progress_pct": round(physical_progress_pct, 2),
        "disparity_pct": disparity,
        "anomaly_detected": anomaly,
        "alert_level": alert,
    }


def classify_gatishakti_engine(sector: str, description: str) -> dict[str, Any]:
    """Classifies a project into one of the PM Gati Shakti 7 Engines and evaluates multi-modal synergy."""
    text = f"{sector} {description}".lower()

    engine = "Logistics Infrastructure"
    if any(
        k in text
        for k in [
            "highway",
            "road",
            "expressway",
            "nh-",
            "bypass",
            "flyover",
            "morth",
            "nhai",
        ]
    ):
        engine = "Roads"
    elif any(
        k in text
        for k in ["rail", "dfc", "bullet train", "track", "gauge", "station", "loco"]
    ):
        engine = "Railways"
    elif any(
        k in text for k in ["metro", "mrt", "brts", "suburban", "tram", "monorail"]
    ):
        engine = "Mass Transport"
    elif any(
        k in text for k in ["port", "harbour", "jetty", "berth", "sagarmala", "dock"]
    ):
        engine = "Ports"
    elif any(
        k in text
        for k in ["waterway", "nw-", "river", "ganga", "barrage", "canal", "inland"]
    ):
        engine = "Waterways"
    elif any(
        k in text for k in ["airport", "runway", "terminal", "aai", "udan", "heliport"]
    ):
        engine = "Airports"

    # Check multi-modal connectivity synergy
    has_synergy = any(
        term in text
        for term in [
            "intermodal",
            "multimodal",
            "icd",
            "freight village",
            "mmlp",
            "rail-linked",
            "port-connectivity",
            "airport-express",
        ]
    )

    return {
        "gatishakti_engine": engine,
        "multimodal_synergy": has_synergy,
        "pillar_priority": "High"
        if engine in ["Roads", "Railways", "Ports"]
        else "Medium",
    }
