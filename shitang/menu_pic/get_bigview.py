import pandas as pd
import requests
import re
import os
from PIL import Image


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
        for i in range(1):
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


def thum_pic(im_path):
    err_pic = Image.new("RGB", (300, 300))

    size_1 = (600, 300)
    size_2 = (300, 600)

    try:

        im = Image.open(im_path)
        # 创建缩略图
        if im.size[0] > im.size[1]:
            im.thumbnail(size_1)
        else:
            im.thumbnail(size_2)

        # 创建300*300缩略图
        x_middle = im.size[0] / 2
        x_mid_left = int(x_middle - 150)
        x_mid_right = int(x_middle + 150)

        y_mid_up = int(im.size[1] / 2 - 150)
        y_mid_down = int(im.size[1] / 2 + 150)

        box = (x_mid_left, y_mid_up, x_mid_right, y_mid_down)
        region = im.crop(box)

        # 图片旋转
        # region = region.transpose(Image.ROTATE_180)

    except IOError:
        print("cannot create thumbnail ")
        return err_pic

    return region


def main():
    df = pd.read_excel("d://menu.xlsx")

    im_big = Image.new("RGB", (df.shape[1] * 300, 10 * 300))

    for index, row in df.iterrows():

        col_num = 0
        for rowitem in row:
            if str(rowitem) != 'nan':
                search_pic(str(rowitem))
            origin_path = "d://menu_pic//" + str(rowitem) + "0.jpg"
            thum = thum_pic(origin_path)
            im_big.paste(thum, (col_num * 300, index * 300, (col_num + 1) * 300, (index + 1) * 300))

            print(col_num * 300, index * 300, (col_num + 1) * 300, (index + 1) * 300)
            col_num = col_num + 1

    im_big.save("d://menu_pic//big_view", "JPEG")


main()
