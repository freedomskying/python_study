# get_menu_image.py
import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"thumbURL\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print("")


def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def get_menu_list(file_path, menu_list):
    with open(file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            menu_list.append([line.strip()])


def main():
    # 获取菜单信息
    menu_list = []
    file_path = ""
    get_menu_list(file_path, menu_list)

    #获取图片
    start_url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='
    for i in range(len(menu_list)):
        try:
            url = start_url + menu_list[i]
            html = getHTMLText(url)
            parsePage(html)
        except:
            continue

main()
