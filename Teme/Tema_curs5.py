import requests
from bs4 import BeautifulSoup

URL = 'https://ratings.fide.com/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)

table = soup.find(id='search_results')
print(table)

table_r = table.find(id='top_rating_div')
print(table_r)

# games_title = game_gallery.find_all(class_='game-box')
# print(games_title)


