"""Tests for src/tourism_data.py - Indian Tourism and Architectural Heritage."""

from src import tourism_data


def test_get_state_tourism_known_states():
    rajasthan = tourism_data.get_state_tourism("Rajasthan")
    assert "Land of Kings" in rajasthan["tagline"]
    assert len(rajasthan["architectural_marvels"]) >= 3
    assert len(rajasthan["natural_spots"]) >= 2
    assert any("Delhi-Mumbai Expressway" in c for c in rajasthan["infra_connectivity"])

    kerala = tourism_data.get_state_tourism("Kerala")
    assert "God's Own Country" in kerala["tagline"]
    assert any("Padmanabhaswamy" in m["name"] for m in kerala["architectural_marvels"])
    assert any("Munnar" in n["name"] for n in kerala["natural_spots"])


def test_get_state_tourism_fallback():
    punjab = tourism_data.get_state_tourism("Punjab")
    assert "Punjab" in punjab["tagline"]
    assert "architectural_marvels" in punjab
    assert "natural_spots" in punjab
    assert "infra_connectivity" in punjab
