# Databricks notebook source
# MAGIC %md
# MAGIC # Run PragatiGati Pipeline End-to-End
# MAGIC
# MAGIC Orchestrates the entire Medallion Architecture:
# MAGIC 1. Setup Catalog and Schemas
# MAGIC 2. Ingest Bronze Layers:
# MAGIC    - NHAI/MoRTH Highways & Bharatmala
# MAGIC    - Jal Shakti Flood Control & Embankments
# MAGIC    - LGD Administrative Master Directory
# MAGIC    - India GIS Boundaries
# MAGIC    - Census & MoSPI District Demographics
# MAGIC 3. Silver & Gold Transformations
# MAGIC 4. Automated Data Quality Audits

# COMMAND ----------

setup_step = "00_setup/00_setup_workspace"
required_loads = [
    "01_bronze/01_bronze_nhai_morth_projects",
    "01_bronze/02_bronze_flood_control",
    "01_bronze/03_bronze_lgd_geography",
    "01_bronze/05_bronze_boundaries",
    "01_bronze/06_bronze_census_table_c",
]
validation_step = "04_validation/01_validation_bronze"


def run_step(step):
    """Run one notebook workflow. Return 'done', SKIPPED, or FAILED."""
    try:
        return dbutils.notebook.run(f"./{step}", 3600) or "done"
    except Exception as error:  # noqa: BLE001 keep going to capture all step outputs
        return "FAILED: " + str(error).strip().splitlines()[0][:300]


results = []
setup_result = run_step(setup_step)
results.append((setup_step, setup_result))
if setup_result.startswith(("FAILED", "SKIPPED")):
    display(spark.createDataFrame(results, "step string, result string"))
    raise RuntimeError(f"Setup step failed: {setup_result}")

for step in required_loads:
    result = run_step(step)
    results.append((step, result))
    print(f"{step}: {result}")

blocked = [step for step, result in results if step in required_loads and result.startswith(("FAILED", "SKIPPED"))]
if blocked:
    results.append((validation_step, "BLOCKED: required bronze load did not finish: " + ", ".join(blocked)))
else:
    results.append((validation_step, run_step(validation_step)))

# COMMAND ----------

display(spark.createDataFrame(results, "step string, result string"))
failed = [step for step, result in results if result.startswith(("FAILED", "BLOCKED"))]
if failed:
    raise RuntimeError("Pipeline failed on steps: " + ", ".join(failed))
