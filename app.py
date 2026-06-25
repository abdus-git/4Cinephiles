import streamlit as st

from recommender import recommend
from utils import load_movies, fetch_poster
from ui import page_header,hero_banner, movie_card, footer

st.set_page_config(
    page_title="Movie Recommendation",
    page_icon="🎬",
    layout="wide"
)

## css
st.markdown("""
<style>

.stButton>button{
    background:#E50914;
    color:white;
    border-radius:12px;
    height:50px;
    width:180px;
    font-weight:bold;
    border:none;
    transition:0.3s;
}
.stButton > button:hover{
    background:#B20710;
}
div[data-baseweb="select"]{
    border-radius:10px;
}
img{
    border-radius:15px;
    object-fit:cover;
}
</style>
""", unsafe_allow_html=True)

movies = load_movies()
movies.columns = movies.columns.str.strip()

page_header()
hero_banner()

##sidebar
st.sidebar.title("🎬 Movie Recommendation")
st.sidebar.markdown("---")
st.sidebar.subheader("About")
st.sidebar.write(
    """
    4Cinephiles is an AI-powered Movie Recommendation System
    built using Content-Based Filtering.
    """
)
st.sidebar.markdown("---")
st.sidebar.subheader("Recommendation Method")
st.sidebar.success("Content-Based Filtering")

st.sidebar.markdown("---")
st.sidebar.subheader("Dataset")
st.sidebar.metric("Movies", len(movies))

st.sidebar.markdown("---")
st.sidebar.caption("Developed by Abdus ❤️")


st.markdown("""
<h3 style="color:white;">
🎥 Choose a Movie
</h3>
""", unsafe_allow_html=True)

selected_movie = st.selectbox(
    "",
    movies["title"].values
)

col1, col2, col3 = st.columns([2, 2, 1])

with col2:
    recommend_button = st.button("🎬 Recommend")

if recommend_button:

    with st.spinner("Finding similar movies... 🍿"):

        recommended_movies, recommended_movie_ids = recommend(selected_movie)

    st.markdown("""
    <h2 style="color:#E50914;">
    🍿 Recommended Movies
    </h2>
    """, unsafe_allow_html=True)

    cols = st.columns(5)

    for i in range(len(recommended_movies)):

        with cols[i]:

            poster = fetch_poster(recommended_movie_ids[i])

            if poster:
                st.image(
                    poster,
                    use_container_width=True)
            else:
                st.image(
                    "assets/no_poster.png", use_container_width=True)

            movie_info = movies[
                movies["movie_id"] == recommended_movie_ids[i]
            ].iloc[0]

            genres = movie_info["genres"]

            if isinstance(genres, list):
                genres = " • ".join(genres[:3])
            else:
                genres = str(genres)

            rating = movie_info["vote_average"]
            year = str(movie_info["release_date"][:4])
            runtime = movie_info["runtime"]

            movie_card(
            recommended_movies[i],
            genres,
            rating,
            year,
            runtime
            )

footer()