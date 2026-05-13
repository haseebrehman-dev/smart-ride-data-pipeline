import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions

# --- PHASE 1: ENGINE SETUP ---

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

print(" Starting Smart-Ride Silver Layer ETL...")

# --- PHASE 2: EXTRACT (Read from Bronze) ---

bronze_path = "s3://smartride-datalake-haseeb-2026/bronze/raw_indrive_rides.csv"

raw_df = spark.read.option("header", "true").option("inferSchema", "true").csv(bronze_path)

# --- PHASE 3: TRANSFORM (Cleaning Logic) ---
print(" Cleaning Data: Removing cancelled rides and zero fares...")
clean_df = raw_df.filter((raw_df.ride_status == 'Completed') & (raw_df.fare_pkr > 0))

# --- PHASE 4: LOAD (Write to Silver) ---
silver_path = "s3://smartride-datalake-haseeb-2026/silver/clean_rides/"

print(f" Saving clean data to {silver_path} in Parquet format...")
clean_df.write.mode("overwrite").parquet(silver_path)

print(" ETL Job Completed Successfully!")