import xgboost as xgb
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
import shap
import matplotlib.pyplot as plt
import pandas as pd
from preprocessor import CreditPreprocessor

class CreditTrainer:
    def __init__(self):
        self.preprocessor = CreditPreprocessor()
        self.models = {}
    
    def train_models(self):
        """Train XGBoost + baselines."""
        X_train, y_train, X_test, y_test = self.preprocessor.prepare_data()
        
        # XGBoost
        xgb_model = xgb.XGBClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            subsample=0.8,
            random_state=42
        )
        xgb_model.fit(X_train, y_train)
        
        # Random Forest
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_model.fit(X_train, y_train)
        
        # Logistic Regression
        lr_model = LogisticRegression(random_state=42)
        lr_model.fit(X_train, y_train)
        
        self.models = {'xgb': xgb_model, 'rf': rf_model, 'lr': lr_model}
        
        # Save
        joblib.dump(self.models, 'models/credit_models.pkl')
        joblib.dump(self.preprocessor, 'models/preprocessor.pkl')
        
        # SHAP explainer
        explainer = shap.TreeExplainer(xgb_model)
        shap_values = explainer.shap_values(X_test[:100])  # Sample
        shap.summary_plot(shap_values, X_test[:100], show=False)
        plt.savefig('outputs/shap_summary.png')
        
        print("✅ Models trained + SHAP saved!")
        return {
            'xgb_auc': roc_auc_score(y_test, xgb_model.predict_proba(X_test)[:, 1]),
            'rf_auc': roc_auc_score(y_test, rf_model.predict_proba(X_test)[:, 1]),
            'lr_auc': roc_auc_score(y_test, lr_model.predict_proba(X_test)[:, 1])
        }

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)
    trainer = CreditTrainer()
    results = trainer.train_models()
    print(results)
