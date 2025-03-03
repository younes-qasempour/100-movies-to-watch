import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, 'html.parser')

title_elements = soup.find_all('h3', class_='title')
titles_text = [title.getText() for title in title_elements]
titles_ordered = titles_text[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles_ordered:
        file.write(title + "\n")