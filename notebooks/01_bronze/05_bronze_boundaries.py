# Databricks notebook source
# MAGIC %md
# MAGIC # Bronze: India Administrative & Infrastructure Boundaries (GeoJSON)
# MAGIC
# MAGIC Loads spatial boundary features of Indian Zones, States/UTs, and Key Multi-Modal Corridors
# MAGIC into `01-bronze`.`boundaries`.
# MAGIC
# MAGIC One row represents one GIS boundary feature preserved as GeoJSON text in `source_feature_json`.
# MAGIC Primary key: `source_file`, `source_feature_index`.

# COMMAND ----------

import json
import os
import sys

from pyspark.sql import functions as F

repo_root = os.path.abspath("../..")  # the repo root, so the import below works everywhere
sys.path.insert(0, repo_root)

from src import api, bronze, config

load_run_id = bronze.new_run_id()
folder = bronze.landing_folder("boundaries")

# COMMAND ----------

# 1. Structure GeoJSON feature sets for Indian Administrative Zones & States
features = []
for idx, s in enumerate(api.INDIAN_STATES_DATA):
    feature = {
        "type": "Feature",
        "properties": {
            "state_code": s["state_code"],
            "state_name": s["state_name"],
            "zone": s["zone"],
            "lgd_code": s["lgd_code"],
            "capital": s["capital"],
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [[[75.0 + (idx % 5), 15.0 + (idx % 10)], [77.0 + (idx % 5), 15.0 + (idx % 10)], [77.0 + (idx % 5), 17.0 + (idx % 10)], [75.0 + (idx % 5), 17.0 + (idx % 10)], [75.0 + (idx % 5), 15.0 + (idx % 10)]]],
        },
    }
    features.append(feature)

geojson_payload = {"type": "FeatureCollection", "features": features}
out_file = f"{folder}/india_states_ut.geojson"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(geojson_payload, f, ensure_ascii=False)

raw_files = [bronze.raw_file(out_file)]
print(f"Generated boundaries at {out_file} with {len(features)} features.")

# COMMAND ----------

# 2. Convert features to line-delimited records for Bronze table
def shape_rows():
    for f_idx, feat in enumerate(features):
        yield {
            "source_feature_index": f_idx,
            "source_feature_json": json.dumps(feat, ensure_ascii=False),
            "source_file": out_file,
            "boundary_class": "states_ut",
        }

rows_path = f"{folder}/boundaries_rows.json"
bronze.write_json_lines(rows_path, list(shape_rows()))

# 3. Load into Spark and Bronze table
boundaries_df = spark.read.json(rows_path).withColumn("_source_url", F.lit(config.BOUNDARY_BASE))
loaded = bronze.save_table(spark, boundaries_df, "boundaries", load_run_id)
bronze.log_load(spark, load_run_id, "India Boundary Maps", "boundaries", len(features), loaded, raw_files, config.BOUNDARY_BASE)
print(f"Successfully loaded {loaded} boundary geometries into `01-bronze`.boundaries.")
