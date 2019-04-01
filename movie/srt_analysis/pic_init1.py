import cv2
import numpy as np


# 线降噪
def interference_line(img, img_name):
    filename = img_name.split('.')[0] + '-ifl.jpg'
    h, w = img.shape[:2]
    # opencv 矩阵点是反的
    # img[1, 2] 1-图像的高度， 2-图像的宽度
    for y in range(1, w - 1):
        for x in range(1, h - 1):
            count = 0
            print(img[x, y - 1])
            if img[x, y - 1] > 245:
                count = count + 1
            if img[x, y + 1] > 245:
                count = count + 1
            if img[x - 1, y] > 245:
                count = count + 1
            if img[x + 1, y] > 245:
                count = count + 1
            if count > 2:
                img[x, y] = 255
    cv2.imwrite(filename, img)


# 点降噪
def interference_point(img, img_name, x=0, y=0):
    """
    9邻域框,以当前点为中心的田字框,黑点个数
    :param img:
    :param img_name:
    :param x:
    :param y:
    :return:
    """

    filename = img_name.split('.')[0] + '-interference_point.jpg'

    # todo 判断图片的长度宽度下线

    cur_pixel = img[x, y]  # 当前像素点的值
    height, width = img.shape[:2]
    for y in range(0, width - 1):
        for x in range(0, height - 1):
            if y == 0:  # 第一行
                if x == 0:  # 左上顶点，4邻域
                    # 中心店旁边3个点
                    print(cur_pixel)
                    print(int(cur_pixel))
                    sum = int(cur_pixel) + int(img[x, y + 1]) + int(img[x + 1, y]) + int(img[x + 1, y + 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                elif x == height - 1:  # 左上顶点
                    sum = int(cur_pixel) + int(img[x, y + 1]) + int(img[x - 1, y]) + int(img[x - 1, y + 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                else:  # 最上非顶点6邻域
                    sum = int(img[x - 1, y]) + int(img[x - 1, y + 1]) + int(cur_pixel) + int(img[x, y + 1]) + int(
                        img[x + 1, y], int(img[x + 1, y + 1]))
                    if sum <= 3 * 245:
                        img[x, y] = 0
            elif y == width - 1:  # 最下面一行
                if x == 0:  # 左下顶点
                    # 中心点旁边3个点
                    sum = int(cur_pixel) + int(img[x + 1, y]) + int(img[x + 1, y - 1]) + int(img[x, y - 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                elif x == height - 1:  # 右下顶点
                    sum = int(cur_pixel) + int(img[x, y - 1]) + int(img[x - 1, y]) + int(img[x - 1, y - 1])
                    if sum <= 2 * 245:
                        img[x, y] = 0
                else:  # 最下非顶点6邻域
                    sum = int(cur_pixel) + int(img[x - 1, y]) + int(img[x + 1, y]) + int(img[x, y - 1]) + int(
                        img[x - 1, y - 1]) + int(img[x + 1, y - 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
            else:  # y不在边界
                if x == 0:  # 左边非顶点
                    sum = int(img[x, y - 1]) + int(cur_pixel) + int(img[x, y + 1]) + int(img[x + 1, y - 1]) + int(
                        img[x + 1, y]) + int(img[x + 1, y + 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
                elif x == height - 1:  # 右边非顶点
                    sum = int(img[x, y - 1]) + int(cur_pixel) + int(img[x, y + 1]) + int(img[x - 1, y - 1]) + int(
                        img[x - 1, y]) + int(img[x - 1, y + 1])
                    if sum <= 3 * 245:
                        img[x, y] = 0
                else:  # 具备9邻域条件的
                    sum = int(img[x - 1, y - 1]) + int(img[x - 1, y]) + int(img[x - 1, y + 1]) + int(
                        img[x, y - 1]) + int(cur_pixel) + int(img[x, y + 1]) + int(img[x + 1, y - 1]) + int(
                        img[x + 1, y]) + int(img[x + 1, y + 1])
                    if sum <= 4 * 245:
                        img[x, y] = 0
    cv2.imwrite(filename, img)


if __name__ == '__main__':
    file_name = "D:/test7.jpg"
    image = cv2.imread(file_name)
    kernal = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    # kernal = np.ones((5, 5), np.float32) / 25
    sharpened = cv2.filter2D(image, -1, kernal)
    cv2.imshow("sharpened", sharpened)
    cv2.waitKey()

    sharpened_path = file_name.split('.')[0] + '-sharp.jpg'
    print(sharpened_path)
    cv2.imwrite(sharpened_path, sharpened)
    interference_point(sharpened, sharpened_path)
