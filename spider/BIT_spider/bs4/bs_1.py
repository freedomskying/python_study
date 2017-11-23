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
soup = BeautifulSoup(demo, "html.parser")

# print(soup.prettify())

# 标签打印
print(soup.title)
print(soup.a)
print(soup.a.string)
print(soup.a.name)
print(soup.a.parent.name)
print(soup.a.attrs)
print(soup.a.attrs['href'])
print(type(soup.a.attrs))
print(type(soup.a))
print(soup.p)
print(soup.b.string)

# 内容遍历
print(soup.head)
print(soup.head.contents)

print(soup.body)
print(soup.body.contents)
print(soup.body.contents[1])
print(len(soup.body.contents))

for child in soup.body.children:
    print(child)

# 标签上行遍历
print(soup.title.parent)

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

#标签平行遍历
print(soup.a.next_sibling)
print(soup.a.next_sibling.next_sibling)
print(soup.a.previous_sibling)
print(soup.a.previous_sibling.previous_sibling)
print(soup.a.parent)

for sibling in soup.a.next_siblings:
    print(sibling)

for sibling in soup.a.previous_siblings:
    print(sibling)