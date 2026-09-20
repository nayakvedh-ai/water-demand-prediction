import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# Number of days
days = 730

# Create dates
dates = pd.date_range(start="2024-01-01", periods=days, freq="D")

# Generate weather-related data
temperature = np.random.normal(28, 4, days)
temperature = np.clip(temperature, 18, 40)

rainfall = np.random.exponential(2, days)
rainfall = np.clip(rainfall, 0, 30)

humidity = np.random.normal(65, 12, days)
humidity = np.clip(humidity, 35, 95)

# Determine weekday/weekend
day_type = dates.dayofweek.map(
    lambda x: "Weekend" if x >= 5 else "Weekday"
)

# Generate water demand
base_demand = 10000

water_demand = (
    base_demand
    + (temperature - 25) * 250
    - rainfall * 80
    + np.array([500 if day == "Weekday" else -300 for day in day_type])
    + np.random.normal(0, 300, days)
)

water_demand = np.maximum(water_demand, 5000)

# Previous day's demand
previous_demand = np.roll(water_demand, 1)
previous_demand[0] = water_demand[0]

# Create DataFrame
data = pd.DataFrame({
    "Date": dates,
    "Temperature": temperature.round(2),
    "Rainfall": rainfall.round(2),
    "Humidity": humidity.round(2),
    "Day_Type": day_type,
    "Previous_Demand": previous_demand.round(2),
    "Water_Demand": water_demand.round(2)
})

# Save dataset
data.to_csv("data/water_demand.csv", index=False)

print("Dataset created successfully!")
print(f"Number of records: {len(data)}")
print("\nFirst 5 records:")
print(data.head())