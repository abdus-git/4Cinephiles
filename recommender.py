import pickle

movies = pickle.load(open("model/movie_list.pkl","rb"))
similarity = pickle.load(open("model/similarity.pkl","rb"))

def  recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])

    recommended_movies = []
    recommended_movie_ids = []

    for i in movies_list[1:6]:
        movie = movies.iloc[i[0]]

        recommended_movies.append(movie.title)
        recommended_movie_ids.append(movie.movie_id)
    
    return recommended_movies, recommended_movie_ids