"""Comprehensive Indian Tourism, Architectural Heritage, and Natural Spot Knowledge Base.

Aligned with the Government of India's 'Dekho Apna Desh' and 'Vikas Bhi, Virasat Bhi'
(Development & Heritage) initiatives, linking modern infrastructure (Expressways,
Vande Bharat, UDAN, Parvatmala Ropeways) to historic architecture and natural wonders.
"""

from typing import Dict, Any, List

STATE_TOURISM_DATA: Dict[str, Dict[str, Any]] = {
    "Rajasthan": {
        "tagline": "The Land of Kings (पधारो म्हारे देश)",
        "greeting": "Khamma Ghani! (खम्मा घणी)",
        "accent_color": "#EA580C",
        "architectural_marvels": [
            {
                "name": "Amber Fort & Palace (Jaipur)",
                "type": "Rajput-Mughal Fort Architecture",
                "highlight": "Mirror work in Sheesh Mahal, intricate ramparts, Maota Lake view.",
                "built_century": "16th Century",
            },
            {
                "name": "Chand Baori Stepwell (Abhaneri)",
                "type": "Hydraulic Ancient Architecture",
                "highlight": "3,500 narrow steps over 13 storeys; geometric mathematical symmetry.",
                "built_century": "9th Century",
            },
            {
                "name": "Mehrangarh Fort (Jodhpur)",
                "type": "Hilltop Citadel Architecture",
                "highlight": "Perched 400 feet above the Blue City; formidable 120-ft high bastions.",
                "built_century": "15th Century",
            },
            {
                "name": "Ranakpur Jain Temple",
                "type": "Maru-Gurjara Temple Architecture",
                "highlight": "1,444 uniquely hand-carved marble pillars, no two alike.",
                "built_century": "15th Century",
            },
        ],
        "natural_spots": [
            {
                "name": "Ranthambore National Park (Sawai Madhopur)",
                "category": "Tiger Reserve & Deciduous Wilderness",
                "highlight": "Royal Bengal tigers roaming amidst ancient lake ruins and banyan trees.",
            },
            {
                "name": "Sam Sand Dunes & Thar Desert (Jaisalmer)",
                "category": "Desert Ecology & Sand Dunes",
                "highlight": "Shifting golden dunes, camel safaris, and starlit astronomical skies.",
            },
            {
                "name": "Keoladeo Ghana National Park (Bharatpur)",
                "category": "UNESCO Wetland & Bird Sanctuary",
                "highlight": "Winter haven for over 370 migratory avian species from Siberia and Central Asia.",
            },
        ],
        "infra_connectivity": [
            "Delhi-Mumbai Expressway (NE-4): Cuts Delhi-Jaipur drive to 2.5 hours.",
            "Ajmer-Delhi Vande Bharat Express: Semi-high-speed rail access to Pink City.",
            "UDAN Regional Flights: Direct links to Kishangarh (Ajmer) and Bikaner.",
        ],
        "culture_and_cuisine": "Dal Baati Churma, Ker Sangri, Blue Pottery, and Ghoomar folk dance.",
        "best_time_to_visit": "October to March (Pleasant winter season)",
    },
    "Kerala": {
        "tagline": "God's Own Country (കേരളം)",
        "greeting": "Namaskaram! (നമസ്കാരം)",
        "accent_color": "#059669",
        "architectural_marvels": [
            {
                "name": "Padmanabhaswamy Temple (Thiruvananthapuram)",
                "type": "Chera & Dravidian Architecture",
                "highlight": "16th-century Gopuram, 365 intricately carved granite pillars.",
                "built_century": "8th–16th Century",
            },
            {
                "name": "Bekal Fort (Kasaragod)",
                "type": "Coastal Defense Architecture",
                "highlight": "Keyhole-shaped citadel on the Arabian Sea with subterranean escape tunnels.",
                "built_century": "17th Century",
            },
            {
                "name": "Traditional Kettuvallam (Houseboats)",
                "type": "Indigenous Marine Architecture",
                "highlight": "Constructed without a single nail using Anjili wood tied with coir ropes.",
                "built_century": "Traditional",
            },
        ],
        "natural_spots": [
            {
                "name": "Munnar & Anamudi Peak (Idukki)",
                "category": "Western Ghats High-Altitude Shola Ecosystem",
                "highlight": "Rolling tea plantations, misty valleys, and home to endangered Nilgiri Tahr.",
            },
            {
                "name": "Alleppey & Vembanad Backwaters",
                "category": "Wetland & Lagoon Ecosystem",
                "highlight": "Interconnected canals, paddy fields cultivated below sea level (Kuttanad).",
            },
            {
                "name": "Silent Valley National Park (Palakkad)",
                "category": "Pristine Tropical Rainforest",
                "highlight": "One of the last undisturbed rain forests with rare Lion-Tailed Macaques.",
            },
        ],
        "infra_connectivity": [
            "Kochi Metro Water Metro: World's first integrated electric water transit network.",
            "Thiruvananthapuram-Kasargod Vande Bharat Express: High-speed coastal connectivity.",
            "Wayanad Twin-Tube Hill Highway Tunnel: All-weather Western Ghats transit.",
        ],
        "culture_and_cuisine": "Sadya, Appam with Stew, Kathakali, Kalaripayattu martial art, and boat races.",
        "best_time_to_visit": "September to March; Monsoon tourism in June–August",
    },
    "Uttar Pradesh": {
        "tagline": "The Heartland of Culture (उत्तर प्रदेश - सबका साथ, सबका विकास)",
        "greeting": "Pranam! (प्रणाम / राधे राधे)",
        "accent_color": "#D97706",
        "architectural_marvels": [
            {
                "name": "Taj Mahal & Agra Fort (Agra)",
                "type": "Mughal Marble Architecture (UNESCO)",
                "highlight": "Pietra dura inlay, octagonal minarets, central dome symbolizing eternal love.",
                "built_century": "17th Century",
            },
            {
                "name": "Varanasi Riverfront Ghats & Kashi Vishwanath Dham",
                "type": "Ancient Riverfront Architectural Complex",
                "highlight": "84 stepped stone ghats on the sacred Ganga, grand renovated temple corridor.",
                "built_century": "Continuous Antiquity",
            },
            {
                "name": "Bara Imambara & Rumi Darwaza (Lucknow)",
                "type": "Awadhi Architectural Grandeur",
                "highlight": "World's largest unsupported arched hall (Bhool-Bhulaiya labyrinth).",
                "built_century": "18th Century",
            },
        ],
        "natural_spots": [
            {
                "name": "Dudhwa National Park (Lakhimpur Kheri)",
                "category": "Terai Sal Forest & Grassland Ecosystem",
                "highlight": "Rhinos, Royal Bengal tigers, swamp deer (Barasingha), and rich birdlife.",
            },
            {
                "name": "Chandra Prabha Wildlife Sanctuary (Chandauli)",
                "category": "Vindhyan Escarpment & Waterfalls",
                "highlight": "Cascading Rajdari & Devdari waterfalls surrounded by prehistoric cave shelters.",
            },
        ],
        "infra_connectivity": [
            "Purvanchal & Bundelkhand Expressways: Rapid access to historic heartlands.",
            "Noida International Airport (Jewar): Multi-modal gateway to Western UP.",
            "Vande Bharat Express (Delhi-Varanasi & Lucknow-Gorakhpur).",
        ],
        "culture_and_cuisine": "Awadhi Biryani, Banarasi Silk, Chikankari embroidery, and Ganga Aarti.",
        "best_time_to_visit": "October to March",
    },
    "Maharashtra": {
        "tagline": "Gateway to Great India (महाराष्ट्र - जय महाराष्ट्र)",
        "greeting": "Jai Maharashtra! (जय महाराष्ट्र / नमस्कार)",
        "accent_color": "#DC2626",
        "architectural_marvels": [
            {
                "name": "Ajanta & Ellora Rock-Cut Caves (Chhatrapati Sambhaji Nagar)",
                "type": "Ancient Rock-Cut Monolithic Architecture (UNESCO)",
                "highlight": "Kailasa Temple (Cave 16) carved top-down from a single volcanic basalt cliff.",
                "built_century": "2nd Century BCE – 10th Century CE",
            },
            {
                "name": "Raigad & Sindhudurg Sea Forts",
                "type": "Maratha Military & Naval Fort Architecture",
                "highlight": "Chhatrapati Shivaji Maharaj's coastal fortress with lead-poured underwater foundations.",
                "built_century": "17th Century",
            },
            {
                "name": "Chhatrapati Shivaji Maharaj Terminus (CSMT, Mumbai)",
                "type": "Victorian Gothic Revival & Indo-Saracenic",
                "highlight": "High Victorian stone dome, turrets, pointed arches, and wood carving.",
                "built_century": "19th Century",
            },
        ],
        "natural_spots": [
            {
                "name": "Kaas Plateau / Valley of Flowers (Satara)",
                "category": "UNESCO Biosphere & Basalt Plateau",
                "highlight": "Endemic seasonal wildflowers blooming in carpets over volcanic laterite.",
            },
            {
                "name": "Tadoba-Andhari Tiger Reserve (Chandrapur)",
                "category": "Teak Forest & Wildlife Sanctuary",
                "highlight": "Oldest and largest national park in Maharashtra with high tiger density.",
            },
            {
                "name": "Lonar Crater Lake (Buldhana)",
                "category": "Geo-Heritage Meteorite Impact Lake",
                "highlight": "World's only hyper-velocity meteorite impact crater in basaltic rock.",
            },
        ],
        "infra_connectivity": [
            "Mumbai-Nagpur Samruddhi Mahamarg: 701-km Super Communication Expressway.",
            "Mumbai Trans Harbour Link (Atal Setu): India's longest sea bridge.",
            "Navi Mumbai International Airport & Metro Line 3 (Aqua Line).",
        ],
        "culture_and_cuisine": "Puran Poli, Misal Pav, Warli Tribal Art, Lavani dance, and Ganesh Utsav.",
        "best_time_to_visit": "July to February (Lush Sahyadri monsoons and mild winters)",
    },
    "Uttarakhand": {
        "tagline": "Devbhoomi - Land of the Gods (देवभूमि उत्तराखण्ड)",
        "greeting": "Pranam! (सादर प्रणाम)",
        "accent_color": "#0284C7",
        "architectural_marvels": [
            {
                "name": "Kedarnath & Badrinath Temples",
                "type": "Katyuri & Nagara Stone Architecture",
                "highlight": "Centuries-old glacial stone architecture that survived catastrophic floods.",
                "built_century": "8th Century",
            },
            {
                "name": "Jageshwar Temple Complex (Almora)",
                "type": "Nagara Style Devalayas",
                "highlight": "Cluster of 124 stone temples nestled in a dense deodar forest canopy.",
                "built_century": "7th–12th Century",
            },
        ],
        "natural_spots": [
            {
                "name": "Valley of Flowers & Nanda Devi Biosphere (Chamoli)",
                "category": "UNESCO World Heritage Alpine Meadow",
                "highlight": "Alpine meadows of 500+ flower species framed by snow-clad Himalayan peaks.",
            },
            {
                "name": "Jim Corbett National Park (Nainital)",
                "category": "Sub-Himalayan Sal Forest & Riverine Belts",
                "highlight": "India's first national park, legendary refuge for Bengal tigers and wild elephants.",
            },
            {
                "name": "Rishikesh & Ganga River Gorges",
                "category": "Himalayan Riverine Gorge",
                "highlight": "Yoga capital of the world, white-water rapids, and suspension bridges.",
            },
        ],
        "infra_connectivity": [
            "Char Dham All-Weather Road Pariyojana: Widened highway connectivity.",
            "Rishikesh-Karnaprayag Rail Link: 125-km mountain tunnel rail project.",
            "Parvatmala Ropeways to Kedarnath and Hemkund Sahib.",
        ],
        "culture_and_cuisine": "Kafuli, Bal Mithai, Garhwali and Kumaoni traditional wood-carved homes.",
        "best_time_to_visit": "March to June (Summer) and September to November (Autumn)",
    },
    "Tamil Nadu": {
        "tagline": "Where Stories Never End (தமிழ்நாடு)",
        "greeting": "Vanakkam! (வணக்கம்)",
        "accent_color": "#7C3AED",
        "architectural_marvels": [
            {
                "name": "Brihadisvara Temple (Thanjavur)",
                "type": "Great Living Chola Temple (UNESCO)",
                "highlight": "Granite tower (Vimana) rising 216 feet, topped by an 80-tonne single stone dome.",
                "built_century": "11th Century (1010 CE)",
            },
            {
                "name": "Meenakshi Amman Temple (Madurai)",
                "type": "Dravidian Temple Complex",
                "highlight": "14 monumental gopurams decorated with thousands of painted mythological figures.",
                "built_century": "6th–17th Century",
            },
            {
                "name": "Group of Monuments at Mamallapuram",
                "type": "Pallava Rock-Cut Architecture (UNESCO)",
                "highlight": "Pancha Rathas, Shore Temple, and Arjuna's Penance bas-relief carving.",
                "built_century": "7th–8th Century",
            },
        ],
        "natural_spots": [
            {
                "name": "Nilgiri Biosphere & Ooty Peaks",
                "category": "Western Ghats Montane Forest",
                "highlight": "UNESCO Heritage Nilgiri Mountain Railway (Toy Train), blue hills, eucalyptus groves.",
            },
            {
                "name": "Gulf of Mannar Marine National Park",
                "category": "Coral Reef & Marine Biosphere",
                "highlight": "21 coastal islands with mangroves, dugongs (sea cows), and endangered coral beds.",
            },
            {
                "name": "Mudumalai National Park",
                "category": "Deciduous Wildlife Corridor",
                "highlight": "Crucial Asian elephant migration corridor and tiger reserve.",
            },
        ],
        "infra_connectivity": [
            "Bengaluru-Chennai Expressway (NE-5): 4-lane access connecting tech corridors.",
            "Chennai-Coimbatore & Chennai-Mysuru Vande Bharat Expresses.",
            "Pamban Railway Sea Bridge (India's 1st vertical-lift sea bridge to Rameswaram).",
        ],
        "culture_and_cuisine": "Idli-Sambar, Chettinad cuisine, Bharatanatyam, Kanchipuram silk sarees.",
        "best_time_to_visit": "November to February",
    },
    "Assam": {
        "tagline": "The Awesome Assam (অসম)",
        "greeting": "Nomoskar! (নমস্কাৰ)",
        "accent_color": "#16A34A",
        "architectural_marvels": [
            {
                "name": "Rang Ghar & Talatal Ghar (Sivasagar)",
                "type": "Ahom Royal Architecture",
                "highlight": "Two-storey royal amphitheatre built with indigenous rice paste and duck-egg mortar.",
                "built_century": "18th Century",
            },
            {
                "name": "Kamakhya Temple (Guwahati)",
                "type": "Nilachal Hybrid Nagara-Ahom Style",
                "highlight": "Crucible of Tantric Shaktism with bee-hive shaped stone shikhara.",
                "built_century": "8th–16th Century",
            },
        ],
        "natural_spots": [
            {
                "name": "Kaziranga National Park (Golaghat / Nagaon)",
                "category": "UNESCO World Heritage Sanctuary",
                "highlight": "Sanctuary for two-thirds of the world's Great One-Horned Rhinoceroses.",
            },
            {
                "name": "Majuli Island (Brahmaputra River)",
                "category": "World's Largest Inhabited River Island",
                "highlight": "Neo-Vaishnavite Satras, vibrant pottery, mask-making, and riverine ecosystem.",
            },
            {
                "name": "Manas National Park",
                "category": "UNESCO Tiger & Biosphere Reserve",
                "highlight": "Pristine sub-Himalayan foothill forest with Pygmy Hogs and Golden Langurs.",
            },
        ],
        "infra_connectivity": [
            "Bogibeel Rail-cum-Road Bridge: Longest rail-road bridge in India over Brahmaputra.",
            "National Waterway 2 (NW-2): Freight and luxury river cruise corridor.",
            "Guwahati-New Jalpaiguri Vande Bharat Express.",
        ],
        "culture_and_cuisine": "Assam Tea, Bihu dance, Muga Golden Silk, and Kaji Nemu.",
        "best_time_to_visit": "October to April",
    },
    "Gujarat": {
        "tagline": "Vibrant Gujarat (આપણું ગુજરાત)",
        "greeting": "Kem Cho! (કેમ છો / જય શ્રી કૃષ્ણ)",
        "accent_color": "#F59E0B",
        "architectural_marvels": [
            {
                "name": "Rani ki Vav Stepwell (Patan)",
                "type": "Maru-Gurjara Inverted Temple Stepwell (UNESCO)",
                "highlight": "Subterranean stepwell featuring over 500 principal sculptures of Vishnu avatars.",
                "built_century": "11th Century",
            },
            {
                "name": "Sun Temple, Modhera",
                "type": "Solanki Architectural Masterpiece",
                "highlight": "Built so the sun's first rays at the equinox illuminate the inner sanctum.",
                "built_century": "1026 CE",
            },
            {
                "name": "Statue of Unity (Kevadia)",
                "type": "World's Tallest Monumental Engineering",
                "highlight": "182-metre bronze tribute to Sardar Vallabhbhai Patel with high-speed elevators.",
                "built_century": "2018 CE",
            },
        ],
        "natural_spots": [
            {
                "name": "Gir National Park & Wildlife Sanctuary (Junagadh)",
                "category": "Asiatic Lion Last Sanctuary",
                "highlight": "The only remaining natural habitat of the majestic Asiatic Lion in the world.",
            },
            {
                "name": "Great Rann of Kutch (Kutch)",
                "category": "White Salt Desert Salt Marsh",
                "highlight": "Vast expanse of shimmering salt desert, host to the vibrant Rann Utsav.",
            },
            {
                "name": "Marine National Park (Gulf of Kutch)",
                "category": "Intertidal Coral & Mangrove Park",
                "highlight": "First marine park in India where visitors can walk to coral reefs at low tide.",
            },
        ],
        "infra_connectivity": [
            "Mumbai-Ahmedabad High-Speed Rail (Bullet Train): India's flagship high-speed rail corridor.",
            "Delhi-Mumbai Expressway (Gujarat Packages) & Dholera Greenfield Expressway.",
            "Vande Bharat Express (Mumbai-Gandhinagar).",
        ],
        "culture_and_cuisine": "Dhokla, Thepla, Garba & Dandiya dance, Patola silk weaving.",
        "best_time_to_visit": "November to February (Rann Utsav season)",
    },
    "Madhya Pradesh": {
        "tagline": "The Heart of Incredible India (मध्य प्रदेश)",
        "greeting": "Namaste! (नमस्कार)",
        "accent_color": "#8B5CF6",
        "architectural_marvels": [
            {
                "name": "Khajuraho Group of Monuments",
                "type": "Chandela Nagara Architecture (UNESCO)",
                "highlight": "Intricately carved sandstone temples celebrating spiritual and aesthetic human life.",
                "built_century": "10th–11th Century",
            },
            {
                "name": "Great Stupa at Sanchi",
                "type": "Ancient Buddhist Monolithic Architecture (UNESCO)",
                "highlight": "Hemispherical brick dome commissioned by Emperor Ashoka with ceremonial Toranas.",
                "built_century": "3rd Century BCE",
            },
            {
                "name": "Gwalior Fort",
                "type": "Hilltop Citadel Architecture",
                "highlight": "'The Pearl among Fortresses of India', vibrant turquoise tilework on Man Mandir.",
                "built_century": "8th–15th Century",
            },
        ],
        "natural_spots": [
            {
                "name": "Kanha & Bandhavgarh Tiger Reserves",
                "category": "Sal & Bamboo Wilderness",
                "highlight": "Inspiration for Rudyard Kipling's Jungle Book with highest tiger density.",
            },
            {
                "name": "Bhedaghat Marble Rocks & Dhuandhar Falls (Jabalpur)",
                "category": "Narmada River Marble Gorge",
                "highlight": "Narmada river carved through 100-ft pure white marble canyons.",
            },
            {
                "name": "Pachmarhi Biosphere Reserve",
                "category": "Satpura Queen of Hills",
                "highlight": "Lush plateaus, natural rock shelters, and pre-historic cave art.",
            },
        ],
        "infra_connectivity": [
            "Bhopal & Indore Metro Rail Networks under active development.",
            "Delhi-Mumbai Expressway (MP Section across Ratlam).",
            "Bhopal-New Delhi Vande Bharat Express.",
        ],
        "culture_and_cuisine": "Poha Jalebi, Bhutte Ka Kees, Chanderi sarees, and Gond tribal paintings.",
        "best_time_to_visit": "October to March",
    },
    "Odisha": {
        "tagline": "India's Best Kept Secret (ଓଡ଼ିଶା)",
        "greeting": "Namaskar! (ନମସ୍କାର)",
        "accent_color": "#06B6D4",
        "architectural_marvels": [
            {
                "name": "Sun Temple at Konark",
                "type": "Kalinga Architectural Marvel (UNESCO)",
                "highlight": "Monumental chariot with 24 carved stone wheels serving as astronomical sundials.",
                "built_century": "13th Century",
            },
            {
                "name": "Jagannath Temple (Puri)",
                "type": "Monumental Kalinga Temple Architecture",
                "highlight": "65-meter deula spire, epic annual Ratha Yatra, and world's largest kitchen.",
                "built_century": "12th Century",
            },
        ],
        "natural_spots": [
            {
                "name": "Chilika Lake & Nalabana Bird Sanctuary",
                "category": "Asia's Largest Brackish Water Lagoon",
                "highlight": "Home to endangered Irrawaddy dolphins and over a million migratory birds.",
            },
            {
                "name": "Simlipal Biosphere Reserve & Tiger Reserve",
                "category": "Dense Sal Forest & Waterfalls",
                "highlight": "Home to rare melanistic (black) tigers, Joranda and Barehipani waterfalls.",
            },
            {
                "name": "Bhitarkanika National Park",
                "category": "Mangrove Wetland Ecosystem",
                "highlight": "Second largest mangrove ecosystem in India, giant saltwater crocodiles.",
            },
        ],
        "infra_connectivity": [
            "Coastal Economic Corridor & NH-316 Puri-Bhubaneswar highway.",
            "Vande Bharat Express (Howrah-Puri & Puri-Rourkela).",
            "Paradeep & Dhamra Deep-water Port Infrastructure.",
        ],
        "culture_and_cuisine": "Chhena Poda, Odissi classical dance, Pattachitra scroll art, and Sambalpuri sarees.",
        "best_time_to_visit": "October to March",
    },
}


