import joblib
import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt
from preprocessor import preprocess_text, get_vectorizer
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import os 
import requests
import zipfile
import io

def load_data():
    """Download and load SMS Spam dataset from UCI."""

    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00228/smsspamcollection.zip"
    data_file = "SMSSpamCollection"

    # Download if file does not exist
    if not os.path.exists(data_file):
        print("Downloading dataset...")
        response = requests.get(url)
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        zip_file.extractall()

    # Load dataset
    df = pd.read_csv(data_file, sep="\t", names=["label", "text"])
    # Apply preprocessing
    df["text"] = df["text"].apply(preprocess_text)
    return df

def train_models():
    """Train and compare models."""
    df = load_data()
    X = df['text']
    y = df['label'].map({'ham': 0, 'spam': 1})
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    vectorizer, X_train_vec = get_vectorizer(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    # Train models
    nb_model = MultinomialNB().fit(X_train_vec, y_train)
    lr_model = LogisticRegression(random_state=42).fit(X_train_vec, y_train)
    
    # Predictions
    nb_pred = nb_model.predict(X_test_vec)
    lr_pred = lr_model.predict(X_test_vec)
    
    # Metrics
    nb_acc = accuracy_score(y_test, nb_pred)
    lr_acc = accuracy_score(y_test, lr_pred)
    
    # Save models
    joblib.dump(nb_model, 'nb_model.pkl')
    joblib.dump(lr_model, 'lr_model.pkl')
    joblib.dump(vectorizer, 'vectorizer.pkl')
    
    return {
        'nb_acc': nb_acc,
        'lr_acc': lr_acc,
        'nb_matrix': confusion_matrix(y_test, nb_pred),
        'lr_matrix': confusion_matrix(y_test, lr_pred)
    }

def plot_confusion_matrices(results):
    """Plot confusion matrices."""
    fig = make_subplots(rows=1, cols=2, 
                       subplot_titles=('Naive Bayes', 'Logistic Regression'),
                       specs=[[{"type": "heatmap"}, {"type": "heatmap"}]])
    
    # NB
    fig.add_trace(
        go.Heatmap(z=results['nb_matrix'], x=['Ham', 'Spam'], y=['Ham', 'Spam'],
                  colorscale='Blues'),
        row=1, col=1
    )
    
    # LR
    fig.add_trace(
        go.Heatmap(z=results['lr_matrix'], x=['Ham', 'Spam'], y=['Ham', 'Spam'],
                  colorscale='Blues'),
        row=1, col=2
    )
    
    fig.update_layout(title="Confusion Matrices (Test Set)", height=400)
    fig.write_html('confusion_matrices.html')
    return fig
