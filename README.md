# 🚗 Smart-Ride: Scalable Data Lake & Analytics Pipeline

## 📖 Project Overview
This project focuses on building a robust end-to-end Data Engineering pipeline for a high-volume Ride-Hailing platform (similar to InDrive or Careem). The goal is to manage massive amounts of trip data, ensuring high availability, data quality, and ready-to-use analytics for business decision-making.

## 🏗️ Data Architecture (Medallion Approach)
The pipeline implements the **Medallion Architecture** to maintain a clean and reliable Data Lake on AWS:

* **Bronze Zone (Raw Layer):** Immutable storage of raw JSON/CSV ride data ingested directly from source systems.
* **Silver Zone (Cleansing Layer):** Filtered and standardized data processed via PySpark to remove cancellations and anomalies.
* **Gold Zone (Curated Layer):** Aggregated business-level tables optimized for high-speed SQL querying and BI Dashboards.

## 🛠️ Technical Ecosystem
* **Language:** Python 3.x (Data Generation & Ingestion)
* **Distributed Computing:** PySpark / AWS Glue
* **Cloud Storage:** Amazon S3 (Object Storage)
* **Query Engine:** Amazon Athena (Serverless SQL)
* **Version Control:** Git & GitHub

## 🚀 Key Implementations

### 1. Data Ingestion & Storage
The initial phase involves simulating real-world ride logs from Lahore (pickup/dropoff, fares, distance) and ingesting them into the S3 Bronze bucket. This ensures we have a "Source of Truth" before any transformation.

### 2. Cloud Infrastructure (AWS S3)
The data lake is structured to support scalability. Below is the current state of the Bronze landing zone:
![S3 Bronze Zone](./assets/s3_bronze_zone.png)

## 📊 Future Enhancements
- Automating the ETL trigger using AWS Lambda or Airflow.
- Implementing real-time streaming with AWS Kinesis.
- Developing a Power BI dashboard for trip trend analysis.
