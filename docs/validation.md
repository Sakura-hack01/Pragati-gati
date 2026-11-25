# Data Quality & Validation Rules (PragatiGati)

Automated data quality checks run across all Bronze and Silver tables, persisting audit results in `04-validation`.`dq_results`.

## Audit Actions

- **stop**: Fatal data integrity violation (e.g., null primary key, non-unique contract ID, negative budget). Halts downstream pipeline execution immediately.
- **flag**: Data quality anomaly or edge-case (e.g., coordinate outside India bounding box, clearance gate pending, front-loading disparity >15%). Logged for review and Silver transformation handling.

## Core Table Audits

### 1. `nhai_morth_projects`

| Column | Rule | Action | Rationale |
| --- | --- | --- | --- |
| `contractId` | Not Null & Unique | `stop` | Unique contract identifier across MoRTH/NHAI. |
| `budgetInCrores` | Positive Value | `flag` | Budgets must be greater than zero. |
| `amountPaidInCrores` | <= Budget | `flag` | Disbursements cannot exceed allocated contract outlay. |
| `latitude, longitude` | Inside India Box (Lat 6.5–37.5, Lon 68.0–97.5) | `flag` | Excludes miskeyed or overseas coordinates. |
| `pariveshClearanceStatus` | Valid Clearance Gate | `flag` | Ensures known PARIVESH milestone values. |

### 2. `flood_control_projects`

| Column | Rule | Action | Rationale |
| --- | --- | --- | --- |
| `attributes.ObjectId` | Not Null & Unique | `stop` | Feature identifier for GIS layer. |
| `attributes.ContractID` | Not Null | `stop` | Traceable contract identification. |
| `attributes.ContractCostCrores` | Positive Value | `flag` | Flood defense assets must have positive costs. |

### 3. `lgd_geography` & `census_population`

| Column | Rule | Action | Rationale |
| --- | --- | --- | --- |
| `lgd_district_code` | Not Null & Unique | `stop` | Official LGD administrative primary key. |
| `population_projected_2024` | Strictly Positive | `stop` | Baseline population required for per-capita spend calculations. |
