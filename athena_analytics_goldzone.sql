-- ==========================================
-- PROJECT: Smart-Ride Data Pipeline
-- LAYER: Gold Zone (Analytics)
-- TOOL: Amazon Athena
-- ==========================================

-- 1. Create External Table (pointing to Silver Parquet data)

CREATE EXTERNAL TABLE IF NOT EXISTS silver (
    trip_id STRING,
    driver_id STRING,
    pickup_location STRING,
    dropoff_location STRING,
    pickup_datetime STRING,
    distance_km DOUBLE,
    fare_pkr DOUBLE,
    ride_status STRING
)
STORED AS PARQUET
LOCATION 's3://smartride-datalake-haseeb-2026/silver/clean_rides/';


-- 2. Business Summary (KPIs)
SELECT 
    COUNT(trip_id) as total_successful_rides,
    SUM(fare_pkr) as total_revenue_pkr,
    AVG(distance_km) as average_distance_km
FROM silver;


-- 3. High-Demand Pickup Locations
SELECT 
    pickup_location, 
    COUNT(trip_id) as trip_count, 
    SUM(fare_pkr) as total_revenue
FROM silver
GROUP BY pickup_location
ORDER BY total_revenue DESC;


-- 4. Data Quality Validation
SELECT 
    ride_status, 
    COUNT(*) as total_count 
FROM silver
GROUP BY ride_status;