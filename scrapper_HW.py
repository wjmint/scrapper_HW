import requests
from bs4 import BeautifulSoup

# data = requests.get("https://store.steampowered.com/search/?specials=1")
# url = "https://store.steampowered.com/search/?specials=1"
# result = BeautifulSoup(data.text, 'html.parser')
# LIMIT = 50

# print(data.status_code)
# print(result)


# def section_extract():
#     data1 = requests.get(url)
#     steam_result = BeautifulSoup(data1.text, 'html.parser')
#     game_links = steam_result.find_all('a', {'class': 'serch_result_row'})
#     pages = []
#     for link in game_links:
#         pages.append(link.string)
#     return pages


def pagination_extract():
    url = requests.get("https://www.indeed.com/jobs?q=python&limit=50&start=400")
    result = BeautifulSoup(url.text, 'html.parser')
    pagination = result.find('div', {'class': 'pagination'})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    page = pages[-1]
    return page
    # print(result)
    print(page)
    # for game_title in pages:
    #     title = game_title.find('div', {'class': 'responsive_search_name_combined'})
    #     title2 = title.find('div', {'class': 'col'})
    #     title3 = title2.find('span', {'class': 'title'})
    #     print(title3)


pagination_extract()    