-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Silver: Standardized Projects & Places (PragatiGati)
-- MAGIC
-- MAGIC Cleans, harmonizes, and enriches raw Bronze data:
-- MAGIC 1. Maps raw district names to authoritative LGD (Local Government Directory) codes.
-- MAGIC 2. Standardizes financial outlay and payments into Indian Rupee (₹ Crores).
-- MAGIC 3. Calculates the Financial-to-Physical Disparity ratio to detect "Ghost Progress" anomalies.
-- MAGIC 4. Flags PARIVESH clearance bottlenecks and trapped capital.

-- COMMAND ----------

USE CATALOG `pragatigati-capstone`;

CREATE OR REPLACE TABLE `02-silver`.places AS
SELECT
    g.lgd_district_code,
    g.district_name,
    g.lgd_state_code,
    g.state_name,
    g.state_code,
    g.administrative_zone,
    COALESCE(c.population_projected_2024, 1500000) AS population,
    COALESCE(g.is_aspirational_district, FALSE) AS is_aspirational_district,
    CURRENT_TIMESTAMP() AS updated_ts
FROM `01-bronze`.lgd_geography AS g
LEFT JOIN `01-bronze`.census_population AS c
    ON g.lgd_district_code = c.lgd_district_code;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Silver Projects Transformation

-- COMMAND ----------

CREATE OR REPLACE TABLE `02-silver`.projects AS
SELECT
    p.contractId AS contract_id,
    TRIM(p.projectName) AS project_name,
    p.executingAgency AS executing_agency,
    p.sector,
    p.gatishaktiEngine AS gatishakti_engine,
    p.state AS state_name,
    p.district AS district_name,
    g.lgd_district_code,
    g.lgd_state_code,
    g.administrative_zone,
    
    -- Standardized Capex in ₹ Crores
    CAST(p.budgetInCrores AS DECIMAL(18, 2)) AS budget_crores,
    CAST(p.amountPaidInCrores AS DECIMAL(18, 2)) AS amount_paid_crores,
    ROUND((CAST(p.amountPaidInCrores AS DOUBLE) / NULLIF(CAST(p.budgetInCrores AS DOUBLE), 0)) * 100, 2) AS financial_progress_pct,
    CAST(p.physicalProgressPct AS DOUBLE) AS physical_progress_pct,
    
    -- Disparity Indicator: Financial % - Physical %
    ROUND(
        ((CAST(p.amountPaidInCrores AS DOUBLE) / NULLIF(CAST(p.budgetInCrores AS DOUBLE), 0)) * 100) - CAST(p.physicalProgressPct AS DOUBLE),
        2
    ) AS progress_disparity_pct,
    
    p.status,
    p.pariveshClearanceStatus AS parivesh_clearance_status,
    CASE 
        WHEN p.pariveshClearanceStatus IN ('Stage_I_Pending', 'Stage_II_Pending', 'Wildlife_Sanction_Pending', 'Land_Acquisition_Dispute', 'CRZ_Review')
        THEN TRUE 
        ELSE FALSE 
    END AS is_clearance_blocked,
    
    p.contractorName AS contractor_name,
    p.concessionModel AS concession_model,
    CAST(p.latitude AS DOUBLE) AS latitude,
    CAST(p.longitude AS DOUBLE) AS longitude,
    CAST(p.startDate AS DATE) AS start_date,
    CAST(p.targetCompletionDate AS DATE) AS target_completion_date,
    CURRENT_TIMESTAMP() AS silver_load_ts
FROM `01-bronze`.nhai_morth_projects AS p
LEFT JOIN `02-silver`.places AS g
    ON p.state = g.state_name AND p.district = g.district_name;

-- COMMAND ----------

SELECT COUNT(*) AS total_silver_projects FROM `02-silver`.projects;
