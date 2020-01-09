import requests
from bs4 import BeautifulSoup

import json
import re

# I did it manually
r = requests.get('https://www.filmsite.org/top100filmquotes.html').text
soup = BeautifulSoup(r, 'html.parser')
span = soup.find('table')
tags = span.findAll('tr')

for i in tags:
    print(i)