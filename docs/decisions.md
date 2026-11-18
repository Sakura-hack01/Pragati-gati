# Architectural & Design Decisions

Each significant design choice is logged with an identifier, date, rationale, and consequences.

## Log

| ID | Date | Decision | Rationale |
| --- | --- | --- | --- |
| D-01 | Oct 01 | Adopt India National Infrastructure Pipeline & PM Gati Shakti as focal scope | India's massive infrastructure capex (Bharatmala, Sagarmala, DFC, Bullet Train) offers a richer, high-impact landscape for data engineering and governance. |
| D-02 | Oct 01 | Medallion Lakehouse on Databricks with catalog `pragatigati-capstone` | Cleanly isolates raw, cleaned, dimensional, and audit tables across numbered schemas. |
| D-03 | Oct 02 | Establish Local Government Directory (LGD) as geographic master | LGD (Ministry of Panchayati Raj) is the official Digital India coding standard for States, UTs, and Districts, preventing ambiguous spelling joins. |
| D-04 | Oct 02 | Currency standardization to Indian Rupee (INR / ₹ Crores) | Indian public works capex is officially budgeted and reported in ₹ Crores (1 Crore = 10 Million INR). |
| D-05 | Oct 03 | **Novelty 1: PM Gati Shakti 7 Engines Multi-Modal Classification** | Infrastructure projects must not be monitored in silos; aligning projects to the 7 Gati Shakti pillars enables inter-modal gap detection. |
| D-06 | Oct 03 | **Novelty 2: PARIVESH 2.0 Statutory Clearance Bottleneck Engine** | In India, over 60% of infrastructure delays occur at regulatory gates (Forest Stage I/II, Wildlife, Land Sec 19). Tracking "Trapped Capex" quantifies blocked economic value. |
| D-07 | Oct 03 | **Novelty 3: IMD Monsoon Impact & Seasonal Disruption Risk Score** | Peak monsoon (Jun-Sep) causes severe construction moratoriums. Cross-referencing IMD hazard zones with project schedules predicts weather-induced delays. |
| D-08 | Oct 04 | **Novelty 4: NITI Aayog Aspirational Districts Capex Equity Metric** | Computes Per-Capita Capex (₹/person) and infrastructure deficit to ensure equitable national development across the 112 priority districts. |
| D-09 | Oct 04 | **Novelty 5: Financial vs Physical "Ghost Progress" Disparity Detector** | Compares % Financial Disbursed against % Physical Progress to expose front-loading anomalies and cash diversion risks. |
| D-10 | Oct 05 | Provide both Databricks Lakehouse SQL models and Interactive Web Dashboard | Delivers instant local visualization via Leaflet GIS and Chart.js while maintaining full compatibility with Databricks SQL & Genie. |
