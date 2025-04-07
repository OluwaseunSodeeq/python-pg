import requests
from bs4 import BeautifulSoup


response =  requests.get("https://news.ycombinator.com/news")
yc_news = response.text

soup = BeautifulSoup(yc_news, "html.parser")
print(soup.title.string)
# print(soup.prettify())

article_tag = soup.find_all(name="a", class_="titlelink")
# article_tag = soup.find_all(name="a", class_="storylink")
for article in article_tag:
    article_text = article_tag.tag.getText()
    article_link = article_tag.tag.get("href")
    print(article_text)
    print(article_link)

print(article_tag)


movies_response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_response.raise_for_status()
movies_web_page = movies_response.text
soup = BeautifulSoup(movies_web_page, "html.parser")
all_movies_tittles = soup.find_all(name="h3", class_="title")

movies_title = [movie.get() for movie in all_movies_tittles]
print(movies_title)
for n in range(len(movies_title)-1, 0, -1):
    print(movies_title[n])

print(movies_title[::-1])

with open("movies.txt", "w") as file:
    for movie in movies_title:
        file.write(f"{movie}\n")