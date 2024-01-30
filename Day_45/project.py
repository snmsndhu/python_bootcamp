import requests
from bs4 import BeautifulSoup

URL = ""

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_ = "title")

movie_titles = [movie.getText() for movie in all_movies]
# for n in range(len(movie_titles) -1, -1, -1):
#     print(movie_titles[n])
movies = movie_titles[::-1]

with open ("movie.txt", mode= "w") as file:
    for movie in movies:
        file.write(f"{movie}\n")