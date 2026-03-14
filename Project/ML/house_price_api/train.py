import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from preprocessor import preprocessor
import optuna
import joblib
import os

mlflow.set_experiment("house_price_prediction")
mlflow.set_tracking_uri("http://localhost:5000")  # Local MLflow server

def objective(trial):
    # Hyperparameters
    n_estimators = trial.suggest_int('n_estimators', 50, 300)
    max_depth = trial.suggest_int('max_depth', 5, 20)
    min_samples_split = trial.suggest_int('min_samples_split', 2, 20)
    
    # Load data
    housing = fetch_california_housing(as_frame=True)
    X = pd.DataFrame(housing.data, columns=housing.feature_names)
    y = np.log(housing.target + 1)  # Log transform
    
    # Preprocess
    X_processed = preprocessor.fit_transform(X)
    
    # Train model
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )
    
    # Cross-validation
    scores = cross_val_score(model, X_processed, y, cv=5, scoring='neg_mean_squared_error')
    rmse = np.sqrt(-scores.mean())
    
    return rmse

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    
    # Start MLflow server (run separately: mlflow ui)
    print("🔍 Run MLflow: mlflow ui --port 5000")
    print("🚀 Optimizing...")
    
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=50)
    
    # Log best model
    with mlflow.start_run():
        best_params = study.best_params
        print(f"✅ Best RMSE: {study.best_value:.4f}")
        print(f"📊 Best params: {best_params}")
        
        # Train final model
        housing = fetch_california_housing(as_frame=True)
        X = pd.DataFrame(housing.data, columns=housing.feature_names)
        y = np.log(housing.target + 1)
        
        X_processed = preprocessor.fit_transform(X)
        final_model = RandomForestRegressor(**best_params, random_state=42)
        final_model.fit(X_processed, y)
        
        # Save artifacts
        joblib.dump(final_model, "models/best_model.pkl")
        joblib.dump(preprocessor, "models/preprocessor.pkl")
        
        mlflow.log_params(best_params)
        mlflow.log_metric("rmse", study.best_value)
        mlflow.sklearn.log_model(final_model, "model")
        mlflow.sklearn.log_model(preprocessor, "preprocessor")
