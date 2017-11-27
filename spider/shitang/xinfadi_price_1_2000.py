# -*- coding: utf-8 -*-

# 导入requests库
from bs4 import BeautifulSoup

import requests
import bs4


def getHTMLText(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    try:
        r = requests.get(url, timeout=30, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fill_price_list(html, pfile):
    soup = BeautifulSoup(html, "html.parser")
    i = 0
    for tr in soup.find('table', class_='hq_table').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            if i == 0:
                i = i + 1
                continue
            i = i + 1
            pfile.write(tds[0].string + "," + tds[1].string + "," + tds[2].string + "," + tds[3].string + "," + tds[
                4].string + "," + tds[5].string + "," + tds[6].string + '\n')


def main():
    pfile = open('d:\\xinfadi_1_2000.csv', 'w', encoding='utf-8')

    for page_num in range(1, 3):
        url = 'http://www.xinfadi.com.cn/marketanalysis/0/list/' + str(page_num) + '.shtml'
        html = getHTMLText(url)
        fill_price_list(html, pfile)

    pfile.close()


main()
