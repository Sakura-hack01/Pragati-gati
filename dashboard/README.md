# PragatiGati Dashboard

Real-time executive monitoring and cultural tourism exploration platform for India's national infrastructure.

## Real-Time Capabilities

- **Live WebSocket & SSE Streaming**: Broadcasts live construction progress, drone survey verifications, and IMD rainfall hazard alerts.
- **Construction Velocity Tracker**: Monitors daily paving speed (e.g. 39.4 km/day) in real time.
- **Real-Time Telemetry Ticker & Activity Log**: Dynamic slide-out drawer recording real-time project milestone certifications and treasury disbursements.

## Indian Architectural Heritage & Cultural Tourism ("Vikas Bhi, Virasat Bhi")

Aligned with the national vision of *"Vikas Bhi, Virasat Bhi"* (Development along with Cultural Heritage) and *"Dekho Apna Desh"*:

- **State Tourism & Natural Wonders Spotlight**:
  - Selecting any Indian state (e.g., Rajasthan, Kerala, Uttar Pradesh, Maharashtra, Assam, Gujarat, Tamil Nadu, Uttarakhand) instantly reveals:
    - **Architectural Marvels**: Ancient & medieval wonders (stepwells, rock-cut cave temples, living Chola temples, Ahom amphitheaters, Maratha sea forts) and modern megastructures.
    - **Natural Spots & Eco-Sanctuaries**: National parks, tiger reserves, alpine meadows, pristine backwaters, white salt deserts.
    - **Infrastructure-Tourism Links**: Specific Bharatmala Expressways (e.g. NE-4), Vande Bharat routes, and Parvatmala ropeways connecting tourists to these sites.
    - **Cultural Identity**: Authentic regional greetings, folk dances, GI-tagged handicrafts, and culinary gems.
- **Interactive Map Layer Switcher**:
  - Toggle between **Infra Packages** (Highways, Rail, Ports) and **Tourism & Heritage Spots** directly on the interactive GIS map.

## Running Locally

To launch the real-time server:

```bash
python dashboard/app.py --port 8050 --open
```

Navigate to `http://localhost:8050` in your web browser.
