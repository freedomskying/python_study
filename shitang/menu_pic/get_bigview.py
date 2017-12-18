import pandas as pd
import requests
import re
import os


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(html, pic_name):
    root = "D://menu_pic//"
    try:
        plt = re.findall(r'"objURL":"(.*?)"', html)
        for i in range(4):
            path = root + pic_name + str(i) + ".jpg"
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(plt[i])
                with open(path, 'wb') as f:
                    f.write(r.content)
                    r.close()

            print(plt[i])
    except Exception as err:
        print(err)


def search_pic(pic_name):
    # 获取图片
    start_url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='
    try:
        url = start_url + pic_name
        print(url)
        html = getHTMLText(url)
        parsePage(html, pic_name)
    except Exception as err:
        print(err)


def main():
    df = pd.read_excel("d:\\menu.xlsx")

    for index, row in df.iterrows():
        for rowitem in row:
            if str(rowitem) != 'nan':
                search_pic(str(rowitem))


main()
