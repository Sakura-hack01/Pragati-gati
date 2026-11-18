-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Set up the PragatiGati Lakehouse Catalog
-- MAGIC
-- MAGIC Run this once from VS Code, as a workflow. It is safe to re-run. It only adds what is missing.
-- MAGIC
-- MAGIC Creates the `pragatigati-capstone` catalog, one schema per medallion layer in run order,
-- MAGIC and the `00-source`.`landing` volume for Indian infrastructure files and API snapshots.

-- COMMAND ----------

CREATE CATALOG IF NOT EXISTS `pragatigati-capstone`;
USE CATALOG `pragatigati-capstone`;

CREATE SCHEMA IF NOT EXISTS `00-source` COMMENT 'Raw landing volume: API responses, LGD files, Census snapshots';
CREATE SCHEMA IF NOT EXISTS `01-bronze` COMMENT 'High-fidelity raw tables as ingested, with load timestamps and sha256 checksums';
CREATE SCHEMA IF NOT EXISTS `02-silver` COMMENT 'Cleaned, standardized data linked with official LGD codes and ₹ INR figures';
CREATE SCHEMA IF NOT EXISTS `03-gold` COMMENT 'Star schema (facts & dimensions) and analytical aggregates for Dashboards and Genie';
CREATE SCHEMA IF NOT EXISTS `04-validation` COMMENT 'Automated data quality results, stop/flag rules, and pipeline audit logs';

CREATE VOLUME IF NOT EXISTS `00-source`.landing COMMENT 'Landing storage for raw JSONs, GeoJSONs, and MoSPI Census files';

SHOW SCHEMAS;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Catalog Verification
-- MAGIC
-- MAGIC Confirm all five schemas exist under `pragatigati-capstone`.
-- MAGIC If transitioning from an older catalog, old schemas can be safely decommissioned.
