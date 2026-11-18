# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze: Jal Shakti & Flood Control Projects (FMBAP / Namami Gange)
# MAGIC
# MAGIC Loads river flood mitigation and embankment assets from the Ministry of Jal Shakti
# MAGIC / Flood Management and Border Areas Programme (FMBAP) into `01-bronze`.`flood_control_projects`.
# MAGIC
# MAGIC One row represents one flood defense feature, retaining original GIS geometries and attributes.
# MAGIC The key is `attributes.ObjectId`.

# COMMAND ----------

import os
import sys

from pyspark.sql import functions as F

repo_root = os.path.abspath("../..")  # the repo root, so the import below works everywhere
sys.path.insert(0, repo_root)

from src import api, bronze, config

# COMMAND ----------

# 1. Ingest flood mitigation layer features and save raw replies
load_run_id = bronze.new_run_id()
folder = bronze.landing_folder("flood_control", load_run_id)
raw_files = []

for page, reply, _, total in api.flood_control_pages(page_size=config.JAL_SHAKTI_PAGE_SIZE):
    raw_files.append(bronze.save_raw(f"{folder}/page_{page:03d}.json", reply))

print(f"Saved {len(raw_files)} pages to {folder}. Total flood assets reported: {total:,}.")

# COMMAND ----------

# 2. Parse feature attributes and GIS coordinates
page_files = [path for path, _, _ in raw_files]
flood = (
    spark.read.option("multiLine", "true")
    .json(page_files)
    .select(
        F.explode("features").alias("feature"),
        "spatialReference",
        F.col("_metadata.file_path").alias("_raw_file"),
    )
    .select("feature.*", "spatialReference", "_raw_file")
    .withColumn("_source_url", F.lit(config.JAL_SHAKTI_LAYER))
)

# COMMAND ----------

# 3. Save to Bronze Delta Table and log provenance
loaded = bronze.save_table(spark, flood, "flood_control_projects", load_run_id)
bronze.log_load(spark, load_run_id, "Jal Shakti Flood Control Layer", "flood_control_projects", total, loaded, raw_files, config.JAL_SHAKTI_LAYER)
print(f"Successfully loaded {loaded:,} of {total:,} flood control assets.")
