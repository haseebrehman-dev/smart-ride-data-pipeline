import pandas as pd
import random
from datetime import datetime, timedelta

print("Starting InDrive (Lahore) Data Generation...")

# Lahore  locations
locations = ['Johar Town', 'DHA Phase 5', 'Gulberg III', 'Model Town', 
             'Bahria Town', 'Wapda Town', 'Cantt', 'Iqbal Town']
statuses = ['Completed', 'Completed', 'Completed', 'Cancelled', 'Driver_Cancelled']

data = []
start_date = datetime(2026, 5, 1)

# 5,000 rides data generation
for i in range(1, 5001):
    pickup = random.choice(locations)
    dropoff = random.choice([loc for loc in locations if loc != pickup])
    
    # Random time logic
    trip_time = start_date + timedelta(days=random.randint(0, 10), minutes=random.randint(0, 1440))
    
    # Fare and Distance logic
    distance = round(random.uniform(2.0, 25.0), 1) # 2km to 25km
    fare = int(distance * random.uniform(70, 100)) # PKR 70-100 per km
    
    status = random.choice(statuses)
    if status != 'Completed':
        fare = 0 # Cancelled ride  fare zero
        
    data.append({
        "trip_id": f"TRP-{10000 + i}",
        "driver_id": random.randint(500, 550),
        "pickup_location": pickup,
        "dropoff_location": dropoff,
        "pickup_datetime": trip_time.strftime("%Y-%m-%d %H:%M:%S"),
        "distance_km": distance,
        "fare_pkr": fare,
        "ride_status": status
    })

# Create DataFrame and save in CSV
df = pd.DataFrame(data)
file_name = "raw_indrive_rides.csv"
df.to_csv(file_name, index=False)

print(f"Success! {len(df)} rides data '{raw_indrive_rides.csv}'  save successfully.")
