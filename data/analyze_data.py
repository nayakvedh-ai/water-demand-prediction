import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/water_demand.csv")

# -------------------------------
# Graph 1: Temperature vs Demand
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(data["Temperature"], data["Water_Demand"])
plt.xlabel("Temperature (°C)")
plt.ylabel("Water Demand")
plt.title("Temperature vs Water Demand")
plt.grid(True)
plt.show()


# -------------------------------
# Graph 2: Rainfall vs Demand
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(data["Rainfall"], data["Water_Demand"])
plt.xlabel("Rainfall (mm)")
plt.ylabel("Water Demand")
plt.title("Rainfall vs Water Demand")
plt.grid(True)
plt.show()


# -------------------------------
# Graph 3: Daily Water Demand
# -------------------------------
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Water_Demand"])
plt.xlabel("Date")
plt.ylabel("Water Demand")
plt.title("Daily Water Demand Trend")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()