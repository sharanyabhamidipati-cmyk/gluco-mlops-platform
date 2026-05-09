import os
import joblib
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "glucose_risk_model.pkl")

model = joblib.load(MODEL_PATH)


def predict_glucose_risk(glucose, hour, day_of_week, is_overnight):
    input_data = pd.DataFrame(
        [[glucose, hour, day_of_week, is_overnight]],
        columns=[
            "glucose",
            "hour",
            "day_of_week",
            "is_overnight",
        ]
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]

    return {
        "prediction": int(prediction),
        "risk_probability": round(float(probability), 4)
    }
