import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

title_elements = soup.find_all('h3', class_='title')
titles_text = [title.getText() for title in title_elements]
titles_ordered = [i for i in list(reversed(titles_text))]

with open("list.txt", "w", encoding="utf-8") as file:
    for title in titles_ordered:
        file.write(title + "\n")