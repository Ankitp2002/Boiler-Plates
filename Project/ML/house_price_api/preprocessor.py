from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import pandas as pd
import numpy as np

class HousingFeatureEngineer(BaseEstimator, TransformerMixin):
    """Custom feature engineering for California Housing."""
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        
        # Feature engineering
        X['rooms_per_household'] = X['AveRooms'] / (X['Population'] + 1)
        X['bedrooms_per_room'] = X['AveBedrms'] / (X['AveRooms'] + 1)
        X['population_per_household'] = X['Population'] / (X['AveOccup'] + 1)
        
        # Interaction terms
        X['income_location'] = X['MedInc'] * X['Latitude']
        X['age_location'] = X['HouseAge'] * X['Longitude']
        
        # Log transform target (done in training)
        return X

preprocessor = Pipeline([
    ('features', HousingFeatureEngineer()),
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('scale', StandardScaler())
])
