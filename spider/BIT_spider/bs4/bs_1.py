# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "https://python123.io/ws/demo.html"

try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
except:
    print("爬取失败")

demo = r.text
soup = BeautifulSoup(demo,"html.parser")

print(soup.prettify())