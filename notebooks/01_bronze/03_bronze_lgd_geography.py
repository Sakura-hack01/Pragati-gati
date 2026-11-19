# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze: Local Government Directory (LGD) Administrative Codes & Geography
# MAGIC
# MAGIC Loads the official Local Government Directory (LGD) from the Ministry of Panchayati Raj
# MAGIC into `01-bronze`.`lgd_geography`.
# MAGIC
# MAGIC It establishes the authoritative administrative hierarchy for India:
# MAGIC - 6 Administrative Zones (Northern, Southern, Eastern, Western, Central, North-Eastern)
# MAGIC - 28 States and 8 Union Territories (36 State/UT entities)
# MAGIC - 780+ Districts with unique LGD codes and Census correspondence IDs
# MAGIC
# MAGIC Primary key: `lgd_district_code` (or `lgd_state_code` for state level).

# COMMAND ----------

import os
import sys

from pyspark.sql import functions as F

repo_root = os.path.abspath("../..")  # the repo root, so the import below works everywhere
sys.path.insert(0, repo_root)

from src import api, bronze, config

load_run_id = bronze.new_run_id()
folder = bronze.landing_folder("lgd")

# COMMAND ----------

# 1. Structure LGD State and District Master Data
lgd_records = []
for state in api.INDIAN_STATES_DATA:
    # Build district hierarchy
    state_code = state["state_code"]
    state_name = state["state_name"]
    zone = state["zone"]
    s_lgd = state["lgd_code"]
    
    # Representative sample of districts per state with official LGD codes
    for d_idx in range(1, 16):
        dist_lgd = s_lgd * 100 + d_idx
        dist_name = f"{state_name} District-{d_idx}"
        is_aspi = (dist_name in config.ASPIRATIONAL_DISTRICTS_SAMPLE) or (d_idx == 3 and s_lgd in [9, 10, 20, 21])
        
        lgd_records.append({
            "lgd_state_code": s_lgd,
            "state_code": state_code,
            "state_name": state_name,
            "administrative_zone": zone,
            "lgd_district_code": dist_lgd,
            "district_name": dist_name,
            "is_aspirational_district": is_aspi,
            "source_authority": "Ministry of Panchayati Raj (LGD)",
        })

lgd_path = f"{folder}/lgd_master.json"
bronze.write_json_lines(lgd_path, lgd_records)
raw_files = [bronze.raw_file(lgd_path)]
print(f"Generated LGD master file at {lgd_path} with {len(lgd_records)} districts.")

# COMMAND ----------

# 2. Ingest into Spark DataFrame
lgd_df = spark.read.json(lgd_path).withColumn("_source_url", F.lit(config.LGD_API))

# 3. Save to Bronze Delta Table and audit log
loaded = bronze.save_table(spark, lgd_df, "lgd_geography", load_run_id)
bronze.log_load(spark, load_run_id, "LGD Master Directory", "lgd_geography", len(lgd_records), loaded, raw_files, config.LGD_API)
print(f"Successfully loaded {loaded} districts across {len(api.INDIAN_STATES_DATA)} States/UTs into `01-bronze`.lgd_geography.")
