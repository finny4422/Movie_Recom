import streamlit as st
import pickle
import pandas as pd
import numpy as np


def recommend(movie_name):
    movie_index = movies[movies["title"] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(enumerate(distances), reverse=True, key=(lambda x: x[1]))[1:6]
    l = []
    for i, j in movie_list:
        l.append(movies.iloc[i]["title"])
    return l


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommender System")
selected_movie = st.selectbox('Select the movie of your choice', movies["title"].values)

if st.button('Find Similar Movies'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)