"""Dataset generator for PragatiGati:
1. Expands src/tourism_data.py with comprehensive state data, history, and booking codes.
2. Updates dashboard/data.js with RAW_PROJECTS enriched with infra_image_url and district_part,
   plus STATE_TOURISM and SCENIC_CORRIDORS.
"""

import json

from src import analytics, api

# 1. Curated 21 Indian States with Rich Historical Context and Airport/Rail Codes
STATE_TOURISM = {
    "Rajasthan": {
        "tagline": "The Land of Kings (पधारो म्हारे देश)",
        "greeting": "Khamma Ghani! (खम्मा घणी)",
        "accent_color": "#EA580C",
        "hero_image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Royal Sandstone & Stepwell Corridor",
        "architectural_marvels": [
            {
                "name": "Amber Fort & Palace (Jaipur)",
                "type": "Rajput-Mughal Fort Architecture",
                "highlight": "Mirror work in Sheesh Mahal, intricate ramparts, Maota Lake reflection.",
                "history": "Commissioned in 1592 CE by Raja Man Singh I of the Kachwaha Rajput clan, Amber Fort served as the royal seat of Jaipur's rulers. Blending red sandstone and white marble, it embodies the synthesis of Rajput martial grandeur and Mughal decorative artistry with its cooling water channels and celestial mirror mosaics.",
                "built_century": "16th Century (1592 CE)",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1000&q=80",
                "latitude": 26.9855,
                "longitude": 75.8513,
                "infra_link": "Delhi-Mumbai Expressway (NE-4) Jaipur Interchange",
                "nearest_airport": {
                    "name": "Jaipur International Airport",
                    "code": "JAI",
                },
                "nearest_railway": {"name": "Jaipur Junction", "code": "JP"},
            },
            {
                "name": "Chand Baori Stepwell (Abhaneri)",
                "type": "Hydraulic Ancient Architecture",
                "highlight": "3,500 narrow steps over 13 storeys; geometric mathematical symmetry.",
                "history": "Carved in the 9th Century CE by King Chanda of the Nikumbha dynasty, Chand Baori is one of India's deepest and largest subterranean stepwells. Descending 100 feet into the earth, its 3,500 chevron-patterned steps ensured round-the-year access to groundwater in the arid desert, acting as a cooling community pavilion dedicated to Harshat Mata.",
                "built_century": "9th Century CE",
                "badge": "Ancient Hydraulic Feat",
                "image_url": "https://images.unsplash.com/photo-1608958435020-e8a7109ba809?auto=format&fit=crop&w=1000&q=80",
                "latitude": 27.0072,
                "longitude": 76.6064,
                "infra_link": "NH-21 Agra-Jaipur Highway Corridor",
                "nearest_airport": {
                    "name": "Jaipur International Airport",
                    "code": "JAI",
                },
                "nearest_railway": {"name": "Bandikui Junction", "code": "BKI"},
            },
            {
                "name": "Mehrangarh Fort (Jodhpur)",
                "type": "Hilltop Citadel Architecture",
                "highlight": "Perched 400 feet above the Blue City; formidable 120-ft high basalt bastions.",
                "history": "Founded in 1459 CE by Rao Jodha, founder of Jodhpur, Mehrangarh stands atop a perpendicular cliff of columnar volcanic basalt. Its monumental ramparts preserved Rajasthan against centuries of siege, while its royal palaces like Moti Mahal and Phool Mahal house some of the finest gilded woodwork and royal palanquins in India.",
                "built_century": "15th Century (1459 CE)",
                "badge": "Citadel Architecture",
                "image_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1000&q=80",
                "latitude": 26.2978,
                "longitude": 73.0185,
                "infra_link": "Jodhpur Vande Bharat Express Terminal",
                "nearest_airport": {"name": "Jodhpur Airport", "code": "JDH"},
                "nearest_railway": {"name": "Jodhpur Junction", "code": "JU"},
            },
        ],
        "natural_spots": [
            {
                "name": "Ranthambore Tiger Reserve",
                "category": "Dry Deciduous Forest & Tiger Haven",
                "highlight": "Ancient 10th-century Chauhan fortress ruins nestled amid wild royal Bengal tiger territories.",
                "history": "Originally the private hunting preserve of the Maharajas of Jaipur, Ranthambore is home to a 1,000-year-old hilltop fort atop dramatic Aravali-Vindhya escarpments, now celebrated globally as a cornerstone of Project Tiger.",
                "badge": "Project Tiger Sanctuary",
                "image_url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1000&q=80",
                "latitude": 26.0173,
                "longitude": 76.5026,
                "infra_link": "Delhi-Mumbai Expressway Sawai Madhopur Spoke",
                "nearest_airport": {
                    "name": "Jaipur International Airport",
                    "code": "JAI",
                },
                "nearest_railway": {"name": "Sawai Madhopur Junction", "code": "SWM"},
            },
            {
                "name": "Sambhar Salt Lake",
                "category": "Ramsar Inland Salt Wetland",
                "highlight": "India's largest inland salt lake, winter haven for tens of thousands of pink flamingos.",
                "history": "Mentioned in the Mahabharata as part of the kingdom of king Vrishparva, Sambhar Lake has yielded salt through traditional solar evaporation brine pans for over a millennium, served by an antique narrow-gauge British salt railway.",
                "badge": "Ramsar Biosphere Site",
                "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1000&q=80",
                "latitude": 26.9167,
                "longitude": 75.0,
                "infra_link": "Jaipur-Ajmer 6-Lane Expressway (NH-48)",
                "nearest_airport": {
                    "name": "Jaipur International Airport",
                    "code": "JAI",
                },
                "nearest_railway": {"name": "Phulera Junction", "code": "FL"},
            },
        ],
        "infra_connectivity": [
            "Delhi-Mumbai Expressway (NE-4): 8-lane greenfield corridor cutting Delhi-Jaipur transit to 2.5 hours.",
            "Ajmer-Delhi Vande Bharat Express: High-speed rail corridor serving Jaipur and Alwar.",
            "Kishangarh Airport (KQH) & Jodhpur Airport expansion under UDAN scheme.",
        ],
        "culture_and_cuisine": "Dal Baati Churma, Ker Sangri, Ghoomar dance, Blue Pottery of Jaipur, and Bagru hand-block prints.",
        "best_time_to_visit": "October to March (Pleasant desert winter)",
    },
    "Kerala": {
        "tagline": "God's Own Country (ദൈവത്തിന്റെ സ്വന്തം നാട്)",
        "greeting": "Swagatham! (സ്വാഗതം)",
        "accent_color": "#059669",
        "hero_image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Western Ghats & Coastal Waterway Trail",
        "architectural_marvels": [
            {
                "name": "Sree Padmanabhaswamy Temple",
                "type": "Chera-Travancore Dravidian Architecture",
                "highlight": "16th-century Gopuram, 365 carved granite pillars, world's wealthiest temple vaults.",
                "history": "Rebuilt in its grand stone form in the 18th Century by Maharaja Marthanda Varma of Travancore, this sanctum is an architectural masterpiece of Kerala and Tamil Dravidian fusion. In 1750 CE, the Maharaja dedicated the entire kingdom to Lord Padmanabha, ruling as Padmanabhadasa (servant of the Lord).",
                "built_century": "8th–18th Century",
                "badge": "Sacred Architectural Wonder",
                "image_url": "https://images.unsplash.com/photo-1621847468516-1ed5d0df56fe?auto=format&fit=crop&w=1000&q=80",
                "latitude": 8.4831,
                "longitude": 76.9436,
                "infra_link": "Thiruvananthapuram Vande Bharat Terminal",
                "nearest_airport": {
                    "name": "Thiruvananthapuram International Airport",
                    "code": "TRV",
                },
                "nearest_railway": {
                    "name": "Thiruvananthapuram Central",
                    "code": "TVC",
                },
            },
            {
                "name": "Traditional Kettuvallam (Houseboats)",
                "type": "Indigenous Marine Architecture",
                "highlight": "Constructed without a single nail using Anjili timber lashed with coconut coir ropes.",
                "history": "Originally developed centuries ago as heavy grain barges called Kettuvallams to transport rice and spices across the Vembanad inland waterways, their vaulted canopies made of bamboo poles and palm fronds have evolved into world-famous floating architectural eco-villas.",
                "built_century": "Living Craft Heritage",
                "badge": "Eco Marine Architecture",
                "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1000&q=80",
                "latitude": 9.4981,
                "longitude": 76.3388,
                "infra_link": "Kochi Water Metro & Alleppey Waterway Hub",
                "nearest_airport": {
                    "name": "Cochin International Airport",
                    "code": "COK",
                },
                "nearest_railway": {
                    "name": "Alappuzha Railway Station",
                    "code": "ALLP",
                },
            },
        ],
        "natural_spots": [
            {
                "name": "Munnar Tea Valleys & Anamudi",
                "category": "Western Ghats High-Altitude Shola",
                "highlight": "Rolling emerald tea plantations, misty valleys, and home to endangered Nilgiri Tahr.",
                "history": "Soaring up to 2,695m at Anamudi—the highest peak in South India—Munnar's microclimate and ancient Montane Shola rainforests have preserved rare botanical species like the Neelakurinji flower that blooms once every 12 years.",
                "badge": "UNESCO Western Ghats",
                "image_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1000&q=80",
                "latitude": 10.0889,
                "longitude": 77.0595,
                "infra_link": "Kochi-Munnar NH-85 Mountain Highway",
                "nearest_airport": {
                    "name": "Cochin International Airport",
                    "code": "COK",
                },
                "nearest_railway": {"name": "Aluva Railway Station", "code": "AWY"},
            },
            {
                "name": "Alleppey & Vembanad Backwaters",
                "category": "Wetland & Lagoon Ecosystem",
                "highlight": "Interconnected canals, paddy fields cultivated up to 3 meters below sea level (Kuttanad).",
                "history": "Vembanad is India's longest lake and a Ramsar-protected wetland. The Kuttanad farming system here is one of only two in the world recognized by FAO for agriculture practiced below sea level using indigenous bunding bio-engineering.",
                "badge": "Ramsar Wetland Site",
                "image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1000&q=80",
                "latitude": 9.5826,
                "longitude": 76.3888,
                "infra_link": "National Waterway 3 (NW-3) Coastal Canal",
                "nearest_airport": {
                    "name": "Cochin International Airport",
                    "code": "COK",
                },
                "nearest_railway": {
                    "name": "Alappuzha Railway Station",
                    "code": "ALLP",
                },
            },
        ],
        "infra_connectivity": [
            "Kochi Water Metro: World's first integrated electric water transit network.",
            "Thiruvananthapuram-Kasargod Vande Bharat Express: High-speed coastal connectivity.",
            "Wayanad Twin-Tube Hill Highway Tunnel: All-weather Western Ghats transit.",
        ],
        "culture_and_cuisine": "Sadya, Appam with Stew, Kathakali, Kalaripayattu martial art, and boat races.",
        "best_time_to_visit": "September to March; Monsoon tourism in June-August",
    },
    "Uttar Pradesh": {
        "tagline": "The Heartland of Culture (उत्तर प्रदेश)",
        "greeting": "Pranam! (प्रणाम / राधे राधे)",
        "accent_color": "#D97706",
        "hero_image": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Sacred Ganga & Mughal Heritage Expressway",
        "architectural_marvels": [
            {
                "name": "Taj Mahal (Agra)",
                "type": "Mughal Marble Architecture",
                "highlight": "Flawless bilateral symmetry, translucent Makrana white marble, pietra dura inlay.",
                "history": "Commissioned in 1632 CE by Mughal Emperor Shah Jahan to house the tomb of his favorite wife, Mumtaz Mahal. Built over 20 years by an international guild of 20,000 artisans led by Ustad Ahmad Lahori, it stands as the zenith of Indo-Islamic architecture, celebrated universally as an eternal monument to love.",
                "built_century": "17th Century (1632–1653 CE)",
                "badge": "UNESCO World Heritage & 7 Wonders",
                "image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1000&q=80",
                "latitude": 27.1751,
                "longitude": 78.0421,
                "infra_link": "Taj Expressway & Delhi-Agra Rapid Rail Transit",
                "nearest_airport": {
                    "name": "Agra Civil Enclave (Kheria)",
                    "code": "AGR",
                },
                "nearest_railway": {"name": "Agra Cantt", "code": "AGC"},
            },
            {
                "name": "Varanasi Ganga Ghats & Vishwanath Corridor",
                "type": "Living Ancient Riverfront Architecture",
                "highlight": "84 sacred stone ghats lining the crescent sweep of the Ganges; subterranean corridor.",
                "history": "One of the world's oldest continuously inhabited civilizational cities, Varanasi (Kashi) was described in ancient Vedic scriptures. Its grand stone riverfront ghats were restored in the 18th century by Maratha Queen Ahilyabai Holkar and expanded with the modern Kashi Vishwanath Corridor connecting the temple directly to the holy Ganga.",
                "built_century": "Ancient Vedic to 18th Century Maratha Revival",
                "badge": "Ancient Living Civilisation",
                "image_url": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1000&q=80",
                "latitude": 25.3176,
                "longitude": 83.0062,
                "infra_link": "Purvanchal Expressway & Vande Bharat Express",
                "nearest_airport": {
                    "name": "Lal Bahadur Shastri International Airport",
                    "code": "VNS",
                },
                "nearest_railway": {"name": "Varanasi Junction", "code": "BSB"},
            },
            {
                "name": "Fatehpur Sikri Imperial Citadels",
                "type": "Red Sandstone Mughal Capital",
                "highlight": "Buland Darwaza (Door of Victory), Panch Mahal, Diwan-i-Khas central pillar.",
                "history": "Constructed in 1571 CE by Emperor Akbar to honor Sufi saint Shaikh Salim Chishti, Fatehpur Sikri served as the short-lived imperial capital of the Mughal Empire. Its pristine red sandstone courtyards showcase Akbar's eclectic vision, harmonizing Hindu, Persian, and Jain structural elements.",
                "built_century": "16th Century (1571 CE)",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1000&q=80",
                "latitude": 27.0945,
                "longitude": 77.6679,
                "infra_link": "Agra-Lucknow Expressway (ALE)",
                "nearest_airport": {"name": "Agra Civil Enclave", "code": "AGR"},
                "nearest_railway": {"name": "Fatehpur Sikri Station", "code": "FTS"},
            },
        ],
        "natural_spots": [
            {
                "name": "Dudhwa National Park & Tiger Reserve",
                "category": "Terai Alluvial Grassland Ecosystem",
                "highlight": "Lush Sal forests, swamp deer (Barasingha), and royal Bengal tigers near Nepal border.",
                "history": "Notified as a national park in 1977 due to the relentless efforts of conservationist 'Billy' Arjan Singh, Dudhwa represents the last surviving refuge of the Himalayan Terai alluvial grassland habitat in northern India.",
                "badge": "Terai Tiger Biosphere",
                "image_url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1000&q=80",
                "latitude": 28.5146,
                "longitude": 80.6481,
                "infra_link": "Gorakhpur-Siliguri Expressway Corridor",
                "nearest_airport": {
                    "name": "Chaudhary Charan Singh International Airport",
                    "code": "LKO",
                },
                "nearest_railway": {"name": "Mailani Junction", "code": "MLN"},
            }
        ],
        "infra_connectivity": [
            "Purvanchal & Ganga Expressways: Backbone of 6-lane high-speed expressway transit.",
            "Delhi-Meerut RRTS (Namo Bharat): India's first 160 km/h Regional Rapid Transit.",
            "Vande Bharat Express (New Delhi-Varanasi & Gorakhpur-Lucknow).",
        ],
        "culture_and_cuisine": "Awadhi Biryani, Tunday Kebabs, Banarasi Silk Sarees, Kathak classical dance, and Chikan embroidery.",
        "best_time_to_visit": "October to March",
    },
    "Maharashtra": {
        "tagline": "Gateway to the Nation (जय जय महाराष्ट्र माझा)",
        "greeting": "Jai Maharashtra! (जय महाराष्ट्र)",
        "accent_color": "#2563EB",
        "hero_image": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Konkan Coast & Western Ghats Skyrail",
        "architectural_marvels": [
            {
                "name": "Ajanta & Ellora Caves",
                "type": "Monolithic Rock-Cut Cave Architecture",
                "highlight": "Kailasa Temple (Cave 16) carved top-down from a single basalt cliff; 2nd BCE frescoes.",
                "history": "Ajanta comprises 30 Buddhist rock-cut caves dating from the 2nd Century BCE. Ellora, carved between the 6th and 10th centuries CE under Rashtrakuta kings, culminates in the Kailash Temple—the largest monolithic rock excavation in the world, carved vertically downwards removing 200,000 tonnes of basalt rock.",
                "built_century": "2nd Century BCE – 10th Century CE",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 20.0268,
                "longitude": 75.178,
                "infra_link": "Samruddhi Mahamarg (Mumbai-Nagpur Expressway)",
                "nearest_airport": {
                    "name": "Chhatrapati Sambhajinagar Airport",
                    "code": "IXU",
                },
                "nearest_railway": {
                    "name": "Aurangabad Railway Station",
                    "code": "AWB",
                },
            },
            {
                "name": "Mumbai Trans Harbour Link (Atal Setu)",
                "type": "Modern Oceanic Bridge Engineering",
                "highlight": "21.8 km oceanic sea bridge with orthotropic steel deck spans across Thane Creek.",
                "history": "Inaugurated in 2024, Atal Setu is India's longest oceanic sea bridge. Engineering marvel using seismic isolation bearings, reverse circulation drilling in marine basalt, and bird-friendly noise barriers to preserve flamingos in Sewri mudflats.",
                "built_century": "2024 CE",
                "badge": "Modern Engineering Feat",
                "image_url": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1000&q=80",
                "latitude": 18.96,
                "longitude": 72.95,
                "infra_link": "Navi Mumbai International Airport Expressway Spoke",
                "nearest_airport": {
                    "name": "Chhatrapati Shivaji Maharaj International Airport",
                    "code": "BOM",
                },
                "nearest_railway": {"name": "CSMT / Dadar", "code": "CSMT"},
            },
            {
                "name": "Chhatrapati Shivaji Maharaj Terminus (CSMT)",
                "type": "Victorian Gothic Revival & Indian Palace Motifs",
                "highlight": "High Victorian Gothic cathedral architecture with traditional Indian stone carvings.",
                "history": "Designed by British architect F.W. Stevens and completed in 1887 to mark Queen Victoria's Golden Jubilee, CSMT blends Italian Gothic Revival with Indian palace domes, turrets, and intricate stone gargoyles carved by students of Sir J.J. School of Art.",
                "built_century": "19th Century (1887 CE)",
                "badge": "UNESCO World Heritage Railway Station",
                "image_url": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1000&q=80",
                "latitude": 18.9402,
                "longitude": 72.8356,
                "infra_link": "Central Railway High-Speed Transit Hub",
                "nearest_airport": {
                    "name": "Chhatrapati Shivaji Maharaj International Airport",
                    "code": "BOM",
                },
                "nearest_railway": {"name": "CSMT Railway Station", "code": "CSMT"},
            },
        ],
        "natural_spots": [
            {
                "name": "Tadoba-Andhari Tiger Reserve",
                "category": "Dense Teak Forest & Wildlife Sanctuary",
                "highlight": "Maharashtra's oldest national park, home to dominant Royal Bengal tiger populations.",
                "history": "Named after the forest deity 'Taru' worshipped by indigenous Gond tribes, Tadoba was created as a wildlife sanctuary in 1955. Its pristine bamboo thickets and perennial lakes support high tiger and leopard densities.",
                "badge": "Jewel of Vidarbha Tiger Reserve",
                "image_url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1000&q=80",
                "latitude": 20.2185,
                "longitude": 79.3032,
                "infra_link": "Nagpur-Chandrapur 4-Lane Highway",
                "nearest_airport": {
                    "name": "Dr. Babasaheb Ambedkar International Airport",
                    "code": "NAG",
                },
                "nearest_railway": {"name": "Chandrapur Railway Station", "code": "CD"},
            }
        ],
        "infra_connectivity": [
            "Mumbai-Nagpur Samruddhi Mahamarg: 701 km access-controlled super-communication expressway.",
            "Mumbai-Goa & Mumbai-Solapur Vande Bharat Express routes.",
            "Navi Mumbai International Airport (NMIA) multi-modal hub.",
        ],
        "culture_and_cuisine": "Vada Pav, Misal Pav, Puran Poli, Lavani folk dance, and Warli indigenous tribal paintings.",
        "best_time_to_visit": "October to March; Monsoon magic in July-September",
    },
    "Uttarakhand": {
        "tagline": "Devbhoomi - Land of the Gods (देवभूमि)",
        "greeting": "Namaskar! (नमस्कार)",
        "accent_color": "#0284C7",
        "hero_image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The High-Altitude Himalayan Valley Way",
        "architectural_marvels": [
            {
                "name": "Kedarnath & Badrinath Himalayan Shrines",
                "type": "Nagara Himalayan Stone Architecture",
                "highlight": "Centuries-old grey stone temple standing resilient at 3,584m amid snow peaks.",
                "history": "Believed to have been originally established by the Pandavas and rebuilt by 8th-century philosopher Adi Shankaracharya, Kedarnath is built of massive interlocking stone slabs placed without mortar that withstood the cataclysmic 2013 Himalayan flash floods unscathed.",
                "built_century": "8th Century CE",
                "badge": "High-Altitude Sacred Temple",
                "image_url": "https://images.unsplash.com/photo-1605649487212-47bdab064df8?auto=format&fit=crop&w=1000&q=80",
                "latitude": 30.7352,
                "longitude": 79.0669,
                "infra_link": "Char Dham All-Weather Highway & Rishikesh-Karanprayag Rail Link",
                "nearest_airport": {
                    "name": "Jolly Grant Airport Dehradun",
                    "code": "DED",
                },
                "nearest_railway": {
                    "name": "Haridwar Junction / Rishikesh",
                    "code": "HW",
                },
            }
        ],
        "natural_spots": [
            {
                "name": "Jim Corbett National Park",
                "category": "Sub-Himalayan Foothill Ecosystem",
                "highlight": "India's first national park (1936), rolling grasslands (Chaurs), and Ramganga river.",
                "history": "Established in 1936 as Hailey National Park to protect the endangered Bengal tiger, it was renamed in honor of conservationist and author Jim Corbett. It pioneered Project Tiger in India in 1973.",
                "badge": "First National Park of India",
                "image_url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1000&q=80",
                "latitude": 29.53,
                "longitude": 78.7747,
                "infra_link": "Delhi-Dehradun Expressway Corridor",
                "nearest_airport": {"name": "Pantnagar Airport", "code": "PGH"},
                "nearest_railway": {"name": "Ramnagar Railway Station", "code": "RMR"},
            },
            {
                "name": "Valley of Flowers National Park",
                "category": "High-Altitude Alpine Meadow",
                "highlight": "Over 500 species of wild mountain flowers blooming against glacial peaks.",
                "history": "Discovered by mountaineer Frank S. Smythe in 1931, this UNESCO alpine valley blooms with rare endemic flora such as the Brahmakamal and blue poppy, nestled alongside sacred Hemkund Sahib lake.",
                "badge": "UNESCO World Heritage Nature",
                "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "latitude": 30.728,
                "longitude": 79.6053,
                "infra_link": "Joshimath-Badrinath All-Weather Road",
                "nearest_airport": {"name": "Jolly Grant Airport", "code": "DED"},
                "nearest_railway": {
                    "name": "Rishikesh Railway Station",
                    "code": "RKSH",
                },
            },
        ],
        "infra_connectivity": [
            "Char Dham All-Weather Highway: 889 km engineered mountain road network.",
            "Rishikesh-Karanprayag Rail Link: 125 km line with 105 km in state-of-the-art bored tunnels.",
            "Delhi-Dehradun Greenfield Expressway (cuts travel time from 6h to 2.5h).",
        ],
        "culture_and_cuisine": "Kafuli, Bal Mithai, Garhwali and Kumaoni folk songs, Aipan traditional ritual floor art.",
        "best_time_to_visit": "May to October (Valley blooms in July-August)",
    },
    "Tamil Nadu": {
        "tagline": "Land of Living Chola Temples (தமிழ்நாடு)",
        "greeting": "Vanakkam! (வணக்கம்)",
        "accent_color": "#DC2626",
        "hero_image": "https://images.unsplash.com/photo-1621847468516-1ed5d0df56fe?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Great Chola & Ocean Rail Odyssey",
        "architectural_marvels": [
            {
                "name": "Brihadisvara Temple (Thanjavur)",
                "type": "Great Chola Dravidian Architecture",
                "highlight": "216-ft monolithic granite Vimana capped by an 80-tonne granite Kumbam.",
                "history": "Built in 1010 CE by the legendary Chola Emperor Rajaraja I, the 'Big Temple' of Thanjavur is entirely built of interlocking granite in an area devoid of granite quarries. Its shadow-free design and thousand-year-old Tamil inscriptions document the zenith of maritime Chola civilization.",
                "built_century": "11th Century (1010 CE)",
                "badge": "UNESCO World Heritage Chola Temple",
                "image_url": "https://images.unsplash.com/photo-1621847468516-1ed5d0df56fe?auto=format&fit=crop&w=1000&q=80",
                "latitude": 10.7828,
                "longitude": 79.1318,
                "infra_link": "NH-36 Vikravandi-Thanjavur Corridor",
                "nearest_airport": {
                    "name": "Tiruchirappalli International Airport",
                    "code": "TRZ",
                },
                "nearest_railway": {"name": "Thanjavur Junction", "code": "TJ"},
            },
            {
                "name": "Meenakshi Amman Temple (Madurai)",
                "type": "Nayak Dynasty Dravidian Masterpiece",
                "highlight": "14 monumental towering gopurams encrusted with thousands of painted mythological figures.",
                "history": "Dating back to Sangam literature roots and reconstructed in its present form by Nayak King Tirumala Nayaka in the 17th Century, the temple features the Hall of Thousand Pillars where each granite column is sculpted with lifelike celestial beings and acoustic musical pillars.",
                "built_century": "16th-17th Century",
                "badge": "Architectural Icon of India",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 9.9195,
                "longitude": 78.1193,
                "infra_link": "Madurai-Bengaluru Vande Bharat Route",
                "nearest_airport": {"name": "Madurai Airport", "code": "IXM"},
                "nearest_railway": {"name": "Madurai Junction", "code": "MDU"},
            },
            {
                "name": "New Pamban Ocean Railway Bridge (Rameswaram)",
                "type": "Modern Oceanic Vertical-Lift Bridge",
                "highlight": "India's first vertical-lift sea bridge lifting 17 metres for cargo ships to pass.",
                "history": "Replacing the historic 1914 Scherzer rolling lift bridge across Palk Strait, this newly commissioned 2.05 km railway bridge incorporates stainless steel reinforcement and electromechanical vertical lift spans designed to endure cyclonic sea spray while linking the mainland to sacred Rameswaram island.",
                "built_century": "2024 CE",
                "badge": "Modern Engineering Ocean Milestone",
                "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
                "latitude": 9.2876,
                "longitude": 79.3129,
                "infra_link": "Rameswaram Ocean Rail Link",
                "nearest_airport": {"name": "Madurai Airport", "code": "IXM"},
                "nearest_railway": {
                    "name": "Rameswaram Railway Station",
                    "code": "RMM",
                },
            },
        ],
        "natural_spots": [
            {
                "name": "Nilgiri Biosphere & Mudumalai",
                "category": "UNESCO Biosphere Reserve",
                "highlight": "Dense jungle habitat of Asian elephants, Nilgiri Langurs, and Bengal tigers.",
                "history": "Forming the first biosphere reserve established in India (1986), the Nilgiris bridge the Eastern and Western Ghats, sheltering indigenous Toda tribes and centuries-old tea plantations.",
                "badge": "UNESCO Biosphere Sanctuary",
                "image_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1000&q=80",
                "latitude": 11.5623,
                "longitude": 76.5345,
                "infra_link": "NH-181 Coimbatore-Ooty Hill Highway",
                "nearest_airport": {
                    "name": "Coimbatore International Airport",
                    "code": "CJB",
                },
                "nearest_railway": {"name": "Udhagamandalam (Ooty)", "code": "UAM"},
            }
        ],
        "infra_connectivity": [
            "Bengaluru-Chennai Expressway (NE-5): 4-lane access-controlled greenfield expressway.",
            "Chennai-Coimbatore & Chennai-Mysuru Vande Bharat Express corridors.",
            "New Pamban Sea Bridge & Sagarmala Port modernisation at Chennai and Tuticorin.",
        ],
        "culture_and_cuisine": "Idli-Sambar, Chettinad cuisine, Bharatanatyam classical dance, Kanchipuram silk sarees.",
        "best_time_to_visit": "November to February",
    },
    "Gujarat": {
        "tagline": "Vibrant Gujarat (આપણું ગુજરાત)",
        "greeting": "Kem Cho! (કેમ છો)",
        "accent_color": "#F59E0B",
        "hero_image": "https://images.unsplash.com/photo-1624606275150-1df0480373e3?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The High-Speed Rail & White Desert Trail",
        "architectural_marvels": [
            {
                "name": "Statue of Unity (Ekta Nagar)",
                "type": "World's Tallest Monumental Engineering",
                "highlight": "182-metre bronze colossus overlooking Narmada; high-speed glass viewing gallery at 153m.",
                "history": "Inaugurated in 2018 to honor Sardar Vallabhbhai Patel, the Iron Man who unified 562 princely states into modern India. Designed by sculptor Ram V. Sutar and built by L&T with 1,700 tonnes of bronze plates, it stands nearly twice as tall as the Statue of Liberty.",
                "built_century": "2018 CE",
                "badge": "World's Tallest Statue",
                "image_url": "https://images.unsplash.com/photo-1624606275150-1df0480373e3?auto=format&fit=crop&w=1000&q=80",
                "latitude": 21.838,
                "longitude": 73.7191,
                "infra_link": "Vadodara-Ekta Nagar Electric Rail Link & Expressway",
                "nearest_airport": {"name": "Vadodara Airport", "code": "BDQ"},
                "nearest_railway": {"name": "Ekta Nagar (Kevadiya)", "code": "EKNR"},
            },
            {
                "name": "Rani ki Vav Stepwell (Patan)",
                "type": "Maru-Gurjara Inverted Temple Stepwell",
                "highlight": "Subterranean stepwell featuring over 500 principal sculptures of Vishnu avatars.",
                "history": "Commissioned in 1063 CE by Queen Udayamati in memory of King Bhima I of the Solanki (Chaulukya) dynasty. Conceived as an inverted subterranean temple, it showcases the pinnacle of Maru-Gurjara stepped water engineering, preserved for centuries beneath silt from the Saraswati river.",
                "built_century": "11th Century (1063 CE)",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1608958435020-e8a7109ba809?auto=format&fit=crop&w=1000&q=80",
                "latitude": 23.8589,
                "longitude": 72.1017,
                "infra_link": "Ahmedabad-Patan 4-Lane Highway Corridor",
                "nearest_airport": {
                    "name": "Sardar Vallabhbhai Patel International Airport",
                    "code": "AMD",
                },
                "nearest_railway": {"name": "Patan Railway Station", "code": "PTN"},
            },
        ],
        "natural_spots": [
            {
                "name": "Great Rann of Kutch",
                "category": "Endless White Salt Desert Marsh",
                "highlight": "Vast expanse of shimmering salt desert, host to the world-famous Rann Utsav.",
                "history": "Part of the ancient Indus river delta uplifted by tectonic earthquakes centuries ago, the Great Rann is one of the largest salt deserts in the world, glowing under full moon nights and winter flamingo migrations.",
                "badge": "White Salt Desert Wonder",
                "image_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1000&q=80",
                "latitude": 23.8344,
                "longitude": 69.8327,
                "infra_link": "Bhuj Airport & Khavda Road Corridor",
                "nearest_airport": {"name": "Bhuj Airport", "code": "BHJ"},
                "nearest_railway": {"name": "Bhuj Railway Station", "code": "BHUJ"},
            },
            {
                "name": "Gir National Park",
                "category": "Asiatic Lion Sanctuary",
                "highlight": "The only natural wild habitat of the endangered Asiatic Lion (Panthera leo persica) on Earth.",
                "history": "Protected by the visionary Nawab of Junagadh in 1900 when barely 20 lions remained, Gir now shelters over 700 wild Asiatic lions in dry deciduous teak forests, representing one of Asia's premier conservation triumphs.",
                "badge": "Sole Asiatic Lion Habitat",
                "image_url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1000&q=80",
                "latitude": 21.1243,
                "longitude": 70.8242,
                "infra_link": "Rajkot-Junagadh-Somnath Highway",
                "nearest_airport": {
                    "name": "Rajkot International Airport (Hirasar)",
                    "code": "HSR",
                },
                "nearest_railway": {"name": "Junagadh Junction", "code": "JND"},
            },
        ],
        "infra_connectivity": [
            "Mumbai-Ahmedabad High-Speed Rail (Bullet Train): India's flagship high-speed rail corridor.",
            "Delhi-Mumbai Expressway (Gujarat Packages) & Dholera Greenfield Expressway.",
            "Vande Bharat Express (Mumbai-Gandhinagar & Ahmedabad-Jamnagar).",
        ],
        "culture_and_cuisine": "Dhokla, Thepla, Garba & Dandiya Raas, Patola double-ikat silk weaving.",
        "best_time_to_visit": "November to February (Rann Utsav Season)",
    },
    "Assam": {
        "tagline": "Awesome Assam (অসম)",
        "greeting": "Nomoskar! (নমস্কাৰ)",
        "accent_color": "#16A34A",
        "hero_image": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Great Riverine & Tea Garden Route",
        "architectural_marvels": [
            {
                "name": "Bogibeel Rail-Road Bridge",
                "type": "Heavy Infrastructure River Crossing",
                "highlight": "4.94 km longest rail-cum-road bridge in India spanning the mighty Brahmaputra river.",
                "history": "Commissioned in 2018, Bogibeel is a double-deck steel truss bridge designed to withstand seismic Zone V earthquakes and sub-zero glacial currents, directly connecting Upper Assam and Arunachal Pradesh.",
                "built_century": "2018 CE",
                "badge": "Engineering River Milestone",
                "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
                "latitude": 27.4,
                "longitude": 94.9,
                "infra_link": "Dibrugarh-Dhemaji Frontier Rail Link",
                "nearest_airport": {
                    "name": "Dibrugarh Airport (Mohanbari)",
                    "code": "DIB",
                },
                "nearest_railway": {
                    "name": "Dibrugarh Railway Station",
                    "code": "DBRG",
                },
            },
            {
                "name": "Kamakhya Shakti Peetha (Guwahati)",
                "type": "Nilachala Style Sacred Temple",
                "highlight": "Historic beehive shikhara temple atop Nilachal Hill; sacred center of Tantric traditions.",
                "history": "One of the oldest of the 51 Shakti Peethas, rebuilt in 1565 CE by King Naranarayan of the Koch dynasty after destruction. Its unique Nilachala architectural hybrid combines a cruciform sanctum with a bulbous multi-sided dome.",
                "built_century": "Ancient to 1565 CE",
                "badge": "Sacred Tantric Heritage",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 26.1664,
                "longitude": 91.7054,
                "infra_link": "Guwahati Airport & Vande Bharat Rail Hub",
                "nearest_airport": {
                    "name": "Lokpriya Gopinath Bordoloi International Airport",
                    "code": "GAU",
                },
                "nearest_railway": {"name": "Guwahati Railway Station", "code": "GHY"},
            },
        ],
        "natural_spots": [
            {
                "name": "Kaziranga National Park",
                "category": "UNESCO World Heritage Sanctuary",
                "highlight": "Sanctuary for two-thirds of the entire world population of Great One-Horned Rhinoceroses.",
                "history": "Established as a reserve forest in 1905 by Lord Curzon at the urging of his wife Mary Curzon, Kaziranga's tall elephant grass and Brahmaputra floodplains nurture the highest density of wild rhinos, tigers, and Asiatic wild water buffaloes on Earth.",
                "badge": "UNESCO Rhino Sanctuary",
                "image_url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1000&q=80",
                "latitude": 26.5775,
                "longitude": 93.1711,
                "infra_link": "Asian Highway 1 (AH-1 / NH-715)",
                "nearest_airport": {"name": "Jorhat Airport (Rowriah)", "code": "JRH"},
                "nearest_railway": {"name": "Furkating Junction", "code": "FKG"},
            }
        ],
        "infra_connectivity": [
            "Bogibeel Rail-cum-Road Bridge over Brahmaputra.",
            "National Waterway 2 (NW-2): Luxury river cruise and freight corridor.",
            "Guwahati-New Jalpaiguri Vande Bharat Express.",
        ],
        "culture_and_cuisine": "Assam Tea, Bihu dance, Muga Golden Silk, and Kaji Nemu.",
        "best_time_to_visit": "October to April",
    },
    "Madhya Pradesh": {
        "tagline": "The Heart of Incredible India (मध्य प्रदेश)",
        "greeting": "Namaste! (नमस्कार)",
        "accent_color": "#8B5CF6",
        "hero_image": "https://images.unsplash.com/photo-1605649487212-47bdab064df8?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Chandela & Great Stupa Heritage Way",
        "architectural_marvels": [
            {
                "name": "Khajuraho Group of Monuments",
                "type": "Chandela Nagara Architecture",
                "highlight": "Intricately carved sandstone temples celebrating spiritual and aesthetic human life.",
                "history": "Built between 950 and 1050 CE by the Chandela Rajput dynasty, Khajuraho temples represent the pinnacle of North Indian Nagara temple architecture. Its surviving 25 sandstone temples feature breathtaking carvings depicting cosmology, music, celestial dancers, and classical erotic sculptures.",
                "built_century": "10th-11th Century (950-1050 CE)",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1605649487212-47bdab064df8?auto=format&fit=crop&w=1000&q=80",
                "latitude": 24.8318,
                "longitude": 79.9199,
                "infra_link": "Bundelkhand Expressway Link & Khajuraho Airport",
                "nearest_airport": {"name": "Khajuraho Airport", "code": "HJR"},
                "nearest_railway": {
                    "name": "Khajuraho Railway Station",
                    "code": "KURJ",
                },
            },
            {
                "name": "Great Stupa at Sanchi",
                "type": "Ancient Buddhist Stone Architecture",
                "highlight": "3rd Century BCE hemispherical dome commissioned by Emperor Ashoka; four carved Toranas.",
                "history": "Commissioned by Mauryan Emperor Ashoka in the 3rd Century BCE over the relics of the Buddha, the Great Stupa at Sanchi is the oldest stone structure in India. Its four ornamental ceremonial gateways (Toranas) represent the highest achievement of early Buddhist narrative stone sculpture.",
                "built_century": "3rd Century BCE to 1st Century CE",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 23.4793,
                "longitude": 77.7397,
                "infra_link": "Bhopal-Bina Mainline & NH-146",
                "nearest_airport": {"name": "Raja Bhoj Airport Bhopal", "code": "BHO"},
                "nearest_railway": {"name": "Sanchi / Bhopal Junction", "code": "BPL"},
            },
        ],
        "natural_spots": [
            {
                "name": "Bhedaghat Marble Rocks & Dhuandhar",
                "category": "Narmada River Marble Gorge",
                "highlight": "Narmada river carved through 100-ft pure white marble canyons culminating in mist falls.",
                "history": "Carved by the Narmada River over millions of years through deep beds of magnesium-limestone marble, Bhedaghat is renowned for its sheer shining white cliffs that shift colors under moonlit boat journeys.",
                "badge": "Geo-Heritage River Canyon",
                "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "latitude": 23.1311,
                "longitude": 79.8006,
                "infra_link": "Jabalpur Vande Bharat Hub",
                "nearest_airport": {"name": "Jabalpur Airport (Dumna)", "code": "JLR"},
                "nearest_railway": {"name": "Jabalpur Junction", "code": "JBP"},
            }
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
        "hero_image": "https://images.unsplash.com/photo-1609137144820-25642d992e59?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Kalinga Coastal & Sun Temple Route",
        "architectural_marvels": [
            {
                "name": "Sun Temple at Konark",
                "type": "Kalinga Architectural Marvel",
                "highlight": "Monumental chariot with 24 carved stone wheels serving as astronomical sundials.",
                "history": "Constructed in 1250 CE by King Narasimhadeva I of the Eastern Ganga dynasty, the Konark temple was conceived as a cosmic chariot for the Sun God Surya, pulled by seven stone horses. The 24 intricately carved wheels act as functioning sundials with shadows calculating exact time down to minutes.",
                "built_century": "13th Century (1250 CE)",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1609137144820-25642d992e59?auto=format&fit=crop&w=1000&q=80",
                "latitude": 19.8876,
                "longitude": 86.0945,
                "infra_link": "NH-316 Coastal Economic Corridor",
                "nearest_airport": {
                    "name": "Biju Patnaik International Airport",
                    "code": "BBI",
                },
                "nearest_railway": {"name": "Puri Railway Station", "code": "PURI"},
            },
            {
                "name": "Jagannath Temple (Puri)",
                "type": "Sacred Kalinga Temple Architecture",
                "highlight": "65-meter towering curvilinear Shikhara; home to the world's largest open community kitchen.",
                "history": "Built in the 12th Century CE by King Anantavarman Chodaganga Deva, this sacred Char Dham temple is famed for its wooden deities, massive flag changing rituals against the ocean wind, and the annual Ratha Yatra pulling monumental multi-storey wooden chariots.",
                "built_century": "12th Century CE",
                "badge": "Char Dham Sacred Shikhara",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 19.8048,
                "longitude": 85.8179,
                "infra_link": "Howrah-Puri Vande Bharat Express",
                "nearest_airport": {
                    "name": "Biju Patnaik International Airport",
                    "code": "BBI",
                },
                "nearest_railway": {"name": "Puri Railway Station", "code": "PURI"},
            },
        ],
        "natural_spots": [
            {
                "name": "Chilika Lake & Nalabana",
                "category": "Asia's Largest Brackish Water Lagoon",
                "highlight": "Home to endangered Irrawaddy dolphins and over a million migratory Siberian birds.",
                "history": "Designated India's first Ramsar wetland in 1981, Chilika is an ecological paradise connected to the Bay of Bengal through a narrow channel, supporting thousands of fishing families and rare marine biodiversity.",
                "badge": "Ramsar Wetland Biosphere",
                "image_url": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1000&q=80",
                "latitude": 19.68,
                "longitude": 85.33,
                "infra_link": "Howrah-Chennai Main Line & Puri Vande Bharat",
                "nearest_airport": {
                    "name": "Biju Patnaik International Airport",
                    "code": "BBI",
                },
                "nearest_railway": {"name": "Balugaon Railway Station", "code": "BALU"},
            }
        ],
        "infra_connectivity": [
            "Coastal Economic Corridor & NH-316 Puri-Bhubaneswar highway.",
            "Vande Bharat Express (Howrah-Puri & Puri-Rourkela).",
            "Paradeep & Dhamra Deep-water Port Infrastructure.",
        ],
        "culture_and_cuisine": "Chhena Poda, Odissi classical dance, Pattachitra scroll art, and Sambalpuri sarees.",
        "best_time_to_visit": "October to March",
    },
    "Karnataka": {
        "tagline": "One State, Many Worlds (ಕರ್ನಾಟಕ)",
        "greeting": "Namaskara! (ನಮಸ್ಕಾರ)",
        "accent_color": "#D97706",
        "hero_image": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Vijayanagara Stone Empire & Malnad Trail",
        "architectural_marvels": [
            {
                "name": "Hampi Group of Monuments",
                "type": "Vijayanagara Imperial Architecture",
                "highlight": "Monolithic stone chariot at Vittala Temple; musical granite pillars and boulder citadel.",
                "history": "Capital of the opulent Vijayanagara Empire from 1336 to 1565 CE, Hampi was described by Persian and Portuguese chronicles as one of the largest and richest metropolises in the medieval world. Spread across 4,100 hectares of rugged boulder hills on the Tungabhadra riverbanks, it features royal baths, elephant stables, and the iconic Stone Chariot.",
                "built_century": "14th-16th Century",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 15.335,
                "longitude": 76.46,
                "infra_link": "Bengaluru-Hospet Vande Bharat & NH-50",
                "nearest_airport": {
                    "name": "Jindal Vijayanagar Airport (Toranagallu)",
                    "code": "VDY",
                },
                "nearest_railway": {"name": "Hosapete Junction", "code": "HPT"},
            },
            {
                "name": "Mysore Palace (Amba Vilas)",
                "type": "Indo-Saracenic Royal Palace",
                "highlight": "Illuminated by 97,000 electric bulbs on festive nights; mahogany carvings and stained glass.",
                "history": "Commissioned in 1897 by Maharani Vani Vilas Sannidhana and Maharaja Krishnaraja Wadiyar IV, designed by British architect Henry Irwin. The palace seamlessly blends Hindu, Rajput, Islamic, and Gothic architectural motifs, famed worldwide for the vibrant Dasara royal elephant procession.",
                "built_century": "1912 CE",
                "badge": "Royal Architectural Icon",
                "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1000&q=80",
                "latitude": 12.3051,
                "longitude": 76.6551,
                "infra_link": "Bengaluru-Mysuru 10-Lane Expressway",
                "nearest_airport": {"name": "Mysore Airport", "code": "MYQ"},
                "nearest_railway": {"name": "Mysuru Junction", "code": "MYS"},
            },
        ],
        "natural_spots": [
            {
                "name": "Coorg Coffee Highlands & Abbey Falls",
                "category": "Western Ghats Mist Shola Forest",
                "highlight": "Fragrant arabica coffee estates, cascading waterfalls, and sacred Cauvery river source.",
                "history": "Known as the 'Scotland of India', Kodagu (Coorg) was an independent princely territory of the Kodava warrior clan before integration. Its high-altitude mist and tropical rainfall support rich biodiverse wildlife and spice plantations.",
                "badge": "Western Ghats Coffee Haven",
                "image_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1000&q=80",
                "latitude": 12.4244,
                "longitude": 75.7382,
                "infra_link": "Mysuru-Madikeri 4-Lane Highway",
                "nearest_airport": {
                    "name": "Mangaluru International Airport",
                    "code": "IXE",
                },
                "nearest_railway": {"name": "Mysuru Junction", "code": "MYS"},
            }
        ],
        "infra_connectivity": [
            "Bengaluru-Mysuru 10-Lane Expressway (cuts travel time to 75 minutes).",
            "Bengaluru-Dharwad & Bengaluru-Hyderabad Vande Bharat Express.",
            "Namma Metro Bengaluru Phase-2 Expansion & Kempegowda T2 Terminal.",
        ],
        "culture_and_cuisine": "Bisi Bele Bath, Mysore Pak, Yakshagana dance-theatre, and Mysore Silk sarees.",
        "best_time_to_visit": "October to March",
    },
    "Himachal Pradesh": {
        "tagline": "Land of the Gods (हिमाचल प्रदेश)",
        "greeting": "Namaste! (नमस्ते)",
        "accent_color": "#0284C7",
        "hero_image": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The High-Altitude Tunnel & Spiti Valley Trail",
        "architectural_marvels": [
            {
                "name": "Atal Tunnel Rohtang",
                "type": "High-Altitude Highway Tunnel Engineering",
                "highlight": "9.02 km world's longest highway tunnel above 10,000 feet, bypassing Rohtang blizzard pass.",
                "history": "Opened in 2020 by BRO, Atal Tunnel is an engineering triumph cut through the pir panjal range using the New Austrian Tunnelling Method (NATM). It secures all-weather connectivity to the isolated Lahaul-Spiti valley throughout harsh winters.",
                "built_century": "2020 CE",
                "badge": "World Record Mountain Tunnel",
                "image_url": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
                "latitude": 32.3619,
                "longitude": 77.0375,
                "infra_link": "Manali-Leh Strategic Highway (NH-3)",
                "nearest_airport": {
                    "name": "Kullu-Manali Airport (Bhuntar)",
                    "code": "KUU",
                },
                "nearest_railway": {"name": "Chandigarh Junction", "code": "CDG"},
            },
            {
                "name": "Kalka-Shimla Mountain Railway",
                "type": "UNESCO Colonial Narrow-Gauge Railway",
                "highlight": "Built in 1903 with 102 tunnels, 864 arched bridges, and breathtaking Himalayan viaducts.",
                "history": "Engineered during the British Raj to connect Shimla—the summer capital of British India—the 96-km railway climbs from 656m to 2,076m elevation. Its multi-arch stone viaducts resemble Roman aqueducts and are celebrated on the UNESCO Mountain Railways of India list.",
                "built_century": "1903 CE",
                "badge": "UNESCO Mountain Railway",
                "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
                "latitude": 31.1048,
                "longitude": 77.1734,
                "infra_link": "Kalka-Shimla Toy Train & Himalayan Expressway",
                "nearest_airport": {
                    "name": "Shimla Airport (Jubbarhatti)",
                    "code": "SLV",
                },
                "nearest_railway": {"name": "Shimla Railway Station", "code": "SML"},
            },
        ],
        "natural_spots": [
            {
                "name": "Spiti Valley & Key Monastery",
                "category": "Cold High-Altitude Mountain Desert",
                "highlight": "11th-century Tibetan Buddhist fortress monastery perched at 13,668 feet in moonscape valleys.",
                "history": "Known as the 'Middle Land' between India and Tibet, Spiti has preserved ancient Gelugpa Buddhist monastic traditions, fossil-rich geological strata, and crystal-clear starscapes.",
                "badge": "Himalayan Buddhist Sanctuary",
                "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "latitude": 32.298,
                "longitude": 78.012,
                "infra_link": "Atal Tunnel & Sumdo-Kaza Road",
                "nearest_airport": {"name": "Kullu-Manali Airport", "code": "KUU"},
                "nearest_railway": {"name": "Chandigarh Junction", "code": "CDG"},
            }
        ],
        "infra_connectivity": [
            "Atal Tunnel (9.02 km) all-weather passage.",
            "Kiratpur-Nerchowk 4-lane Himalayan expressway corridor.",
            "Amb Andaura - New Delhi Vande Bharat Express.",
        ],
        "culture_and_cuisine": "Siddu, Dham festive feast, Kullu woolen shawls, and Nati traditional folk dance.",
        "best_time_to_visit": "May to October for roads; December to February for snow",
    },
    "Jammu & Kashmir": {
        "tagline": "Paradise on Earth (جنة نظیر)",
        "greeting": "Aadaab! (آداب / नमस्कार)",
        "accent_color": "#4F46E5",
        "hero_image": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Himalayan Skyway & Chenab Arch Route",
        "architectural_marvels": [
            {
                "name": "Chenab Rail Arch Bridge",
                "type": "World's Highest Railway Arch Bridge",
                "highlight": "Soaring 359 metres above the Chenab riverbed—35 metres taller than the Eiffel Tower.",
                "history": "Constructed as the jewel of the Udhampur-Srinagar-Baramulla Rail Link (USBRL), the 1,315m steel arch bridge is designed to withstand blast resistance, hurricane winds up to 260 km/h, and minus-20 degree Himalayan temperatures, bringing seamless train connectivity to Kashmir valley for the first time.",
                "built_century": "2024 CE",
                "badge": "World's Highest Arch Railway Bridge",
                "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
                "latitude": 33.15,
                "longitude": 75.14,
                "infra_link": "USBRL Kashmir All-Weather Rail Link",
                "nearest_airport": {"name": "Jammu Airport", "code": "IXJ"},
                "nearest_railway": {
                    "name": "Shri Mata Vaishno Devi Katra",
                    "code": "SVDK",
                },
            },
            {
                "name": "Martand Sun Temple Colonnades",
                "type": "Karkota Kashmiri Stone Temple",
                "highlight": "Monumental Greek-influenced stone peristyle courtyard and temple sanctuary atop Anantnag plateau.",
                "history": "Built in the 8th Century CE by Emperor Lalitaditya Muktapida of the Karkota dynasty, Martand synthesized Gandharan, Gupta, and Greco-Roman architectural forms into a distinctive Kashmiri classical style, commanding panoramic views of the Pir Panjal mountains.",
                "built_century": "8th Century CE (725–756 CE)",
                "badge": "Ancient Classical Sun Temple",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 33.7461,
                "longitude": 75.2208,
                "infra_link": "Jammu-Srinagar National Highway (NH-44)",
                "nearest_airport": {
                    "name": "Sheikh ul-Alam International Airport Srinagar",
                    "code": "SXR",
                },
                "nearest_railway": {"name": "Anantnag Railway Station", "code": "ANT"},
            },
        ],
        "natural_spots": [
            {
                "name": "Dal Lake & Shikaras (Srinagar)",
                "category": "High-Altitude Urban Himalayan Lake",
                "highlight": "Intricately carved cedarwood houseboats, floating vegetable markets, and Mughal gardens.",
                "history": "Framed by the Zabarwan hills, Dal Lake was patronized by Mughal Emperors Jahangir and Shah Jahan who laid out Nishat and Shalimar Bagh terrace gardens with fountains fed by snowmelt streams.",
                "badge": "Jewel in the Crown of Kashmir",
                "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
                "latitude": 34.0837,
                "longitude": 74.7973,
                "infra_link": "Srinagar Smart City & Vande Bharat Hub",
                "nearest_airport": {
                    "name": "Srinagar International Airport",
                    "code": "SXR",
                },
                "nearest_railway": {"name": "Srinagar Railway Station", "code": "SINA"},
            }
        ],
        "infra_connectivity": [
            "USBRL Direct Railway Link to Kashmir with Vande Bharat Express.",
            "Zojila Tunnel (14.15 km) & Z-Morh Tunnel for all-weather Ladakh transit.",
            "Banihal-Qazigund Rail Tunnel and NH-44 four-laning.",
        ],
        "culture_and_cuisine": "Wazwan royal banquet, Kahwa green tea with saffron, Pashmina shawls, and paper-mâché art.",
        "best_time_to_visit": "April to October (Spring tulips and autumn chinar) or winter for snow sports",
    },
    "West Bengal": {
        "tagline": "The Cultural Capital (পশ্চিমবঙ্গ)",
        "greeting": "Nomoshkar! (নমস্কার)",
        "accent_color": "#0D9488",
        "hero_image": "https://images.unsplash.com/photo-1558431382-27e303142255?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Grand Colonial Maidan & Darjeeling Toy Train",
        "architectural_marvels": [
            {
                "name": "Victoria Memorial (Kolkata)",
                "type": "Indo-Saracenic & British Empire Marble Monument",
                "highlight": "Magnificent white Makrana marble monument with 16-foot bronze Angel of Victory.",
                "history": "Dedicated to Queen Victoria and completed in 1921 under design by William Emerson, President of the RIBA, this monumental marble edifice incorporates Mughal decorative minarets, Italian Renaissance sculptures, and expansive formal reflecting gardens.",
                "built_century": "1921 CE",
                "badge": "Historic Marble Landmark",
                "image_url": "https://images.unsplash.com/photo-1558431382-27e303142255?auto=format&fit=crop&w=1000&q=80",
                "latitude": 22.5448,
                "longitude": 88.3426,
                "infra_link": "Kolkata Underwater Metro & Vidyasagar Setu",
                "nearest_airport": {
                    "name": "Netaji Subhash Chandra Bose International Airport",
                    "code": "CCU",
                },
                "nearest_railway": {"name": "Howrah Junction", "code": "HWH"},
            },
            {
                "name": "Darjeeling Himalayan Railway (Toy Train)",
                "type": "UNESCO Mountain Narrow-Gauge Railway",
                "highlight": "Opened in 1881, famous for Batasia Loop and spiral reverse zigzags overlooking Kanchenjunga.",
                "history": "A pioneering 2-foot narrow gauge mountain railway scaling 7,000 feet of Himalayan terrain without rack-and-pinion gears. Its vintage steam locomotives still chug across tea estates, preserved under UNESCO World Heritage protection.",
                "built_century": "1881 CE",
                "badge": "UNESCO Mountain Railway",
                "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
                "latitude": 27.041,
                "longitude": 88.2663,
                "infra_link": "Siliguri-Darjeeling Hill Cart Road (NH-110)",
                "nearest_airport": {
                    "name": "Bagdogra International Airport",
                    "code": "IXB",
                },
                "nearest_railway": {"name": "New Jalpaiguri Junction", "code": "NJP"},
            },
        ],
        "natural_spots": [
            {
                "name": "Sundarbans Mangrove Tiger Biosphere",
                "category": "World's Largest Tidal Halophytic Mangrove Delta",
                "highlight": "Tidal delta of Ganges-Brahmaputra, home to amphibious Royal Bengal tigers and Estuarine crocodiles.",
                "history": "Spanning 10,000 sq km across India and Bangladesh, the Sundarbans mangrove labyrinth is named after the 'Sundari' mangrove tree and represents one of the most productive marine-terrestrial ecosystems on Earth.",
                "badge": "UNESCO World Heritage Biosphere",
                "image_url": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1000&q=80",
                "latitude": 21.9497,
                "longitude": 88.8999,
                "infra_link": "National Waterway 1 (NW-1) River Corridor",
                "nearest_airport": {
                    "name": "Netaji Subhash Chandra Bose International Airport",
                    "code": "CCU",
                },
                "nearest_railway": {"name": "Canning Railway Station", "code": "CAN"},
            }
        ],
        "infra_connectivity": [
            "Kolkata Underwater Metro (India's first underwater metro tunnel beneath Hooghly river).",
            "Howrah-NJP & Howrah-Puri Vande Bharat Express corridors.",
            "Kolkata-Siliguri 4-lane Highway Corridor.",
        ],
        "culture_and_cuisine": "Rosogolla, Shorshe Ilish, Durga Puja festival (UNESCO Intangible Heritage), and Rabindra Sangeet.",
        "best_time_to_visit": "October to March",
    },
    "Goa": {
        "tagline": "Pearl of the Orient (गोंय)",
        "greeting": "Dev Boro Dis Dium! (देव बरे दीस दिव)",
        "accent_color": "#EA580C",
        "hero_image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Konkan Coastal Forts & Sea Breeze Trail",
        "architectural_marvels": [
            {
                "name": "Basilica of Bom Jesus (Old Goa)",
                "type": "UNESCO Baroque Church Architecture",
                "highlight": "1605 CE laterite facade holding the sacred silver casket of St. Francis Xavier.",
                "history": "One of the finest examples of Baroque and Manueline architecture in Asia, completed in 1605. Built of unplastered black laterite stone, it contains intricately gilded wood altars and ceiling murals that reflect four centuries of Indo-Portuguese cultural exchange.",
                "built_century": "1605 CE",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1000&q=80",
                "latitude": 15.5008,
                "longitude": 73.9116,
                "infra_link": "Atal Setu Mandovi Cable Bridge & NH-66",
                "nearest_airport": {
                    "name": "Manohar International Airport Mopa",
                    "code": "GOX",
                },
                "nearest_railway": {"name": "Madgaon Junction", "code": "MAO"},
            }
        ],
        "natural_spots": [
            {
                "name": "Dudhsagar Waterfalls Rail Viaduct",
                "category": "Four-Tiered Mountain Waterfall",
                "highlight": "310m milky white cascade tumbling down Western Ghats with trains crossing its misty gorge.",
                "history": "One of India's tallest waterfalls located on the Mandovi River along the Goa-Karnataka border, famed for the dramatic railway viaduct crossing directly in front of the thundering water spray.",
                "badge": "Majestic Mountain Falls",
                "image_url": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1000&q=80",
                "latitude": 15.3144,
                "longitude": 74.3144,
                "infra_link": "Konkan Railway Ghat Section",
                "nearest_airport": {
                    "name": "Dabolim International Airport",
                    "code": "GOI",
                },
                "nearest_railway": {"name": "Kulem Railway Station", "code": "QLM"},
            }
        ],
        "infra_connectivity": [
            "Zuari New 8-Lane Cable-Stayed Bridge.",
            "Manohar International Airport at Mopa (GOX).",
            "Mumbai CSMT - Madgaon Vande Bharat Express.",
        ],
        "culture_and_cuisine": "Goan Fish Curry, Bebinca dessert, Feni, and vibrant Carnival parades.",
        "best_time_to_visit": "November to February",
    },
    "Punjab": {
        "tagline": "The Land of Five Rivers (ਪੰਜਾਬ - Punjab)",
        "greeting": "Sat Sri Akal! (ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ)",
        "accent_color": "#F59E0B",
        "hero_image": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Golden Sanctum & Grand Trunk Heritage Trail",
        "architectural_marvels": [
            {
                "name": "Sri Harmandir Sahib (Golden Temple)",
                "type": "Sikh Sacred Architecture",
                "highlight": "Gilded gold-leaf sanctum floating in the sacred Amrit Sarovar; Guru ka Langar feeding 100,000 daily.",
                "history": "Founded in 1577 CE by Guru Ram Das Ji and designed by Guru Arjan Dev Ji with four open entrances welcoming people of all faiths. Re-gilded in pure gold by Maharaja Ranjit Singh in 1830, it represents the supreme spiritual and temporal center of Sikhism.",
                "built_century": "16th-19th Century",
                "badge": "Supreme Spiritual Monument",
                "image_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1000&q=80",
                "latitude": 31.62,
                "longitude": 74.8765,
                "infra_link": "Delhi-Amritsar-Katra Expressway (under construction)",
                "nearest_airport": {
                    "name": "Sri Guru Ram Dass Jee International Airport",
                    "code": "ATQ",
                },
                "nearest_railway": {"name": "Amritsar Junction", "code": "ASR"},
            },
            {
                "name": "Virasat-e-Khalsa (Anandpur Sahib)",
                "type": "Modern Monumental Fortress Architecture",
                "highlight": "Acclaimed architectural monument by Moshe Safdie narrating 500 years of Sikh history.",
                "history": "Inaugurated in 2011 to celebrate 300 years of the founding of the Khalsa panth, the monument's dramatic sandstone-clad towers and petal-shaped stainless-steel roofs reflect against reflecting water terraces.",
                "built_century": "2011 CE",
                "badge": "Modern Architectural Marvel",
                "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1000&q=80",
                "latitude": 31.2345,
                "longitude": 76.498,
                "infra_link": "Chandigarh-Anandpur Sahib Highway",
                "nearest_airport": {
                    "name": "Shaheed Bhagat Singh International Airport Chandigarh",
                    "code": "IXC",
                },
                "nearest_railway": {"name": "Anandpur Sahib Station", "code": "ANSB"},
            },
        ],
        "natural_spots": [
            {
                "name": "Harike Wetland & Bird Sanctuary",
                "category": "Ramsar Freshwater Wetland",
                "highlight": "Confluence of Beas and Sutlej rivers, winter sanctuary for migratory aquatic birds from Siberia.",
                "history": "Created by the construction of Harike barrage in 1953, this Ramsar site supports rare Indus river dolphins and over 350 species of migratory birds.",
                "badge": "Ramsar Wetland Biosphere",
                "image_url": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1000&q=80",
                "latitude": 31.15,
                "longitude": 74.95,
                "infra_link": "NH-54 Amritsar-Bathinda Highway",
                "nearest_airport": {
                    "name": "Amritsar International Airport",
                    "code": "ATQ",
                },
                "nearest_railway": {"name": "Firozpur Cantt", "code": "FZR"},
            }
        ],
        "infra_connectivity": [
            "Delhi-Amritsar-Katra Greenfield Expressway.",
            "New Delhi - Amritsar Vande Bharat Express.",
            "Ludhiana & Amritsar Multi-Modal Logistics Parks.",
        ],
        "culture_and_cuisine": "Makki di Roti & Sarson da Saag, Amritsari Kulcha, Bhangra & Giddha dance, and Phulkari embroidery.",
        "best_time_to_visit": "October to March",
    },
    "Andhra Pradesh": {
        "tagline": "The Sunrise State (ఆంధ్రప్రదేశ్)",
        "greeting": "Namaskaram! (నమస్కారం)",
        "accent_color": "#D97706",
        "hero_image": "https://images.unsplash.com/photo-1621847468516-1ed5d0df56fe?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Tirumala Hills & Eastern Ghats Corridor",
        "architectural_marvels": [
            {
                "name": "Tirumala Venkateswara Temple",
                "type": "Ancient Dravidian Hill Temple",
                "highlight": "Ananda Nilayam gilded gold tower; most visited sacred pilgrimage temple in the world.",
                "history": "Presiding on the Venkatadri hill of the Seshachalam range, this sanctum has been patronized since the 3rd Century CE by the Pallavas, Cholas, and celebrated Emperor Krishnadevaraya of the Vijayanagara Empire who donated the golden temple kalasam.",
                "built_century": "Ancient Roots with 16th Century Vijayanagara Splendour",
                "badge": "World's Most Visited Shrine",
                "image_url": "https://images.unsplash.com/photo-1621847468516-1ed5d0df56fe?auto=format&fit=crop&w=1000&q=80",
                "latitude": 13.6833,
                "longitude": 79.35,
                "infra_link": "Bengaluru-Chennai Expressway (Chittoor section) & Vande Bharat",
                "nearest_airport": {"name": "Tirupati Airport", "code": "TIR"},
                "nearest_railway": {"name": "Tirupati Main", "code": "TPTY"},
            },
            {
                "name": "Lepakshi Veerabhadra Temple",
                "type": "Vijayanagara Stone Architecture",
                "highlight": "World-famous Hanging Pillar that does not touch the ground, and giant monolithic Nandi bull.",
                "history": "Built in the 16th Century by brothers Virupanna and Veeranna, governors under the Vijayanagara Empire, Lepakshi is renowned for its miraculous hanging stone pillar and vibrant ceiling frescoes depicting scenes from the Ramayana.",
                "built_century": "16th Century (1530 CE)",
                "badge": "Ancient Monolithic Wonder",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 13.8039,
                "longitude": 77.6083,
                "infra_link": "Bengaluru-Hyderabad NH-44 Corridor",
                "nearest_airport": {
                    "name": "Kempegowda International Airport Bengaluru",
                    "code": "BLR",
                },
                "nearest_railway": {"name": "Hindupur Railway Station", "code": "HUP"},
            },
        ],
        "natural_spots": [
            {
                "name": "Araku Valley & Borra Caves",
                "category": "Karst Limestone Cave Formations & Coffee Valleys",
                "highlight": "Million-year-old subterranean stalactite and stalagmite limestone caves in Eastern Ghats.",
                "history": "Deep within the Ananthagiri hills, the Borra Caves were formed by the Gosthani River cutting through Karst limestone, revered by indigenous tribes who discovered a naturally formed Shiva lingam deep in its caverns.",
                "badge": "Karst Geological Wonder",
                "image_url": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1000&q=80",
                "latitude": 18.2811,
                "longitude": 83.0397,
                "infra_link": "Visakhapatnam-Araku Vistadome Glass-Dome Train",
                "nearest_airport": {
                    "name": "Visakhapatnam International Airport",
                    "code": "VTZ",
                },
                "nearest_railway": {"name": "Araku Railway Station", "code": "ARK"},
            }
        ],
        "infra_connectivity": [
            "Bengaluru-Chennai Expressway (Phase-2 Chittoor Packages).",
            "Visakhapatnam-Secunderabad Vande Bharat Express.",
            "Bhogapuram International Airport & Krishnapatnam Port Expansion.",
        ],
        "culture_and_cuisine": "Hyderabadi/Andhra Pulihora, Gongura Pachadi, Kuchipudi classical dance, and Kalamkari hand-block painting.",
        "best_time_to_visit": "October to March",
    },
    "Telangana": {
        "tagline": "The Golden State (తెలంగాణ)",
        "greeting": "Namaskaram! (నమస్కారం)",
        "accent_color": "#9333EA",
        "hero_image": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Kakatiya Heritage & Qutb Shahi Citadel Trail",
        "architectural_marvels": [
            {
                "name": "Ramappa Temple (Palampet)",
                "type": "Kakatiya Stone Architecture",
                "highlight": "Built with ultra-lightweight floating bricks and carved black basalt bracket dancer pillars.",
                "history": "Constructed in 1213 CE during the reign of Kakatiya ruler Ganapati Deva by general Recharla Rudra. Marco Polo visited and called it 'the brightest star in the galaxy of medieval temples'. Its roof bricks are so porous that they float on water, reducing weight on earthquake-prone foundation soils.",
                "built_century": "13th Century (1213 CE)",
                "badge": "UNESCO World Heritage Kakatiya Wonder",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 18.2619,
                "longitude": 79.9431,
                "infra_link": "Hyderabad-Warangal Industrial Corridor",
                "nearest_airport": {
                    "name": "Rajiv Gandhi International Airport Hyderabad",
                    "code": "HYD",
                },
                "nearest_railway": {"name": "Warangal Railway Station", "code": "WL"},
            },
            {
                "name": "Golconda Fort & Acoustic Echo System",
                "type": "Qutb Shahi Citadel & Vault Architecture",
                "highlight": "Formidable diamond citadel with acoustic echo engineering carrying handclaps 1 km to top.",
                "history": "Originally a mud fort under the Kakatiyas in the 11th century, it was expanded by the Qutb Shahi sultans into an impregnable granite citadel. Famous for trading legendary diamonds including the Koh-i-Noor and Hope Diamond.",
                "built_century": "16th Century",
                "badge": "Historic Citadel & Diamond Fortress",
                "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1000&q=80",
                "latitude": 17.3833,
                "longitude": 78.4011,
                "infra_link": "Hyderabad Outer Ring Road (ORR)",
                "nearest_airport": {
                    "name": "Rajiv Gandhi International Airport",
                    "code": "HYD",
                },
                "nearest_railway": {"name": "Secunderabad Junction", "code": "SC"},
            },
        ],
        "natural_spots": [
            {
                "name": "Pakhal Lake & Wildlife Sanctuary",
                "category": "Historic Artificial Forest Lake",
                "highlight": "Man-made lake constructed in 1213 CE surrounded by deciduous teak jungle harboring leopards.",
                "history": "Engineered during the Kakatiya dynasty to harvest rainwater and sustain local agriculture, Pakhal Lake represents ancient Indian civil hydraulic mastery.",
                "badge": "Eco-Forest Lake Biosphere",
                "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "latitude": 17.9625,
                "longitude": 79.9833,
                "infra_link": "Warangal-Narsampet Highway",
                "nearest_airport": {
                    "name": "Rajiv Gandhi International Airport",
                    "code": "HYD",
                },
                "nearest_railway": {"name": "Warangal Railway Station", "code": "WL"},
            }
        ],
        "infra_connectivity": [
            "Hyderabad Regional Ring Road (RRR) & Metro Phase-2.",
            "Secunderabad - Tirupati Vande Bharat Express.",
            "Multi-Modal Logistics Park (MMLP) at Nagulapalli.",
        ],
        "culture_and_cuisine": "Hyderabadi Dum Biryani, Mirchi ka Salan, Bonalu festival, and Pochampally Ikat weave.",
        "best_time_to_visit": "October to March",
    },
    "Bihar": {
        "tagline": "The Cradle of Enlightenment (बिहार)",
        "greeting": "Pranam! (प्रणाम)",
        "accent_color": "#D97706",
        "hero_image": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Buddhist Heritage & Sacred Ganga Trail",
        "architectural_marvels": [
            {
                "name": "Mahabodhi Temple Complex (Bodh Gaya)",
                "type": "Ancient Brick Buddhist Architecture",
                "highlight": "50-meter grand brick pyramidal temple marking the sacred Bodhi Tree where Buddha achieved Enlightenment.",
                "history": "First temple built by Emperor Ashoka in the 3rd Century BCE around the sacred Bodhi Tree (Ficus religiosa). The current 50-meter pyramidal temple, rebuilt in brick during the Gupta and Pala periods, is one of the oldest brick structures surviving in eastern India.",
                "built_century": "3rd Century BCE to 5th-6th Century CE",
                "badge": "UNESCO World Heritage Site",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 24.696,
                "longitude": 84.9914,
                "infra_link": "Gaya International Airport & Grand Trunk Road (NH-19)",
                "nearest_airport": {
                    "name": "Gaya International Airport",
                    "code": "GAY",
                },
                "nearest_railway": {"name": "Gaya Junction", "code": "GAYA"},
            },
            {
                "name": "Nalanda Mahavihara Ancient University Ruins",
                "type": "Ancient Monastic University Architecture",
                "highlight": "Ancient residential university campus with stupas, chaityas, viharas, and water reservoirs.",
                "history": "Established in the 5th Century CE under Gupta rulers, Nalanda was the premier ancient university of the Buddhist world, educating over 10,000 scholars and monks from China, Korea, Japan, and Tibet including Xuanzang.",
                "built_century": "5th to 12th Century CE",
                "badge": "UNESCO World Heritage",
                "image_url": "https://images.unsplash.com/photo-1608958435020-e8a7109ba809?auto=format&fit=crop&w=1000&q=80",
                "latitude": 25.1367,
                "longitude": 85.445,
                "infra_link": "Patna-Bakhtiyarpur 4-Lane Highway",
                "nearest_airport": {
                    "name": "Jay Prakash Narayan International Airport Patna",
                    "code": "PAT",
                },
                "nearest_railway": {"name": "Nalanda / Rajgir Station", "code": "NLD"},
            },
        ],
        "natural_spots": [
            {
                "name": "Valmiki National Park & Tiger Reserve",
                "category": "Terai Foothill Himalayan Jungle",
                "highlight": "Lush sal forests along the Gandak river, home to Bengal tigers, rhinos, and flying foxes.",
                "history": "The only national park in Bihar, contiguous with Nepal's Chitwan National Park, preserving prehistoric foothill fauna and historic sites linked to Sage Valmiki.",
                "badge": "Terai Tiger Biosphere",
                "image_url": "https://images.unsplash.com/photo-1575550959106-5a7defe28b56?auto=format&fit=crop&w=1000&q=80",
                "latitude": 27.3333,
                "longitude": 84.1667,
                "infra_link": "Gorakhpur-Muzaffarpur Highway",
                "nearest_airport": {"name": "Gorakhpur Airport", "code": "GOP"},
                "nearest_railway": {"name": "Narkatiaganj Junction", "code": "NKE"},
            }
        ],
        "infra_connectivity": [
            "Namami Gange Riverfront & Digha-AIIMS Elevated Highway in Patna.",
            "Patna-Ranchi & Patna-Howrah Vande Bharat Express.",
            "Varanasi-Kolkata Greenfield Expressway (passing through Rohtas & Gaya).",
        ],
        "culture_and_cuisine": "Litti Chokha, Sattu, Madhubani (Mithila) folk paintings, Chhath Puja sacred rituals.",
        "best_time_to_visit": "October to March",
    },
    "Sikkim": {
        "tagline": "Small State, Giant Heart (सिक्किम)",
        "greeting": "Tashi Delek! (བཀྲ་ཤིས་བདེ་ལེགས)",
        "accent_color": "#0284C7",
        "hero_image": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Kanchenjunga Alpine & Silk Route Trail",
        "architectural_marvels": [
            {
                "name": "Rumtek Monastery (Dharma Chakra Centre)",
                "type": "Tibetan Kagyu Monastic Architecture",
                "highlight": "Seat of the Gyalwa Karmapa; exquisite golden stupas, intricate thankas, and mandala murals.",
                "history": "Originally built in the mid-18th Century and rebuilt in the 1960s by the 16th Karmapa, Rumtek is the largest monastery in Sikkim, showcasing traditional Tibetan Buddhist sacred woodwork and courtyard ritual mask dances.",
                "built_century": "18th Century / 1966 CE",
                "badge": "Tibetan Buddhist Dharma Centre",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 27.3025,
                "longitude": 88.5447,
                "infra_link": "Gangtok-Ranipool Highway & Pakyong Airport",
                "nearest_airport": {"name": "Pakyong Airport", "code": "PYG"},
                "nearest_railway": {"name": "New Jalpaiguri Junction", "code": "NJP"},
            }
        ],
        "natural_spots": [
            {
                "name": "Gurudongmar Sacred High-Altitude Lake",
                "category": "Glacial High-Altitude Sacred Lake (17,800 ft)",
                "highlight": "One of the highest lakes in the world, revered by Buddhists and Sikhs, surrounded by snow peaks.",
                "history": "Believed to have been blessed by Guru Padmasambhava and Guru Nanak Dev Ji, part of the lake never freezes even in deepest winter, providing fresh drinking water to local nomadic herders.",
                "badge": "High-Altitude Sacred Lake",
                "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "latitude": 28.0258,
                "longitude": 88.7097,
                "infra_link": "North Sikkim Highway (NH-310A)",
                "nearest_airport": {"name": "Pakyong Airport", "code": "PYG"},
                "nearest_railway": {"name": "New Jalpaiguri Junction", "code": "NJP"},
            }
        ],
        "infra_connectivity": [
            "Sivok-Rangpo Railway Project (linking Sikkim to India's broad gauge rail grid).",
            "Pakyong Greenfield Airport (PYG) under UDAN.",
            "Alternative Highway to Gangtok via Melli.",
        ],
        "culture_and_cuisine": "Momos, Thukpa, Gundruk, Cham masked ritual dances, Lepcha and Bhutia handlooms.",
        "best_time_to_visit": "March to May (Rhododendron blooms) and October to December",
    },
    "Meghalaya": {
        "tagline": "Abode of the Clouds (মেঘালয়)",
        "greeting": "Khublei! (খুবলৈ)",
        "accent_color": "#059669",
        "hero_image": "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?auto=format&fit=crop&w=1600&q=80",
        "scenic_route_name": "The Living Root Bridges & Cloud Canyon Way",
        "architectural_marvels": [
            {
                "name": "Nongriat Double Decker Living Root Bridge",
                "type": "Indigenous Bio-Engineering Architecture",
                "highlight": "Two tiers of living Ficus elastica aerial tree roots trained over centuries across raging river.",
                "history": "Pioneered over generations by indigenous Khasi and Jaintia tribes, living root bridges (Jingkieng Jri) are grown rather than built. Aerial roots of the rubber fig tree are channeled through hollowed betel nut trunks across torrential streams, growing stronger over centuries as the living tree matures.",
                "built_century": "Living Centuries-Old Bio-Engineering Heritage",
                "badge": "UNESCO Tentative World Heritage",
                "image_url": "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?auto=format&fit=crop&w=1000&q=80",
                "latitude": 25.2514,
                "longitude": 91.6706,
                "infra_link": "Shillong-Cherrapunji Scenic Mountain Highway",
                "nearest_airport": {"name": "Umroi Airport Shillong", "code": "SHL"},
                "nearest_railway": {"name": "Guwahati Railway Station", "code": "GHY"},
            }
        ],
        "natural_spots": [
            {
                "name": "Nohkalikai Falls (Cherrapunji)",
                "category": "Tallest Plunge Waterfall in India",
                "highlight": "340-metre single plunge waterfall cascading off dramatic red limestone cliff into emerald pool.",
                "history": "Located near Sohra (Cherrapunji)—one of the wettest places on earth—Nohkalikai is fed by constant rain clouds sweeping in from the Bay of Bengal over the Khasi hill escarpment.",
                "badge": "Highest Plunge Waterfall",
                "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "latitude": 25.2755,
                "longitude": 91.6853,
                "infra_link": "Sohra Scenic Circuit Highway",
                "nearest_airport": {"name": "Umroi Airport Shillong", "code": "SHL"},
                "nearest_railway": {"name": "Guwahati Railway Station", "code": "GHY"},
            },
            {
                "name": "Dawki Umngot Transparent River",
                "category": "Crystal Clear Emerald River Canyon",
                "highlight": "Pristine waters so clear that wooden country boats appear to float in mid-air.",
                "history": "Flowing through the Jaintia hills into the plains of Bangladesh, the Umngot River is kept spotless through strict indigenous village community conservation practices.",
                "badge": "Cleanest River in Asia",
                "image_url": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1000&q=80",
                "latitude": 25.1833,
                "longitude": 92.0167,
                "infra_link": "Dawki-Shillong National Highway (NH-206)",
                "nearest_airport": {"name": "Umroi Airport Shillong", "code": "SHL"},
                "nearest_railway": {"name": "Guwahati Railway Station", "code": "GHY"},
            },
        ],
        "infra_connectivity": [
            "Shillong-Dawki 4-Lane Highway with new Umngot cable-stayed bridge.",
            "Guwahati-Shillong 4-Lane Expressway (NH-6).",
            "Shillong Airport (Umroi) direct regional flights under UDAN.",
        ],
        "culture_and_cuisine": "Jadoh, Dohkhlieh, Khasi matrilineal society traditions, and bamboo musical instruments.",
        "best_time_to_visit": "October to April (Monsoon waterfalls at peak in June-September)",
    },
}

# 2. Curated 5 National Scenic Corridors with Geographic Waypoints ("Show the Way")
SCENIC_CORRIDORS = [
    {
        "id": "himalayan-skyway",
        "title": "The Himalayan Skyway & Arch Route",
        "region": "Jammu & Kashmir, Ladakh & Himachal Pradesh",
        "tagline": "Engineering Marvels Amongst the World's Highest Peaks",
        "distance": "580 km",
        "duration": "4-5 Days",
        "image_url": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1400&q=80",
        "description": "Cross the Chenab Rail Bridge—the world's highest arch railway bridge soaring 359m above the riverbed—and traverse all-weather high-altitude engineering through the Atal Tunnel and Zojila Pass.",
        "key_stops": [
            "Chenab Rail Bridge",
            "Zojila All-Weather Tunnel",
            "Atal Tunnel Rohtang",
            "Pangong Tso",
            "Hemis Monastery",
        ],
        "modern_infra": "USBRL Kashmir Rail Link, NH-1 All-Weather Tunneling, Vande Bharat Express",
        "route_coordinates": [
            [32.2396, 77.1887],
            [32.3619, 77.0375],
            [33.15, 75.14],
            [34.0837, 74.7973],
            [34.281, 75.485],
            [34.1526, 77.5771],
        ],
    },
    {
        "id": "konkan-skyrail",
        "title": "The Konkan Viaducts & Western Ghats Route",
        "region": "Maharashtra, Goa & Karnataka",
        "tagline": "Cascading Waterfalls, Basalt Sea Forts & Modern Sea Bridges",
        "distance": "650 km",
        "duration": "3-4 Days",
        "image_url": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1400&q=80",
        "description": "Drive across India's longest oceanic sea bridge (Atal Setu MTHL) and ride the Konkan Skyrail through misty Western Ghats, rock-cut UNESCO caves, and coastal Maratha fortresses.",
        "key_stops": [
            "Mumbai Trans Harbour Link (Atal Setu)",
            "Ajanta & Ellora Caves",
            "Dudhsagar Falls Rail View",
            "Sindhudurg Fort",
        ],
        "modern_infra": "Mumbai-Nagpur Samruddhi Mahamarg, Mumbai-Goa Vande Bharat Express, Konkan Railway Viaducts",
        "route_coordinates": [
            [18.96, 72.95],
            [18.75, 73.4],
            [17.65, 73.3],
            [15.5008, 73.9116],
            [15.3144, 74.3144],
            [14.8, 74.13],
        ],
    },
    {
        "id": "rajasthan-desert",
        "title": "The Royal Desert & Stepwell Corridor",
        "region": "Delhi (NCR), Haryana & Rajasthan",
        "tagline": "Ancient Hydraulic Architecture & Golden Sand Citadels",
        "distance": "720 km",
        "duration": "4 Days",
        "image_url": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1400&q=80",
        "description": "Cruise down the 8-lane Delhi-Mumbai Expressway into the Thar desert to explore geometric subterranean stepwells, amber-hued palace bastions, and tiger wilderness.",
        "key_stops": [
            "Chand Baori Stepwell (Abhaneri)",
            "Amber Fort & Jal Mahal",
            "Mehrangarh Fort Jodhpur",
            "Ranthambore Tiger Reserve",
        ],
        "modern_infra": "Delhi-Mumbai Greenfield Expressway (NE-4), Ajmer-Delhi Vande Bharat, Kishangarh UDAN Airport",
        "route_coordinates": [
            [28.6139, 77.209],
            [27.0072, 76.6064],
            [26.9124, 75.7873],
            [26.2978, 73.0185],
            [26.9157, 70.9083],
        ],
    },
    {
        "id": "chola-coastal",
        "title": "The Chola Temples & Ocean Bridge Odyssey",
        "region": "Tamil Nadu & Kerala",
        "tagline": "Granite Monoliths, Ocean Rail Bridges & Emerald Backwaters",
        "distance": "620 km",
        "duration": "5 Days",
        "image_url": "https://images.unsplash.com/photo-1621847468516-1ed5d0df56fe?auto=format&fit=crop&w=1400&q=80",
        "description": "Witness the 1,000-year-old living Chola granite temples, cross the sea on the new Pamban Vertical-Lift Railway Bridge, and cruise the tranquil inland waterways of Kerala.",
        "key_stops": [
            "Brihadisvara Great Chola Temple",
            "New Pamban Sea Bridge (Rameswaram)",
            "Meenakshi Amman Temple",
            "Alleppey Backwaters",
        ],
        "modern_infra": "Bengaluru-Chennai Expressway (NE-5), Kochi Water Metro, Chennai-Mysuru Vande Bharat",
        "route_coordinates": [
            [13.0827, 80.2707],
            [10.7828, 79.1318],
            [9.9195, 78.1193],
            [9.2876, 79.3129],
            [9.4981, 76.3388],
        ],
    },
    {
        "id": "brahmaputra-living-bridges",
        "title": "The Brahmaputra & Living Bio-Bridge Trail",
        "region": "Assam & Meghalaya",
        "tagline": "Indigenous Bio-Engineering & Sacred River Sanctuaries",
        "distance": "480 km",
        "duration": "4-5 Days",
        "image_url": "https://images.unsplash.com/photo-1597848212624-a19eb35e2651?auto=format&fit=crop&w=1400&q=80",
        "description": "Journey through the wettest subtropical rainforests on Earth across living Ficus root bridges, explore the world's largest river island, and spot one-horned rhinos in the wild.",
        "key_stops": [
            "Nongriat Double Decker Living Root Bridge",
            "Kaziranga National Park",
            "Bogibeel Rail-Road Bridge",
            "Majuli River Island",
        ],
        "modern_infra": "National Waterway 2 (NW-2) River Cruise, Bogibeel Bridge over Brahmaputra, Guwahati-NJP Vande Bharat",
        "route_coordinates": [
            [26.1664, 91.7054],
            [25.5788, 91.8933],
            [25.2514, 91.6706],
            [26.5775, 93.1711],
            [27.4, 94.9],
        ],
    },
]

# 3. Generate RAW_PROJECTS with infra_image_url and district_part
SECTOR_IMAGES = {
    "Roads & Expressways": "https://images.unsplash.com/photo-1545459720-aac8509eb02c?auto=format&fit=crop&w=1000&q=80",
    "Heavy Freight Rail": "https://images.unsplash.com/photo-1474487548417-781cb71495f3?auto=format&fit=crop&w=1000&q=80",
    "High-Speed Mass Transit": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80",
    "Strategic Mountain Tunnel": "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80",
    "Greenfield Deep Port & Sagarmala": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1000&q=80",
    "River Flood Mitigation & Drainage": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1000&q=80",
    "Urban Mass Transit": "https://images.unsplash.com/photo-1517649763962-0c623266ddc0?auto=format&fit=crop&w=1000&q=80",
    "Multi-Modal Logistics Park": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1000&q=80",
    "Inland Waterways & Terminals": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=1000&q=80",
    "Coastal Defense & Sea Dikes": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1000&q=80",
}


def get_project_part(p):
    name = p["projectName"]
    dist = p["district"]
    if "Package" in name:
        parts = [
            part.strip().rstrip(")")
            for part in name.split("(")
            if "Package" in part or "Section" in part
        ]
        if parts:
            return f"{dist} | {parts[0]}"
    if "Zojila" in name:
        return f"{dist} | Western Portal Mountain Bypass Reach"
    if "Bullet Train" in name or "High-Speed" in name:
        return f"{dist} | Elevated Viaduct & Pier Alignment (C4 Package)"
    if "Freight" in name:
        return f"{dist} | Heavy-Haul Track & Yard Alignment"
    if "Expressway" in name:
        return f"{dist} | Greenfield Expressway Section"
    if "Tunnel" in name:
        return f"{dist} | Twin-Tube Hill Tunneling Portal"
    if "Metro" in name:
        return f"{dist} | Elevated Metro Rail Viaduct Reach"
    if "Port" in name:
        return f"{dist} | Deep-Water Wharf & Breakwater Berth"
    if "Flood" in name or "Barrage" in name:
        return f"{dist} | River Embankment & Flood Defense Spur"
    return f"{dist} | Central Infrastructure Corridor"


projects = api.generate_nhai_projects(total_projects=265)
for p in projects:
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

    # Add infra image and district part
    p["infra_image_url"] = SECTOR_IMAGES.get(
        p["sector"],
        "https://images.unsplash.com/photo-1545459720-aac8509eb02c?auto=format&fit=crop&w=1000&q=80",
    )
    p["district_part"] = get_project_part(p)

# Specific landmark overrides for famous state projects
for p in projects:
    if "Zojila" in p["projectName"]:
        p["infra_image_url"] = (
            "https://images.unsplash.com/photo-1513836279014-a89f7a76ae86?auto=format&fit=crop&w=1000&q=80"
        )
    elif "Bullet Train" in p["projectName"]:
        p["infra_image_url"] = (
            "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1000&q=80"
        )
    elif "Vadhavan" in p["projectName"]:
        p["infra_image_url"] = (
            "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1000&q=80"
        )
    elif "Freight" in p["projectName"]:
        p["infra_image_url"] = (
            "https://images.unsplash.com/photo-1474487548417-781cb71495f3?auto=format&fit=crop&w=1000&q=80"
        )

# 4. Write to dashboard/data.js
data_js_content = f"""// PragatiGati: Live Golden Datasets with Infrastructure Imagery & Travel Booking
const RAW_PROJECTS = {json.dumps(projects, indent=2)};

const STATE_TOURISM = {json.dumps(STATE_TOURISM, indent=2)};

const SCENIC_CORRIDORS = {json.dumps(SCENIC_CORRIDORS, indent=2)};
"""

with open("dashboard/data.js", "w", encoding="utf-8") as f:
    f.write(data_js_content)
print("Updated dashboard/data.js successfully.")

# 5. Write to src/tourism_data.py
src_tourism_content = f'''"""Comprehensive Indian Tourism, Architectural Heritage, and Natural Spot Knowledge Base.

Aligned with the Government of India's 'Dekho Apna Desh' and 'Vikas Bhi, Virasat Bhi'
initiatives, styled after world-class tourism portals like Visit Norway's National Scenic Routes,
blending historic architecture and natural wonders with modern transport corridors and
travel booking integrations.
"""

from typing import Any

SCENIC_CORRIDORS: list[dict[str, Any]] = {json.dumps(SCENIC_CORRIDORS, indent=4)}

STATE_TOURISM_DATA: dict[str, dict[str, Any]] = {json.dumps(STATE_TOURISM, indent=4)}


def get_state_tourism(state_name: str) -> dict[str, Any]:
    """Retrieve tourism, architectural, and natural spot data for a given Indian State."""
    if state_name in STATE_TOURISM_DATA:
        return STATE_TOURISM_DATA[state_name]

    # Generic fallback with high-res imagery for any other state
    return {{
        "tagline": f"Explore {{state_name}} - Incredible India",
        "greeting": "Namaste! (नमस्ते)",
        "accent_color": "#FF9933",
        "hero_image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1400&q=80",
        "scenic_route_name": f"The Scenic Heritage Route of {{state_name}}",
        "architectural_marvels": [
            {{
                "name": f"Historic Monuments of {{state_name}}",
                "type": "Regional Architectural Heritage",
                "highlight": f"Centuries-old stone temples, stepwells, and forts of {{state_name}}.",
                "history": f"Protected cultural monuments showcasing centuries of architectural craft, sculpture, and civil engineering in {{state_name}}.",
                "built_century": "Ancient & Medieval",
                "badge": "Heritage Landmark",
                "image_url": "https://images.unsplash.com/photo-1600100397608-f010f447a464?auto=format&fit=crop&w=1000&q=80",
                "latitude": 20.5937,
                "longitude": 78.9629,
                "infra_link": "National Highway Corridors & Vande Bharat Rail",
                "nearest_airport": {{"name": f"{{state_name}} Regional Airport", "code": "DEL"}},
                "nearest_railway": {{"name": f"{{state_name}} Central Station", "code": "NDLS"}},
            }}
        ],
        "natural_spots": [
            {{
                "name": f"Protected Forests & Sanctuaries of {{state_name}}",
                "category": "Wildlife & Natural Ecosystem",
                "highlight": "Lush biodiversity, rivers, flora and fauna under ecological protection.",
                "history": f"Ecological biosphere preserving endemic flora, forest streams, and wildlife in {{state_name}}.",
                "badge": "Eco Sanctuaries",
                "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
                "latitude": 20.5937,
                "longitude": 78.9629,
                "infra_link": "Bharatmala Scenic Roadways",
                "nearest_airport": {{"name": f"{{state_name}} Regional Airport", "code": "DEL"}},
                "nearest_railway": {{"name": f"{{state_name}} Central Station", "code": "NDLS"}},
            }}
        ],
        "infra_connectivity": [
            f"National Highway corridors and Vande Bharat connectivity in {{state_name}}.",
            "PM Gati Shakti multi-modal logistics alignment.",
        ],
        "culture_and_cuisine": f"Traditional folklore, handicrafts, and regional culinary delicacies of {{state_name}}.",
        "best_time_to_visit": "October to March",
    }}
'''

with open("src/tourism_data.py", "w", encoding="utf-8") as f:
    f.write(src_tourism_content)
print("Updated src/tourism_data.py successfully.")
