import streamlit as st
import pandas as pd
from analyzer import DataAnalyzer
import plotly.graph_objects as go

st.title("📊 Smart Data Analyzer")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    analyzer = DataAnalyzer(df)
    
    # Sidebar
    st.sidebar.subheader("Data Info")
    st.sidebar.write(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    # Stats
    st.header("📈 Statistical Summary")
    summary = analyzer.stats_summary()
    for key, table in summary.items():
        st.subheader(key.title())
        st.dataframe(table)
    
    # Plots
    st.header("📊 Distributions")
    figs = analyzer.plot_distributions()
    for col, fig in figs.items():
        st.plotly_chart(fig, use_container_width=True)
    
    # Anomalies
    st.header("🚨 Anomalies Detected")
    anomalies = analyzer.detect_anomalies()
    if any(anomalies.values()):
        anomaly_df = pd.DataFrame()
        for col, indices in anomalies.items():
            if indices:
                anomaly_df[f'{col}_anomalies'] = indices
        st.dataframe(anomaly_df)
        st.success(f"Found anomalies in {len([v for v in anomalies.values() if v])} columns!")
    else:
        st.info("No anomalies detected (Z-score > 3).")
    
    # Raw data
    st.header("📋 Raw Data")
    st.dataframe(df)
