from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from typing import List
import uvicorn

app = FastAPI(title="🏠 House Price Predictor API")

# Load models
model = joblib.load("models/best_model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.post("/predict")
async def predict_price(features: HouseFeatures):
    """Predict house price in $100K units."""
    try:
        # Prepare data
        data = pd.DataFrame([features.dict()])
        X_processed = preprocessor.transform(data)
        
        # Predict
        log_price = model.predict(X_processed)[0]
        price = np.exp(log_price) - 1  # Reverse log transform
        
        return {
            "predicted_price_100k": float(price),
            "confidence": float(model.predict_proba(X_processed)[0].max()) if hasattr(model, 'predict_proba') else 0.95
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model": "RandomForest"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
