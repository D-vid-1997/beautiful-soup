from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')
movie_titles = soup.find_all(name='h3', class_='title')

reverse_movie_list = [movie.getText() for movie in movie_titles]

# My initial solution:

# with open('movies.txt', 'a', encoding='utf-8') as file:
#     for i in range(len(reverse_movie_list)):
#         file.write(f'{reverse_movie_list.pop()}\n')

# Alternate method:

movie_list = reverse_movie_list[::-1]

with open('movies.txt', 'w', encoding='utf-8') as file:
    for movie in movie_list:
        file.write(f'{movie}\n')
