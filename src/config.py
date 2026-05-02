import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "tmdb_movies.csv")

MOVIES_MODEL_PATH = os.path.join(BASE_DIR, "models", "movies.pkl")
SIMILARITY_MODEL_PATH = os.path.join(BASE_DIR, "models", "similarity.pkl")