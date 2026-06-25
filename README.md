# Movie Recommend

Project scaffold for a movie recommendation system.

## Structure

- `data/` - dataset and resources
- `notebooks/` - exploratory notebooks
- `src/` - source code package
- `app.py` - application entry point
- `requirements.txt` - Python dependencies

🎬 4Cinephiles - AI Movie Recommendation System

A Movie Recommendation System built with Python, Streamlit, and Machine Learning. The application recommends similar movies using Content-Based Filtering and Cosine Similarity, while displaying movie posters and information through the TMDB API

✨ Features:

🎥 Recommend similar movies instantly
🤖 Content-Based Recommendation Engine
🎬 Movie posters using TMDB API
⭐ TMDB Ratings
📅 Release Date and Year
⏱ Runtime
🎭 Movie Genres
⚡ Fast and responsive Streamlit application

🛠 Tech Stack:

Programming Language-
Python

Libraries-
Streamlit
Pandas
NumPy
Scikit-learn
Requests
Python-dotenv

Machine Learning-
Content-Based Filtering
Cosine Similarity
Text Vectorization

Dataset-
TMDB 5000 Movies Dataset
TMDB 5000 Credits Dataset

API-
TMDB API

📂 Project Structure:

Movie-Recommend/
│
├── app.py
├── recommender.py
├── utils.py
├── ui.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   ├── moviesbanner.png
│   └── no_poster.png
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── model/
│   ├── movie_list.pkl
│   └── similarity.pkl
│
└── notebooks/
    └── Movie_Recommendation.ipynb

Run the application: streamlit run app.py

🧠 How It Works ??
1.User selects a movie.
2.The recommendation engine calculates similarity using cosine similarity.
3.Top 5 most similar movies are retrieved.
4.Posters and movie information are displayed using the TMDB API.

📈 Future Improvements:

* Improve TMDB API reliability to ensure posters load consistently for all recommended movies.
* Implement local poster caching to reduce API dependency and improve performance.
* Implement a Favorites feature.
* Add user authentication and personalized recommendations.
* Enhance search functionality with autocomplete suggestions.
* Improve overall UI responsiveness and accessibility.


👨‍💻 Author:
Abdus Sami