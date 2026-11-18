"""Tests for Indian infrastructure pipeline data sources and geographic bounding."""

from src import api, config


def test_nhai_projects_generator():
    projects = api.generate_nhai_projects(total_projects=100)
    assert len(projects) == 100
    first = projects[0]
    assert "contractId" in first
    assert "budgetInCrores" in first
    assert "state" in first
    assert "pariveshClearanceStatus" in first
    assert first["budgetInCrores"] > 0


def test_india_bounding_box():
    projects = api.generate_nhai_projects(total_projects=50)
    for p in projects:
        lat = p["latitude"]
        lon = p["longitude"]
        assert config.INDIA_LAT[0] <= lat <= config.INDIA_LAT[1], f"Lat {lat} outside India"
        assert config.INDIA_LON[0] <= lon <= config.INDIA_LON[1], f"Lon {lon} outside India"


def test_flood_control_pages():
    pages = list(api.flood_control_pages(page_size=20))
    assert len(pages) >= 2
    page_num, raw_bytes, rows_count, total = pages[0]
    assert page_num == 1
    assert rows_count == 20
    assert total >= 50
    assert b"spatialReference" in raw_bytes
