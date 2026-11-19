"""Tests for src/analytics.py - Novelty algorithms for Indian infrastructure monitoring."""

from src import analytics


def test_monsoon_risk_high_rainfall_state_low_progress():
    res = analytics.compute_monsoon_risk(
        state="Assam",
        target_completion_month=7,  # July (peak monsoon)
        physical_progress=45.0,
    )
    assert res["monsoon_risk_category"] == "CRITICAL"
    assert res["monsoon_risk_score"] >= 0.70
    assert len(res["risk_factors"]) >= 2


def test_monsoon_risk_low_rainfall_advanced_progress():
    res = analytics.compute_monsoon_risk(
        state="Rajasthan",
        target_completion_month=12,  # December (dry winter)
        physical_progress=92.0,
    )
    assert res["monsoon_risk_category"] == "LOW"
    assert res["monsoon_risk_score"] < 0.40


def test_clearance_bottleneck_pending_trapped_capex():
    res = analytics.compute_clearance_bottleneck(
        clearance_status="Stage_I_Pending",
        total_budget_crores=1200.0,
        financial_spent_crores=150.0,
    )
    assert res["is_clearance_blocked"] is True
    assert res["bottleneck_severity"] == "SEVERE_BOTTLENECK"
    assert res["trapped_capex_crores"] == 1200.0


def test_clearance_bottleneck_cleared():
    res = analytics.compute_clearance_bottleneck(
        clearance_status="Cleared",
        total_budget_crores=800.0,
        financial_spent_crores=600.0,
    )
    assert res["is_clearance_blocked"] is False
    assert res["bottleneck_severity"] == "CLEARED"
    assert res["trapped_capex_crores"] == 0.0


def test_aspirational_equity_deficit():
    res = analytics.compute_aspirational_equity(
        district_name="Bahraich",  # Aspirational district
        district_population=3_500_000,
        total_capex_crores=350.0,  # 350 Cr = 3,500,000,000 INR -> 1000 INR/person
        state_avg_per_capita_inr=20000.0,
    )
    assert res["is_aspirational_district"] is True
    assert res["per_capita_capex_inr"] == 1000.0
    assert res["is_critically_underserved"] is True
    assert res["equity_ratio"] < 0.1
    assert res["infrastructure_deficit_score"] > 0.90


def test_progress_disparity_front_loading_anomaly():
    res = analytics.compute_progress_disparity(
        financial_spent_crores=850.0,
        total_budget_crores=1000.0,  # 85% financial paid
        physical_progress_pct=50.0,  # only 50% physical work done -> 35% disparity!
    )
    assert res["anomaly_detected"] is True
    assert res["alert_level"] == "CRITICAL_FRONT_LOADING"
    assert res["disparity_pct"] == 35.0


def test_progress_disparity_balanced():
    res = analytics.compute_progress_disparity(
        financial_spent_crores=480.0,
        total_budget_crores=1000.0,
        physical_progress_pct=50.0,
    )
    assert res["anomaly_detected"] is False
    assert res["alert_level"] == "BALANCED"


def test_gatishakti_engine_classification():
    nh_res = analytics.classify_gatishakti_engine(
        "Highway", "Construction of 6-lane Greenfield Expressway"
    )
    assert nh_res["gatishakti_engine"] == "Roads"

    dfc_res = analytics.classify_gatishakti_engine(
        "Freight", "Dedicated rail freight line with multimodal terminal"
    )
    assert dfc_res["gatishakti_engine"] == "Railways"
    assert dfc_res["multimodal_synergy"] is True

    port_res = analytics.classify_gatishakti_engine(
        "Sagarmala", "Deep sea port container terminal berth"
    )
    assert port_res["gatishakti_engine"] == "Ports"
