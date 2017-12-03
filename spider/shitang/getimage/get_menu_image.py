# get_menu_image.py
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
    root = "D://menu//"
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


def get_menu_list(file_path, menu_list):
    with open(file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            menu_list.append([line.strip()])


def main():
    # 获取菜单信息
    menu_list = []
    file_path = "d:\\menu.txt"
    get_menu_list(file_path, menu_list)

    # 获取图片
    start_url = 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word='
    for i in range(len(menu_list)):
        try:
            url = start_url + menu_list[i][0]
            print(url)
            html = getHTMLText(url)
            parsePage(html, menu_list[i][0])
        except Exception as err:
            print(err)
            continue


main()
