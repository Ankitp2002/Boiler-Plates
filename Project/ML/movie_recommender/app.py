import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import numpy as np

st.title("🎬 Movie Recommender + Trend Predictor")

# Load models
@st.cache_resource
def load_models():
    rec = joblib.load("models/recommender.pkl")
    prophet_models = joblib.load("models/prophet_models.pkl")
    return rec, prophet_models

rec, prophet_models = load_models()

# User input
st.header("🔍 Get Movie Recommendations")
user_id = st.number_input("Your User ID (1-943)", 1, 943, 1)
liked_movie_title = st.selectbox("Liked this movie:", 
                                ["Toy Story (1995)", "Star Wars (1977)", "Titanic (1997)"])

# Find movie ID
movies = rec.movies
liked_movie_id = movies[movies['title'].str.contains(liked_movie_title.split('(')[0], case=False)]['movie_id'].iloc[0]

if st.button("🎯 Recommend Movies"):
    with st.spinner("Computing hybrid recommendations..."):
        recommendations = rec.hybrid_recommend(user_id, liked_movie_id, 10)
    
    st.subheader("✅ Top Recommendations")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"{i}. **{movie['title']}**")
        st.caption(movie['genres'])

# Trend predictions
st.header("📈 Genre Popularity Trends")
cols = st.columns(len(prophet_models))
for i, (genre, model) in enumerate(prophet_models.items()):
    with cols[i]:
        future = model.make_future_dataframe(periods=12, freq='MS')
        forecast = model.predict(future)
        fig = model.plot(forecast)
        st.plotly_chart(fig, use_container_width=True)

# Genre wordcloud
st.header("🌟 Most Popular Genres")
ratings = pd.read_csv('data/ml-100k/u.data', sep='\t', names=['user_id', 'movie_id', 'rating', 'timestamp'])
movies = pd.read_csv('data/ml-100k/u.item', sep='|', encoding='latin-1', usecols=[1] + list(range(5,24)))
wc = WordCloud(width=800, height=400).generate_from_frequencies(movies.iloc[:,1:].sum().to_dict())
fig, ax = plt.subplots()
ax.imshow(wc)
st.pyplot(fig)
