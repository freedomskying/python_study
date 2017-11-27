# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
import re
import bs4


def getHTMLText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "省份"))
    for i in range(num):
        u = ulist[i]
        #print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
        print(str(u[0]) + str(u[1]) + str(u[2]))
    print("Suc" + str(num))


if __name__ == "__main__":
    print("start")
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html"
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 university
