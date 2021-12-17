import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
urls = []
url = ['https://www.kinopoisk.ru/lists/films/1/', 'https://www.kinopoisk.ru/lists/films/2/', 'https://www.kinopoisk.ru/lists/films/3/',
       'https://www.kinopoisk.ru/lists/films/4/', 'https://www.kinopoisk.ru/lists/films/5/', 'https://www.kinopoisk.ru/lists/films/6/',
       'https://www.kinopoisk.ru/lists/films/7/', 'https://www.kinopoisk.ru/lists/films/8/', 'https://www.kinopoisk.ru/lists/films/9/']
for a in url:
    response = requests.get(a, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    hrefs = soup.find_all('a', class_="film-lists-item", href=True)
    for href in hrefs:
        urls.append('https://www.kinopoisk.ru'+href['href'])
        print('https://www.kinopoisk.ru'+href['href'])

print('*******************')
for i in urls:
    print("'"+i+"', ", end='')