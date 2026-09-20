from flask import Flask, render_template, request
import joblib
import pandas as pd


app = Flask(__name__)


# Load trained ML model
model = joblib.load("model/water_demand_model.pkl")

# Load historical dataset
data = pd.read_csv("data/water_demand.csv")


@app.route("/")
def home():

    # Dashboard statistics
    average_demand = round(data["Water_Demand"].mean(), 2)
    maximum_demand = round(data["Water_Demand"].max(), 2)
    minimum_demand = round(data["Water_Demand"].min(), 2)

    # Prepare data for chart
    dates = data["Date"].tolist()
    demands = data["Water_Demand"].tolist()

    return render_template(
        "index.html",
        average_demand=average_demand,
        maximum_demand=maximum_demand,
        minimum_demand=minimum_demand,
        dates=dates,
        demands=demands
    )


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from form
    temperature = float(request.form["temperature"])
    rainfall = float(request.form["rainfall"])
    humidity = float(request.form["humidity"])
    previous_demand = float(request.form["previous_demand"])

    # Prepare model input
    input_data = [[
        temperature,
        rainfall,
        humidity,
        previous_demand
    ]]

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Conservation recommendation
    if prediction >= 12000:

        recommendation = (
            "High water demand is expected. "
            "Consider reducing unnecessary water usage, "
            "checking for leaks, and prioritizing essential consumption."
        )

        demand_level = "High Demand"

    elif prediction >= 10000:

        recommendation = (
            "Moderate water demand is expected. "
            "Continue responsible water usage and avoid unnecessary wastage."
        )

        demand_level = "Moderate Demand"

    else:

        recommendation = (
            "Lower water demand is expected. "
            "Continue following sustainable water-use practices."
        )

        demand_level = "Low Demand"


    # Dashboard statistics
    average_demand = round(data["Water_Demand"].mean(), 2)
    maximum_demand = round(data["Water_Demand"].max(), 2)
    minimum_demand = round(data["Water_Demand"].min(), 2)


    return render_template(
    "index.html",
    prediction=round(prediction, 2),
    recommendation=recommendation,
    demand_level=demand_level,
    average_demand=average_demand,
    maximum_demand=maximum_demand,
    minimum_demand=minimum_demand,
    dates=data["Date"].tolist(),
    demands=data["Water_Demand"].tolist()
)


if __name__ == "__main__":
    app.run(debug=True)