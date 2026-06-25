import streamlit as st
import os
import pickle
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

@st.cache_data
def load_movies():
    return pickle.load(open("model/movie_list.pkl", "rb"))

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):

    url = (
        f"https://api.themoviedb.org/3/movie/{movie_id}"
        f"?api_key={API_KEY}&language=en-US"
    )
    try:
        response = requests.get(url,timeout=10)
        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return BASE_IMAGE_URL + poster_path

    except requests.exceptions.RequestException:
        pass
    

    return None