from fastapi import FastAPI
from pydantic import BaseModel

from app.predict import predict_glucose_risk

app = FastAPI(
    title="Gluco MLOps Platform",
    version="1.0"
)


class GlucoseRequest(BaseModel):
    glucose: float
    hour: int
    day_of_week: int
    is_overnight: int


@app.get("/")
def home():
    return {
        "message": "Gluco MLOps Platform is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(data: GlucoseRequest):
    result = predict_glucose_risk(
        glucose=data.glucose,
        hour=data.hour,
        day_of_week=data.day_of_week,
        is_overnight=data.is_overnight
    )

    return result
