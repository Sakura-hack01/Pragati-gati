# Databricks notebook source
# MAGIC %md
# MAGIC # Check Indian Infrastructure Data Sources
# MAGIC
# MAGIC Databricks can reach open APIs and public portals. This notebook validates connectivity
# MAGIC to Indian Government infrastructure portals, Gati Shakti, LGD, MoSPI, and PARIVESH.
# MAGIC
# MAGIC - **OK:** Accessible directly via API or automated pipeline.
# MAGIC - **HTTP 403 or BLOCKED:** Upload snapshot files to the `00-source.landing` volume.
# MAGIC - **Endpoints configured in:** `src/config.py`

# COMMAND ----------

import os
import sys

repo_root = os.path.abspath("../..")  # the repo root, so the import below works everywhere
sys.path.insert(0, repo_root)

from src import api, config

rows = [(name, api.check(url), url) for name, url in config.SOURCE_CHECKS.items()]
display(spark.createDataFrame(rows, "source string, status string, url string"))
