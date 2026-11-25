"""Tests for src/tourism_data.py - Indian Tourism and Architectural Heritage."""

from src import tourism_data


def test_get_state_tourism_known_states():
    rajasthan = tourism_data.get_state_tourism("Rajasthan")
    assert "Land of Kings" in rajasthan["tagline"]
    assert len(rajasthan["architectural_marvels"]) >= 3
    assert len(rajasthan["natural_spots"]) >= 2
    assert any("Delhi-Mumbai Expressway" in c for c in rajasthan["infra_connectivity"])
    # Verify image URLs and coordinates exist
    assert rajasthan["architectural_marvels"][0]["image_url"].startswith("https://")
    assert "latitude" in rajasthan["architectural_marvels"][0]

    kerala = tourism_data.get_state_tourism("Kerala")
    assert "God's Own Country" in kerala["tagline"]
    assert any("Padmanabhaswamy" in m["name"] for m in kerala["architectural_marvels"])
    assert any("Munnar" in n["name"] for n in kerala["natural_spots"])
    assert kerala["hero_image"].startswith("https://")


def test_get_state_tourism_fallback():
    punjab = tourism_data.get_state_tourism("Punjab")
    assert "Punjab" in punjab["tagline"]
    assert "architectural_marvels" in punjab
    assert "natural_spots" in punjab
    assert "infra_connectivity" in punjab
    assert punjab["hero_image"].startswith("https://")


def test_scenic_corridors_dataset():
    corridors = tourism_data.SCENIC_CORRIDORS
    assert len(corridors) >= 5
    first = corridors[0]
    assert "title" in first
    assert "image_url" in first
    assert "key_stops" in first
    assert len(first["key_stops"]) >= 3
