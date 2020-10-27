"""
Author: https://github.com/Romawechka
Python version 3.8.5
"""

import requests
from bs4 import BeautifulSoup as BS


if __name__ == "__main__":
    req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    xml = BS(req.content, 'lxml')

    for el in xml.findAll('valute'):

        Gon_dollar = str(el.find('name')).replace('/', '').replace('<name>', '')

        if Gon_dollar == 'Гонконгских долларов':
            value = str(el.find('value')).replace('/', '').replace('<value>', '')
            char = str(el.find('charcode')).replace('/', '').replace('<charcode>', '')

            print(f'1 {char} = {value} Rub')
            break

    inp = input('\nIf you want to exit enter any message or just close the application.\n')
    exit()