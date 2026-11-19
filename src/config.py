"""Names, constants, and endpoints for PragatiGati: India National Infrastructure & PM Gati Shakti Monitoring.

Change a link or configuration here, and every notebook/module reflects it.
"""

CATALOG = "pragatigati-capstone"
SOURCE = "00-source"
BRONZE = "01-bronze"
SILVER = "02-silver"
GOLD = "03-gold"
VALIDATION = "04-validation"

# Files saved before loading: API replies and raw datasets in Databricks volume
LANDING = f"/Volumes/{CATALOG}/{SOURCE}/landing"

REPO = "github.com/PragatiGati/infra-project-monitoring-india"

# User-Agent header for public API requests
USER_AGENT = f"pragatigati-india-monitoring ({REPO})"

# Currency standard: Indian Rupee (INR / ₹)
CURRENCY = "INR"
CURRENCY_SYMBOL = "₹"

# 1. MoRTH & NHAI National Highways and Bharatmala Pariyojana API
NHAI_API = "https://data.gov.in/api/v1/morth-nhai-projects"
NHAI_PAGE_SIZE = 1000

# 2. PM Gati Shakti Multi-Modal Master Plan (Railways, Ports, Freight Corridors)
GATISHAKTI_API = "https://gatishakti.gov.in/api/v1/multimodal-projects"
GATISHAKTI_PAGE_SIZE = 500

# 3. Jal Shakti & Namami Gange / Flood Management and Border Areas Programme (FMBAP)
JAL_SHAKTI_LAYER = "https://services.indiawaterportal.org/arcgis/rest/services/Flood_Mitigation_Projects/FeatureServer/0/query"
JAL_SHAKTI_PAGE_SIZE = 1000

# 4. Local Government Directory (LGD) - Ministry of Panchayati Raj
# Standard administrative codes for 36 States/UTs and 780+ Districts
LGD_FOLDER = f"{LANDING}/lgd"
LGD_API = "https://lgdirectory.gov.in/rest/states-districts"
LGD_FILE = "LGD_States_Districts_2026.json"

# 5. Census & MoSPI Population Data (District-level projections)
CENSUS_FOLDER = f"{LANDING}/census"
CENSUS_FILE = "India_District_Population_MoSPI_2024_2026.xlsx"
EXPECTED_DISTRICTS = 788
TOTAL_POPULATION_ESTIMATE = 1_428_627_663  # 1.428 Billion

# 6. Survey of India / Bharatmaps Boundary GeoJSON
BOUNDARY_BASE = "https://raw.githubusercontent.com/geohacker/india/master/district/"
BOUNDARY_FILES = [
    "india_zones.geojson",
    "india_states_ut.geojson",
    "india_districts.geojson",
    "india_freight_corridors.geojson",
]

# Rough bounding box around India (excluding remote island outer limits)
# Used for coordinate validation: Latitude ~6.5° N to 37.5° N, Longitude ~68.0° E to 97.5° E
INDIA_LAT = (6.5, 37.5)
INDIA_LON = (68.0, 97.5)

# --- NOVELTY 1: PM Gati Shakti 7 Engines ---
GATI_SHAKTI_ENGINES = [
    "Roads",
    "Railways",
    "Airports",
    "Ports",
    "Mass Transport",
    "Waterways",
    "Logistics Infrastructure",
]

# --- NOVELTY 2: PARIVESH 2.0 Clearance Milestones ---
CLEARANCE_STAGES = [
    "Forest_Stage_I",
    "Forest_Stage_II",
    "Environmental_Clearance",
    "Wildlife_Clearance",
    "Coastal_Regulation_Zone",
    "Land_Acquisition_Sec19",
]

# --- NOVELTY 3: IMD Rainfall Hazard Zones ---
# High monsoon rainfall regions face annual construction moratoriums
IMD_HIGH_RAINFALL_STATES = {
    "Assam",
    "Meghalaya",
    "Arunachal Pradesh",
    "Nagaland",
    "Manipur",
    "Mizoram",
    "Tripura",
    "Kerala",
    "Goa",
    "Uttarakhand",
    "Himachal Pradesh",
}

# --- NOVELTY 4: NITI Aayog Aspirational Districts (Selected Priority Set) ---
ASPIRATIONAL_DISTRICTS_SAMPLE = {
    "Mewat",
    "Bahraich",
    "Shravasti",
    "Balrampur",
    "Chandauli",
    "Wayanad",
    "Bijapur",
    "Kupwara",
    "Baramulla",
    "Dahod",
    "Kandhamal",
    "Nabarangpur",
    "Ranchi",
    "Dumka",
    "Kiphire",
}

# --- Source Connectivity Check Endpoints ---
SOURCE_CHECKS = {
    "MoRTH Open Data (data.gov.in)": "https://data.gov.in/api/v1/morth-nhai-projects?limit=1",
    "PM Gati Shakti National Master Plan": "https://gatishakti.gov.in/api/v1/health",
    "LGD Local Government Directory": "https://lgdirectory.gov.in",
    "MoSPI National Statistics": "https://mospi.gov.in",
    "PARIVESH Environmental Clearance Portal": "https://parivesh.nic.in",
    "IMD India Meteorological Dept": "https://mausam.imd.gov.in",
    "Survey of India Bhuvan GIS": "https://bhuvan.nrsc.gov.in",
}
