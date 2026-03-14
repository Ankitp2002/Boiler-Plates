fastapi uvicorn scikit-learn optuna mlflow pandas numpy joblib pydantic

# 1. Clone & setup

mkdir house_price_api && cd house_price_api
pip install -r requirements.txt

# 2. Train with MLflow tracking

mlflow ui --port 5000 & # Tracking UI
python train.py # 50 Optuna trials (~10min)

# 3. Test API

python api.py # http://localhost:8000/docs

curl -X POST "http://localhost:8000/predict" \
 -H "Content-Type: application/json" \
 -d '{"MedInc":3.5,"HouseAge":30,"AveRooms":6.2,"AveBedrms":1.1,"Population":1200,"AveOccup":2.5,"Latitude":37.8,"Longitude":-122.2}'

# 4. Docker production

docker build -t house-price-api .
docker run -p 8000:8000 house-price-api
