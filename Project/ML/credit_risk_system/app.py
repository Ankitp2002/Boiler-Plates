import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import confusion_matrix
import numpy as np

st.title("🏦 Credit Risk Scoring System")

# Load models
@st.cache_resource
def load_models():
    models = joblib.load('models/credit_models.pkl')
    preprocessor = joblib.load('models/preprocessor.pkl')
    return models, preprocessor

models, preprocessor = load_models()

# Sidebar: Single prediction
st.sidebar.header("🔍 Score Applicant")
age = st.sidebar.slider("Age", 18, 80, 35)
job = st.sidebar.selectbox("Job", ["admin", "blue-collar", "technician"])
income = st.sidebar.number_input("Monthly Income (€)", 0, 5000, 1000)
loan_amount = st.sidebar.number_input("Loan Amount (€)", 1000, 50000, 5000)

if st.sidebar.button("🚀 Predict Risk"):
    # Create applicant data
    applicant = pd.DataFrame({
        'age': [age], 'job': [job], 'income': [income],
        'loan_amount': [loan_amount], 'duration': [300]
    })
    
    # Preprocess
    X_processed = preprocessor.scaler.transform(applicant)
    prob = models['xgb'].predict_proba(X_processed)[0, 1]
    
    st.sidebar.metric("Risk Score", f"{prob:.1%}")
    st.sidebar.success("✅ Low Risk" if prob < 0.3 else "⚠️ Medium Risk" if prob < 0.7 else "❌ High Risk")

# Main dashboard
col1, col2 = st.columns(2)

with col1:
    st.header("📊 Model Comparison")
    # Mock metrics (replace with real after training)
    metrics = {
        'XGBoost': 0.92, 'Random Forest': 0.89, 'Logistic': 0.85
    }
    fig = px.bar(x=list(metrics.keys()), y=list(metrics.values()), 
                title="AUC-ROC Scores")
    st.plotly_chart(fig)

with col2:
    st.header("🎯 Feature Importance")
    importance = models['xgb'].feature_importances_
    fig = px.bar(x=['Age', 'Income', 'Job', 'Loan'], y=importance[:4])
    st.plotly_chart(fig)

# SHAP plots
st.header("🔍 SHAP Explanations")
st.image("outputs/shap_summary.png")

st.header("📈 Confusion Matrix")
cm = confusion_matrix([0,1,0,1], models['xgb'].predict(X_test[:4]))
fig = px.imshow(cm, text_auto=True, aspect="auto")
st.plotly_chart(fig)
