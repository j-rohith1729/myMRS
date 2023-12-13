import pickle
import pandas as pd
import streamlit as st


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    # recommended_movies_posters = []
    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
        # recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies


movies_list=pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity=pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    for i in names:
        st.write(i)
