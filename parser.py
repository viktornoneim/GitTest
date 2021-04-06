# scraper.py
import requests
from bs4 import BeautifulSoup
# https://ok.ru/profile/587165486898
import time
import random

def parser_ok(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('h1', class_='p404_t')
    name = soup.find_all('a', class_='profile-user-info_name')

    # if quotes == [<h1 class='p404_t' tsid='page-not-found'>Этой страницы нет в OK</h1>]:
    # profile - user - info_name
    if len(quotes) > 0:
        # if quotes[0].text == 'Этой страницы нет в OK':
        #     print(quotes)
        print('-----' + url)
    else:
        if len(name) > 0:
            name = name[0].find('h1')
            img = soup.find_all(id='viewImageLinkId')
            if len(img) > 0:
                print(name.text + ' = ' + img[0]['src'])
            else:
                print(name.text + ' url === ' + url)

        else:
            print(url)


list_url = ['https://ok.ru/profile/5713870421210/', 'https://ok.ru/profile/587165486898/']
for id in range(587165486339, 587165486898):
    url = 'https://ok.ru/profile/%s/' % str(id)
    time.sleep(random.randint(1,3))
    parser_ok(url)

# от 587165486898-1000
# нашел 587165486131
# ошибка 587165486340
673
# до 587165486898