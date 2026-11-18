-- Databricks notebook source
-- MAGIC %md
-- MAGIC # Gold: Star Schema & PM Gati Shakti Analytical Marts (PragatiGati)
-- MAGIC
-- MAGIC Builds the dimensional model for executive dashboards, policy decision-making, and Databricks Genie:
-- MAGIC - Dimensions: `dim_place`, `dim_gatishakti_engine`, `dim_agency`, `dim_contractor`, `dim_clearance_status`
-- MAGIC - Fact: `fact_project`
-- MAGIC - Analytical Aggregates: `agg_state_equity`, `agg_gatishakti_summary`, `agg_clearance_bottlenecks`

-- COMMAND ----------

USE CATALOG `pragatigati-capstone`;

-- 1. Dimension: Places (LGD Administrative Master)
CREATE OR REPLACE TABLE `03-gold`.dim_place AS
SELECT
    COALESCE(lgd_district_code, -1) AS lgd_district_code,
    COALESCE(district_name, 'Unknown District') AS district_name,
    COALESCE(lgd_state_code, -1) AS lgd_state_code,
    COALESCE(state_name, 'Unknown State') AS state_name,
    COALESCE(state_code, 'NA') AS state_code,
    COALESCE(administrative_zone, 'Central') AS administrative_zone,
    population,
    is_aspirational_district
FROM `02-silver`.places;

-- 2. Dimension: PM Gati Shakti 7 Engines
CREATE OR REPLACE TABLE `03-gold`.dim_gatishakti_engine AS
SELECT
    engine_name,
    pillar_order,
    nodal_ministry,
    strategic_priority
FROM (
    VALUES
        ('Roads', 1, 'Ministry of Road Transport & Highways (MoRTH)', 'Critical'),
        ('Railways', 2, 'Ministry of Railways (MoR)', 'Critical'),
        ('Mass Transport', 3, 'Ministry of Housing & Urban Affairs (MoHUA)', 'High'),
        ('Ports', 4, 'Ministry of Ports, Shipping & Waterways (MoPSW)', 'High'),
        ('Airports', 5, 'Ministry of Civil Aviation (MoCA)', 'High'),
        ('Waterways', 6, 'Inland Waterways Authority of India (IWAI)', 'Medium'),
        ('Logistics Infrastructure', 7, 'Department for Promotion of Industry and Internal Trade (DPIIT)', 'High')
) AS t(engine_name, pillar_order, nodal_ministry, strategic_priority);

-- 3. Fact Table: Projects & Performance Metrics
CREATE OR REPLACE TABLE `03-gold`.fact_project AS
SELECT
    p.contract_id,
    p.project_name,
    p.executing_agency,
    p.sector,
    p.gatishakti_engine,
    COALESCE(p.lgd_district_code, -1) AS lgd_district_code,
    p.state_name,
    p.budget_crores,
    p.amount_paid_crores,
    p.financial_progress_pct,
    p.physical_progress_pct,
    p.progress_disparity_pct,
    
    -- Anomaly Classification
    CASE
        WHEN p.progress_disparity_pct > 25.0 THEN 'CRITICAL_FRONT_LOADING'
        WHEN p.progress_disparity_pct > 15.0 THEN 'MODERATE_DISPARITY'
        WHEN p.progress_disparity_pct < -20.0 THEN 'PHYSICAL_AHEAD_UNPAID'
        ELSE 'BALANCED'
    END AS financial_integrity_status,
    
    p.status,
    p.parivesh_clearance_status,
    p.is_clearance_blocked,
    CASE WHEN p.is_clearance_blocked THEN p.budget_crores ELSE 0.0 END AS trapped_capex_crores,
    
    p.contractor_name,
    p.concession_model,
    p.latitude,
    p.longitude,
    p.start_date,
    p.target_completion_date,
    
    -- IMD Seasonal Disruption Flag
    CASE 
        WHEN p.state_name IN ('Assam', 'Meghalaya', 'Arunachal Pradesh', 'Nagaland', 'Manipur', 'Mizoram', 'Tripura', 'Kerala', 'Goa', 'Uttarakhand', 'Himachal Pradesh')
             AND MONTH(p.target_completion_date) IN (6, 7, 8, 9)
             AND p.physical_progress_pct < 75.0
        THEN 'HIGH_MONSOON_RISK'
        ELSE 'NORMAL'
    END AS monsoon_vulnerability
FROM `02-silver`.projects p;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Gold Analytical Aggregates for Dashboards & Policy Reporting

-- COMMAND ----------

-- Aggregate 1: State-level Capex Equity & Per-Capita Spend (₹ / person)
CREATE OR REPLACE TABLE `03-gold`.agg_state_equity AS
SELECT
    f.state_name,
    COUNT(f.contract_id) AS total_projects,
    ROUND(SUM(f.budget_crores), 2) AS total_capex_crores,
    ROUND(SUM(f.amount_paid_crores), 2) AS total_disbursed_crores,
    ROUND(AVG(f.physical_progress_pct), 1) AS avg_physical_progress_pct,
    ROUND(SUM(f.trapped_capex_crores), 2) AS capex_in_clearance_bottleneck_crores,
    SUM(dp.population) AS estimated_population,
    -- Per capita spend in INR (1 Crore = 10,000,000 INR)
    ROUND((SUM(f.budget_crores) * 10000000.0) / NULLIF(SUM(dp.population), 0), 2) AS capex_per_capita_inr
FROM `03-gold`.fact_project f
LEFT JOIN `03-gold`.dim_place dp
    ON f.lgd_district_code = dp.lgd_district_code
GROUP BY f.state_name;

-- Aggregate 2: Gati Shakti Engine Allocation Breakdown
CREATE OR REPLACE TABLE `03-gold`.agg_gatishakti_summary AS
SELECT
    e.engine_name,
    e.nodal_ministry,
    e.strategic_priority,
    COUNT(f.contract_id) AS project_count,
    ROUND(SUM(f.budget_crores), 2) AS total_budget_crores,
    ROUND(SUM(f.amount_paid_crores), 2) AS total_spent_crores,
    ROUND(AVG(f.physical_progress_pct), 1) AS avg_progress_pct
FROM `03-gold`.dim_gatishakti_engine e
LEFT JOIN `03-gold`.fact_project f
    ON e.engine_name = f.gatishakti_engine
GROUP BY e.engine_name, e.nodal_ministry, e.strategic_priority
ORDER BY total_budget_crores DESC;
