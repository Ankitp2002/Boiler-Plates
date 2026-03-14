import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import joblib

class CreditPreprocessor:
    def __init__(self):
        self.scaler = StandardScaler()
        self.smote = SMOTE(random_state=42)
        self.label_encoders = {}
    
    def load_data(self):
        """Load UCI Bank dataset."""
        df = pd.read_csv("data/bank-additional-full.csv", sep=';')
        return df
    
    def engineer_features(self, df):
        """Financial feature engineering."""
        df = df.copy()
        
        # Target: y (yes=loan, no=no loan)
        df['target'] = (df['y'] == 'yes').astype(int)
        df.drop('y', axis=1, inplace=True)
        
        # Financial ratios
        df['income_stability'] = df['pdays'] / (df['campaign'] + 1)
        df['debt_burden'] = df['euribor3m'] * df['cons.price.idx']
        df['risk_score'] = df['age'] * df['default'].astype(int)
        
        # Categorical encoding
        cat_cols = df.select_dtypes(include=['object']).columns
        for col in cat_cols:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col].astype(str))
            self.label_encoders[col] = le
        
        return df
    
    def prepare_data(self, test_size=0.2):
        """Full pipeline: engineer + split + scale + SMOTE."""
        df = self.load_data()
        df = self.engineer_features(df)
        
        X = df.drop('target', axis=1)
        y = df['target']
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=42, stratify=y
        )
        
        # Scale
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # SMOTE (only training set)
        X_train_balanced, y_train_balanced = self.smote.fit_resample(
            X_train_scaled, y_train
        )
        
        return (X_train_balanced, y_train_balanced, X_test_scaled, y_test)
