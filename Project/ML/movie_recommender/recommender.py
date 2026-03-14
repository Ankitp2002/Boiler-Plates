import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
import joblib
import os

class MovieRecommender:
    def __init__(self):
        self.cf_model = None
        self.tfidf = None
        self.movie_features = None
        self.similarity_matrix = None
        self.movie_title_map = {}
    
    def load_data(self):
        """Load ratings + movies."""
        ratings = pd.read_csv('data/ml-100k/u.data', sep='\t',
                            names=['user_id', 'movie_id', 'rating', 'timestamp'])
        movies = pd.read_csv('data/ml-100k/u.item', sep='|', encoding='latin-1',
                           names=['movie_id', 'title', 'release_date', 'video_release', 
                                  'imdb_url'] + [f'genre_{i}' for i in range(19)],
                           usecols=range(24))
        
        # Extract genres
        movies['genres'] = movies[[f'genre_{i}' for i in range(19)]].apply(
            lambda x: '|'.join(x[movies.columns.get_loc(col)] for col in movies.columns[5:] if x[col] == 1), axis=1
        )
        
        self.ratings = ratings
        self.movies = movies
        return ratings, movies
    
    def train_collaborative_filtering(self):
        """SVD collaborative filtering."""
        reader = Reader(rating_scale=(1, 5))
        data = Dataset.load_from_df(self.ratings[['user_id', 'movie_id', 'rating']], reader)
        trainset, testset = train_test_split(data, test_size=0.2)
        
        self.cf_model = SVD(n_factors=50, n_epochs=20, random_state=42)
        self.cf_model.fit(trainset)
        
        # Test RMSE
        predictions = self.cf_model.test(testset)
        rmse = np.sqrt(np.mean([p.est - p.r_ui**2 for p in predictions]))
        print(f"✅ CF RMSE: {rmse:.4f}")
    
    def train_content_based(self):
        """TF-IDF content similarity."""
        tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.movies['genres'])
        self.similarity_matrix = cosine_similarity(tfidf_matrix)
        self.tfidf = tfidf
        self.movie_features = pd.DataFrame(tfidf_matrix.toarray())
    
    def hybrid_recommend(self, user_id, movie_id, n_recommendations=10):
        """Hybrid: CF prediction + content similarity."""
        if self.cf_model is None or self.similarity_matrix is None:
            raise ValueError("Train models first!")
        
        # Collaborative filtering predictions
        user_movies = self.ratings[self.ratings['user_id'] == user_id]['movie_id'].unique()
        cf_scores = []
        
        for mid in self.movies['movie_id']:
            if mid not in user_movies:
                pred = self.cf_model.predict(user_id, mid).est
                cf_scores.append((mid, pred))
        
        cf_scores = sorted(cf_scores, key=lambda x: x[1], reverse=True)[:50]
        
        # Content boosting
        movie_idx = self.movies[self.movies['movie_id'] == movie_id].index[0]
        similar_idx = np.argsort(self.similarity_matrix[movie_idx])[::-1][1:51]
        
        hybrid_scores = {}
        for mid, cf_score in cf_scores:
            content_boost = self.similarity_matrix[movie_idx][self.movies[self.movies['movie_id'] == mid].index[0]]
            hybrid_scores[mid] = 0.7 * cf_score + 0.3 * content_boost
        
        top_recs = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]
        rec_movies = self.movies[self.movies['movie_id'].isin([mid for mid, _ in top_recs])][['title', 'genres']]
        
        return rec_movies.to_dict('records')

# Train and save
if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    rec = MovieRecommender()
    rec.load_data()
    rec.train_collaborative_filtering()
    rec.train_content_based()
    joblib.dump(rec, "models/recommender.pkl")
