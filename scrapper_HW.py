import requests
from bs4 import BeautifulSoup

data = requests.get("https://store.steampowered.com/search/?specials=1")
steamsale_result = BeautifulSoup(data.text, 'html.parser')

# print(data.status_code)
# print(steamsale_result)

def section_extract():
    title = []
    result = requests.get(data.text, 'html.parser')
    gamesection = result.find("div", {'class' : 'responsive_search_name_combined'})
    names = gamesection.find_all("span", {'class' : 'title'})
    for name in names:
        title.append(name.string)
    return title

def title_extract():
    title = []
    result = requests.get(f"{url}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, 'html.parser')
    game_title = soup.find_all("div", {'class' : 'col search_name ellipsis'})

    for game_t in game_title:
        title = game_t.find('span', {'class' : 'title'})
    return title

section = section_extract()
title = title_extract()
print(section_extract())