def get_state_tourism(state_name: str) -> Dict[str, Any]:
    """Retrieve tourism, architectural, and natural spot data for a given Indian State."""
    if state_name in STATE_TOURISM_DATA:
        return STATE_TOURISM_DATA[state_name]
    
    # Generic fallback for any other state
    return {
        "tagline": f"Explore {state_name} - Incredible India",
        "greeting": "Namaste! (नमस्ते)",
        "accent_color": "#FF9933",
        "architectural_marvels": [
            {
                "name": f"Historic Monuments of {state_name}",
                "type": "Regional Architectural Heritage",
                "highlight": f"Centuries-old stone temples, stepwells, and forts of {state_name}.",
                "built_century": "Ancient & Medieval",
            }
        ],
        "natural_spots": [
            {
                "name": f"Protected Forests & Sanctuaries of {state_name}",
                "category": "Wildlife & Natural Ecosystem",
                "highlight": "Lush biodiversity, rivers, flora and fauna under ecological protection.",
            }
        ],
        "infra_connectivity": [
            f"National Highway corridors and Vande Bharat connectivity in {state_name}.",
            "PM Gati Shakti multi-modal logistics alignment.",
        ],
        "culture_and_cuisine": f"Traditional folklore, handicrafts, and regional culinary delicacies of {state_name}.",
        "best_time_to_visit": "October to March",
    }
