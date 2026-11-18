# PragatiGati Data Model

All tables reside in our Databricks Lakehouse catalog: `pragatigati-capstone`. Schemas are partitioned across Medallion layers in run order.

| Table | Grain (One row represents) | Primary Key |
| --- | --- | --- |
| `01-bronze.nhai_morth_projects` | One highway/expressway contract package as ingested | `contractId` |
| `01-bronze.flood_control_projects` | One flood mitigation or embankment structure | `attributes.ObjectId` |
| `01-bronze.lgd_geography` | One administrative district/state from LGD | `lgd_district_code` |
| `01-bronze.census_population` | One district demographic projection and Aspirational District indicator | `lgd_district_code` |
| `01-bronze.boundaries` | One GIS boundary feature (State/UT/Corridor) as GeoJSON text | `source_file`, `source_feature_index` |
| `01-bronze.load_log` | Ingestion telemetry, row count reconciliation, and SHA-256 digests | `run_id`, `table_name` |
| `02-silver.places` | Cleaned administrative places with LGD codes and Census populations | `lgd_district_code` |
| `02-silver.projects` | Harmonized infrastructure projects with standardized ₹ INR Crores and LGD links | `contract_id` |
| `03-gold.dim_place` | Master dimension for administrative zones, states, districts, and populations | `lgd_district_code` |
| `03-gold.dim_gatishakti_engine` | Master dimension for the 7 Gati Shakti pillars (Roads, Rail, Ports, etc.) | `engine_name` |
| `03-gold.dim_agency` | Executing authority dimension (NHAI, DFCCIL, NHSRCL, Jal Shakti, MoPSW) | `agency_name` |
| `03-gold.dim_contractor` | Contractor dimension with concession model details and delay records | `contractor_name` |
| `03-gold.fact_project` | Central fact table containing Capex, disbursements, progress %, disparity, and trapped capex | `contract_id` |
| `03-gold.agg_state_equity` | Aggregated state-level Capex per capita (₹/person) and clearance bottlenecks | `state_name` |
| `03-gold.agg_gatishakti_summary` | Summary table tracking budget distribution across Gati Shakti pillars | `engine_name` |
| `04-validation.dq_results` | Automated data quality audit results and stop/flag rule statuses | `run_id`, `table_name`, `column`, `data_quality_check` |

## Column Naming Standards

- **Bronze**: Preserves source field naming verbatim (e.g. `contractId`, `budgetInCrores`, `pariveshClearanceStatus`).
- **Silver & Gold**: Follows strict `snake_case` naming (e.g. `contract_id`, `budget_crores`, `physical_progress_pct`, `progress_disparity_pct`).
- **Audit Columns**: Every table retains `_ingest_run_id` and `load_ts` for complete data lineage.
