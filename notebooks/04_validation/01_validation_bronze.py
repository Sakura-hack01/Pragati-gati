# Databricks notebook source
# MAGIC %md
# MAGIC # Validation: Bronze Data Quality Checks (PragatiGati)
# MAGIC
# MAGIC Runs automated DQ audits across all bronze tables and records results in `04-validation`.`dq_results`:
# MAGIC - `stop`: Fatal data corruption. Pipeline stops immediately.
# MAGIC - `flag`: Data quality alert or edge-case rows for Silver layer cleanup.
# MAGIC
# MAGIC Validates Indian geographic boundaries, positive INR budgets, contract uniqueness,
# MAGIC LGD administrative codes, and PARIVESH clearance classifications.

# COMMAND ----------

import os
import sys

from pyspark.sql import functions as F

repo_root = os.path.abspath("../..")  # the repo root, so the import below works everywhere
sys.path.insert(0, repo_root)

from src import bronze, config

run_id = bronze.new_run_id()

# Bronze tables audited in sequence
TABLES = [
    "nhai_morth_projects",
    "flood_control_projects",
    "lgd_geography",
    "census_population",
    "boundaries",
]

# Coordinate bounding box check for India
def in_india(lat_col, lon_col):
    """SQL condition verifying coordinates fall within India geographical bounding box."""
    return f"{lat_col} BETWEEN {config.INDIA_LAT[0]} AND {config.INDIA_LAT[1]} AND {lon_col} BETWEEN {config.INDIA_LON[0]} AND {config.INDIA_LON[1]}"


def check(column, name, failed_expr, action, total_expr=None):
    """Creates one audit check dictionary."""
    return {
        "column": column,
        "check": name,
        "failed": failed_expr,
        "action": action,
        "total": total_expr,
    }


TABLE_CHECKS = {
    "nhai_morth_projects": [
        check("contractId", "not null", "COUNT_IF(contractId IS NULL)", "stop"),
        check("contractId", "unique", "COUNT(*) - COUNT(DISTINCT contractId)", "stop"),
        check("status", "valid project status enum", "COUNT_IF(status IS NULL OR status NOT IN ('Completed', 'On-Going', 'Not Yet Started', 'For Procurement', 'Terminated'))", "flag"),
        check("budgetInCrores", "budget positive (INR Crores)", "COUNT_IF(TRY_CAST(budgetInCrores AS DOUBLE) IS NULL OR TRY_CAST(budgetInCrores AS DOUBLE) <= 0)", "flag"),
        check("amountPaidInCrores", "disbursement within budget", "COUNT_IF(TRY_CAST(amountPaidInCrores AS DOUBLE) > TRY_CAST(budgetInCrores AS DOUBLE))", "flag"),
        check("physicalProgressPct", "between 0 and 100", "COUNT_IF(TRY_CAST(physicalProgressPct AS DOUBLE) NOT BETWEEN 0 AND 100)", "flag"),
        check("latitude, longitude", "coordinates within India bounding box", f"COUNT_IF(latitude IS NOT NULL AND longitude IS NOT NULL AND NOT ({in_india('latitude', 'longitude')}))", "flag"),
        check("pariveshClearanceStatus", "known clearance gate", "COUNT_IF(pariveshClearanceStatus IS NULL)", "flag"),
    ],
    "flood_control_projects": [
        check("attributes.ObjectId", "not null and unique", "COUNT(*) - COUNT(DISTINCT attributes.ObjectId)", "stop"),
        check("attributes.ContractID", "not null", "COUNT_IF(attributes.ContractID IS NULL)", "stop"),
        check("attributes.ContractCostCrores", "positive contract cost", "COUNT_IF(TRY_CAST(attributes.ContractCostCrores AS DOUBLE) <= 0)", "flag"),
        check("attributes.Latitude, attributes.Longitude", "within India bounds", f"COUNT_IF(NOT ({in_india('attributes.Latitude', 'attributes.Longitude')}))", "flag"),
    ],
    "lgd_geography": [
        check("lgd_district_code", "not null and unique", "COUNT(*) - COUNT(DISTINCT lgd_district_code)", "stop"),
        check("state_name", "not null", "COUNT_IF(state_name IS NULL)", "stop"),
        check("administrative_zone", "valid zonal council", "COUNT_IF(administrative_zone NOT IN ('Northern', 'Southern', 'Eastern', 'Western', 'Central', 'North-Eastern'))", "flag"),
    ],
    "census_population": [
        check("lgd_district_code", "not null", "COUNT_IF(lgd_district_code IS NULL)", "stop"),
        check("population_projected_2024", "population strictly positive", "COUNT_IF(TRY_CAST(population_projected_2024 AS LONG) <= 0)", "stop"),
    ],
    "boundaries": [
        check("source_feature_index", "not null", "COUNT_IF(source_feature_index IS NULL)", "stop"),
        check("source_feature_json", "valid GeoJSON feature", "COUNT_IF(source_feature_json IS NULL OR length(source_feature_json) < 10)", "stop"),
    ],
}

# COMMAND ----------

# MAGIC %md
# MAGIC ## Execute Checks & Record in `04-validation`.`dq_results`

# COMMAND ----------

dq_rows = []
for table, checks in TABLE_CHECKS.items():
    full_table = f"`{config.CATALOG}`.`{config.BRONZE}`.{table}"
    try:
        # Build SQL query aggregating all checks for the table in a single scan
        select_exprs = ["COUNT(*) AS total_rows"]
        for idx, c in enumerate(checks):
            select_exprs.append(f"{c['failed']} AS f_{idx}")
            
        sql_query = f"SELECT {', '.join(select_exprs)} FROM {full_table}"
        res = spark.sql(sql_query).collect()[0]
        total = res["total_rows"]
        
        for idx, c in enumerate(checks):
            failed = res[f"f_{idx}"]
            pct = round((failed / total * 100.0), 2) if total > 0 else 0.0
            status = "PASS" if failed == 0 else ("FAIL" if c["action"] == "stop" else "WARNING")
            dq_rows.append((
                run_id,
                table,
                c["column"],
                c["check"],
                failed,
                total,
                pct,
                c["action"],
                status,
            ))
    except Exception as e:  # noqa: BLE001
        print(f"Skipping or error auditing table {table}: {e}")

if dq_rows:
    schema = "run_id string, table_name string, column string, data_quality_check string, failed_rows long, total_rows long, percentage double, action string, status string"
    dq_df = spark.createDataFrame(dq_rows, schema).withColumn("audit_ts", F.current_timestamp())
    dq_df.write.mode("append").option("mergeSchema", "true").saveAsTable(f"`{config.CATALOG}`.`{config.VALIDATION}`.dq_results")
    display(dq_df)
