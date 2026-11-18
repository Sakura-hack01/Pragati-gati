# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze: NHAI & MoRTH National Highways & Bharatmala Projects
# MAGIC
# MAGIC Loads Indian highway infrastructure projects from the MoRTH/NHAI open API feed into
# MAGIC `01-bronze`.`nhai_morth_projects`. One row is one project package with original field names.
# MAGIC The primary business key is `contractId`.
# MAGIC
# MAGIC 1. Saves each API page as received in a timestamped landing folder under `landing/nhai_projects/<run_id>`.
# MAGIC 2. Reads the files into Spark DataFrame, retaining raw field schemas, adding provenance metadata:
# MAGIC    `_raw_file`, `_source_url`, and `_ingest_run_id`.
# MAGIC 3. Appends an audit log entry in `01-bronze`.`load_log` with row counts and SHA-256 fingerprints.

# COMMAND ----------

import os
import sys

from pyspark.sql import functions as F

repo_root = os.path.abspath("../..")  # the repo root, so the import below works everywhere
sys.path.insert(0, repo_root)

from src import api, bronze, config

# COMMAND ----------

# 1. Ingest every API page and save raw JSON payloads
load_run_id = bronze.new_run_id()
folder = bronze.landing_folder("nhai_projects", load_run_id)
raw_files = []

for page, reply, _, total in api.nhai_pages(page_size=config.NHAI_PAGE_SIZE):
    raw_files.append(bronze.save_raw(f"{folder}/page_{page:03d}.json", reply))

print(f"Saved {len(raw_files)} pages to {folder}. Total projects reported: {total:,}.")

# COMMAND ----------

# 2. Read raw pages with Spark schema preservation
page_files = [path for path, _, _ in raw_files]
projects = (
    spark.read.option("multiLine", "true")
    .json(page_files)
    .select(F.explode("data.projects").alias("project"), F.col("_metadata.file_path").alias("_raw_file"))
    .select("project.*", "_raw_file")
    .withColumn("_source_url", F.lit(config.NHAI_API))
)

# COMMAND ----------

# 3. Save to Bronze Delta Table and log audit metadata
loaded = bronze.save_table(spark, projects, "nhai_morth_projects", load_run_id)
bronze.log_load(spark, load_run_id, "NHAI/MoRTH Projects API", "nhai_morth_projects", total, loaded, raw_files, config.NHAI_API)
print(f"Successfully loaded {loaded:,} of {total:,} projects into `01-bronze`.nhai_morth_projects.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Quick Ingestion Summary (Values in ₹ Crores)

# COMMAND ----------

display(spark.sql("""
    SELECT 
        status, 
        COUNT(*) AS project_count, 
        ROUND(SUM(TRY_CAST(budgetInCrores AS DECIMAL(18, 2))), 2) AS total_budget_crores,
        ROUND(SUM(TRY_CAST(amountPaidInCrores AS DECIMAL(18, 2))), 2) AS total_disbursed_crores
    FROM `pragatigati-capstone`.`01-bronze`.nhai_morth_projects
    GROUP BY status
    ORDER BY project_count DESC
"""))
