from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Bug Prediction API")

model = joblib.load("best_model.joblib")
preproc = joblib.load("preproc.joblib")

FEATURES = [
    "radon_total_complexity",
    "radon_num_items",
    "pylint_msgs_count",
    "pylint_rc",
    "bandit_issues_count",
    "bandit_rc"
]

class PredictRequest(BaseModel):
    radon_total_complexity: float
    radon_num_items: float
    pylint_msgs_count: float
    pylint_rc: float
    bandit_issues_count: float
    bandit_rc: float

@app.get("/")
def root():
    return {"status": "Bug Predictor API running"}

@app.post("/predict")
def predict(req: PredictRequest):
    X = pd.DataFrame([[getattr(req, f) for f in FEATURES]], columns=FEATURES)
    proba = model.predict_proba(X)[0][1]
    label = "BUG-FIX LIKELY" if proba >= 0.5 else "NON-BUG"
    return {"label": label, "probability": round(float(proba), 4)}
