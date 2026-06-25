import streamlit as st

def page_header():
    st.markdown("""
    <h1 style='text-align:center; font-size:55px;'>
        🎬 <span style='color:#c7161f;'>4</span><span style='color:#E50914;'>Cinephiles</span>
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h4 style='text-align:center; color:gray;'>
        Find your next favorite movie 🍿
    </h4>
    """, unsafe_allow_html=True)
    st.write("")

def hero_banner():
    st.markdown("""
    <div style="background: linear-gradient(90deg,#111,#1c1c1c,#111); padding:30px; border-radius:12px; text-align:center; margin-bottom:20px;">
        <h2 style="color:white;">
        Search Movies. Discover Your Next Favourite.</h2>
        <p style="color:#bbbbbb; font-size:18px;">Smarter movie discovery with AI-powered recommendations.</p>
    </div>
    """, unsafe_allow_html=True)

    st.image("assets/moviesbanner.png", use_container_width=True)
    st.write("")

def movie_card(title, genres, rating, year, runtime):
    st.markdown(f"""
    <div style="
        background:#1c1c1c; border-radius:15px; padding:12px; text-align:center; min-height:110px; box-shadow:0px 3px 8px rgba(0,0,0,0.3);
    ">
        <h4 style="color:white; margin-bottom:10px;">{title}</h4>
        <p style="color:#FFD700; font-size:16px;">⭐ {rating}</p>
        <p style="color:#BBBBBB;">📅 {year}</p>
        <p style="color:#BBBBBB;">⏱ {runtime} min</p>
        <span style="color:#E50914; font-size:15px;">🎭 {genres}</span>
    </div>
    """, unsafe_allow_html=True)

def footer():
    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; color:gray;">
        Made with ❤️ by Abdus
    </div>
    """, unsafe_allow_html=True)