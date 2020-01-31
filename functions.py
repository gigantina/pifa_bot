import requests
from bs4 import BeautifulSoup as BS
import random
from pyowm import OWM
import config

def parser():
    r = requests.get('https://ria.ru/')
    html = BS(r.content, 'html.parser')
    i = 0
    news = []
    for j in html.select('.cell-list__item'):
        i += 1
        if i <= 5:
            title = j.select('.cell-list__item-title')
            news.append(title[0].text)
        else:
            return news


def weather(gorod):
    API_key = config.PYOWN
    owm = OWM(API_key)
    try:
        obs = owm.weather_at_place(gorod)
        w = obs.get_weather()
        temperature = w.get_temperature('celsius')['temp']
        if temperature > 0:
            temp = 'Температура в г. {} равна {}{}°C'.format(gorod, '+', temperature)
        else:
            temp = 'Температура в г. {} равна {}°C'.format(gorod, temperature)
    except:
        temp = 'Такого города не существует'
    return temp


def orel():
    decision = random.choice(['Орел', 'Решка'])
    return decision


def simple(x):
    try:
        x = int(x)
        dividers = [str(i)  for i in range(1, x + 1) if x % i == 0]
        if len(dividers) > 2:
            dividers = ', '.join(dividers)
        else:
            dividers = 'Простое число'
    except:
        dividers = 'Это не число'
    return dividers