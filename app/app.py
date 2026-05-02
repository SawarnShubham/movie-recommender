import streamlit as st
import pickle

# Load saved files
movies = pickle.load(open('models/movies.pkl', 'rb'))
similarity = pickle.load(open('models/similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"]
    
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

# UI
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    
    for movie in recommendations:
        st.write(movie)