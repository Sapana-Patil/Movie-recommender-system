import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pickle.load(open('movies.pkl', 'rb'))

tv = TfidfVectorizer(stop_words='english', max_features=5000)
vectors = tv.fit_transform(movies['tags'])
similarity = cosine_similarity(vectors)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),
                        reverse=True,
                        key=lambda x: x[1])[1:6]
    recommended = []
    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

st.title('🎬 Movie Recommendation System')

selected_movie = st.selectbox(
    'Select a movie you like!!',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader('Top 5 Recommendations:')
    for movie in recommendations:
        st.write('🎬', movie)