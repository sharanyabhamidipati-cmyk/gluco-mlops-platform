import time

from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

from app.predict import predict_glucose_risk


app = FastAPI(
    title="Gluco MLOps Platform",
    version="1.0"
)


REQUEST_COUNT = Counter(
    "gluco_api_requests_total",
    "Total number of API requests",
    ["method", "endpoint"]
)

PREDICTION_COUNT = Counter(
    "gluco_predictions_total",
    "Total number of prediction requests"
)

REQUEST_LATENCY = Histogram(
    "gluco_api_request_latency_seconds",
    "API request latency in seconds",
    ["endpoint"]
)


class GlucoseRequest(BaseModel):
    glucose: float
    hour: int
    day_of_week: int
    is_overnight: int


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    latency = time.time() - start_time
    endpoint = request.url.path

    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=endpoint
    ).inc()

    REQUEST_LATENCY.labels(
        endpoint=endpoint
    ).observe(latency)

    return response


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
    PREDICTION_COUNT.inc()

    result = predict_glucose_risk(
        glucose=data.glucose,
        hour=data.hour,
        day_of_week=data.day_of_week,
        is_overnight=data.is_overnight
    )

    return result


@app.get("/metrics")
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )
