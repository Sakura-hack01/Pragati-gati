# PragatiGati Lakehouse Notebooks

Our Databricks notebooks, organized by medallion layer. Run the folders in this order. Each folder writes to the corresponding schema in `pragatigati-capstone`.

| Order | Folder | Writes to | Description |
| --- | --- | --- | --- |
| 0 | `00_setup` | `00-source` | Creates the catalog, schemas, landing volume, and validates connectivity |
| 1 | `01_bronze` | `01-bronze` | Ingests high-fidelity raw data with timestamps and SHA-256 hashes |
| 2 | `02_silver` | `02-silver` | Cleans data, standardizes ₹ INR amounts, adds official LGD codes, parses dates |
| 3 | `03_gold` | `03-gold` | Builds Star Schema (facts & dimensions) and PM Gati Shakti analytical aggregates |
| 4 | `04_validation` | `04-validation` | Runs automated DQ audits and logs results in `dq_results` |

## Bronze Ingestion Notebooks

| Notebook | Source | Tables Created |
| --- | --- | --- |
| `01_bronze_nhai_morth_projects` | MoRTH & NHAI Open API / Bharatmala | `nhai_morth_projects` |
| `02_bronze_flood_control` | Ministry of Jal Shakti / FMBAP / Namami Gange | `flood_control_projects` |
| `03_bronze_lgd_geography` | Local Government Directory (LGD) | `lgd_geography` |
| `05_bronze_boundaries` | Bharatmaps / Survey of India GeoJSON | `boundaries` |
| `06_bronze_census_table_c` | MoSPI Census & Aspirational District Index | `census_population` |

The data quality checks run in `04_validation/01_validation_bronze.py`.
