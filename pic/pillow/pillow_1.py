from PIL import Image
import numpy as np
import os

#tutorial
#http://pillow.readthedocs.io/en/4.3.x/handbook/tutorial.html

# 创建缩略图

size_1 = (600, 300)
size_2 = (300, 600)

infile = r"D:\\menu\\芒果汁1.jpg"
outfile = r"D:\\menu\\芒果汁1_thum.jpg"
try:
    # 创建缩略图
    im = Image.open(infile)

    if im.size[0] > im.size[1]:
        im.thumbnail(size_1)
    else:
        im.thumbnail(size_2)

    print(im.format, im.size, im.mode)

    # 创建300*300缩略图
    x_middle = im.size[0] / 2
    x_mid_left = int(x_middle - 150)
    x_mid_right = int(x_middle + 150)

    y_mid_up = int(im.size[1] / 2 - 150)
    y_mid_down = int(im.size[1] / 2 + 150)

    print(x_mid_left, y_mid_up, x_mid_right, y_mid_down)

    box = (x_mid_left, y_mid_up, x_mid_right, y_mid_down)
    region = im.crop(box)

    #图片旋转
    region = region.transpose(Image.ROTATE_180)
    im.paste(region, box)

    im.save(outfile, "JPEG")
except IOError:
    print("cannot create thumbnail for", infile)
