import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load dataset
data = pd.read_csv("data/water_demand.csv")


# Select input features
X = data[
    [
        "Temperature",
        "Rainfall",
        "Humidity",
        "Previous_Demand"
    ]
]

# Select target
y = data["Water_Demand"]


# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = LinearRegression()


# Train model
model.fit(X_train, y_train)


# Make predictions
predictions = model.predict(X_test)


# Evaluate model
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)


print("Model Training Completed!")
print()
print("Model Performance:")
print("-------------------")
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.3f}")


# Save trained model
joblib.dump(model, "model/water_demand_model.pkl")

print()
print("Model saved successfully!")