import pandas as pd
from prophet import Prophet
import joblib
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

def prepare_trends_data():
    """Aggregate ratings by genre and time."""
    ratings = pd.read_csv('data/ml-100k/u.data', sep='\t',
                         names=['user_id', 'movie_id', 'rating', 'timestamp'])
    movies = pd.read_csv('data/ml-100k/u.item', sep='|', encoding='latin-1',
                        usecols=[0,1,2] + list(range(5,24)),
                        names=['movie_id', 'title', 'release_date', 'video_release'] + [f'genre_{i}' for i in range(19)])
    
    # Genre ratings by time
    ratings['ds'] = pd.to_datetime(ratings['timestamp'], unit='s')
    ratings['month'] = ratings['ds'].dt.to_period('M').astype(str)
    
    genre_trends = []
    for genre_col in movies.columns[5:]:
        genre_movies = movies[movies[genre_col] == 1]['movie_id']
        genre_ratings = ratings[ratings['movie_id'].isin(genre_movies)]
        monthly_avg = genre_ratings.groupby('month')['rating'].mean().reset_index()
        monthly_avg['genre'] = genre_col.replace('genre_', '')
        genre_trends.append(monthly_avg)
    
    return pd.concat(genre_trends)

def train_prophet():
    """Train Prophet on top genres."""
    trends = prepare_trends_data()
    top_genres = trends.groupby('genre')['rating'].mean().nlargest(5).index
    
    models = {}
    for genre in top_genres:
        genre_data = trends[trends['genre'] == genre][['ds', 'rating']].rename(columns={'rating': 'y'})
        model = Prophet(yearly_seasonality=True, weekly_seasonality=False)
        model.fit(genre_data)
        models[genre] = model
    
    os.makedirs("models", exist_ok=True)
    joblib.dump(models, "models/prophet_models.pkl")
    return models

if __name__ == "__main__":
    train_prophet()
