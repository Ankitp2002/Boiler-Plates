import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from scipy import stats
import os

class DataAnalyzer:
    def __init__(self, df):
        self.df = df
        self.dtypes_detected = self._detect_types()
    
    def _detect_types(self):
        """Auto-detect column types."""
        dtypes = {}
        for col in self.df.columns:
            if self.df[col].dtype == 'object':
                # Try numeric conversion
                if pd.to_numeric(self.df[col], errors='coerce').notna().all():
                    dtypes[col] = 'numeric'
                else:
                    dtypes[col] = 'categorical'
            else:
                dtypes[col] = 'numeric'
        return dtypes
    
    def stats_summary(self):
        """Generate statistical summaries."""
        summary = {}
        numeric_cols = [col for col, dtype in self.dtypes_detected.items() if dtype == 'numeric']
        cat_cols = [col for col, dtype in self.dtypes_detected.items() if dtype == 'categorical']
        
        if numeric_cols:
            summary['numeric'] = self.df[numeric_cols].describe()
        if cat_cols:
            summary['categorical'] = self.df[cat_cols].describe()
        return summary
    
    def plot_distributions(self):
        """Create distribution plots."""
        figs = {}
        numeric_cols = [col for col, dtype in self.dtypes_detected.items() if dtype == 'numeric']
        
        for col in numeric_cols[:4]:  # Limit for performance
            fig = px.histogram(self.df, x=col, title=f'Distribution of {col}')
            figs[col] = fig
        
        cat_cols = [col for col, dtype in self.dtypes_detected.items() if dtype == 'categorical']
        for col in cat_cols[:4]:
            fig = px.bar(self.df[col].value_counts().reset_index(), x='index', y=col, title=f'{col} Counts')
            figs[col] = fig
        
        return figs
    
    def detect_anomalies(self):
        """Flag anomalies using Z-score > 3."""
        anomalies = {}
        numeric_cols = [col for col, dtype in self.dtypes_detected.items() if dtype == 'numeric']
        for col in numeric_cols:
            z_scores = np.abs(stats.zscore(self.df[col].dropna()))
            anomaly_mask = z_scores > 3
            anomalies[col] = self.df[anomaly_mask].index.tolist()
        return anomalies
