from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

best_movies_webpage = response.text
soup = BeautifulSoup(best_movies_webpage, 'html.parser')
movie_titles = soup.find_all(name='h3', class_='title')

reverse_movie_list = [movie.getText() for movie in movie_titles]
print(reverse_movie_list)

with open('movies.txt', 'a', encoding='utf-8') as file:
    for i in range(len(reverse_movie_list)):
        file.write(f'{reverse_movie_list.pop()}\n')
