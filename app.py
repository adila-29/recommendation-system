import pickle
import streamlit as st
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])
     recommended_movies=[]
     recommended_poster=[]
     for i in movies_list[1:6]:
          movie_id = movies.iloc[i[0]].movie_id
          recommended_poster.append(fetch_poster(movie_id))
          recommended_movies.append(movies.iloc[i[0]].title)
     return recommended_movies,recommended_poster

movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=movies['title'].values
st.title('Movie Recomender ')
selected_movie = st.selectbox('Choose a Movie :', movies_list)
if st.button('Recommend'):
     movies, poster =recommend(selected_movie)
     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
          st.text(movies[0])
          st.image(poster[0])
     with col2:
          st.text(movies[1])
          st.image(poster[1])

     with col3:
          st.text(movies[2])
          st.image(poster[2])
     with col4:
          st.text(movies[3])
          st.image(poster[3])
     with col5:
          st.text(movies[4])
          st.image(poster[4])