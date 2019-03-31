import requests
import os

from PIL import Image


def image_download(url, root):
    """
    图片下载
    url web文件路径
    root 图片保存路径
    """
    # url = "http://image.nationalgeographic.com.cn/2017/1120/20171120022616448.jpg"
    # root = "d://pics//"

    # 文件保存路径
    path = root + url.split('/')[-1]

    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")


def get_image(image_path):
    """
    用Image获取图片文件
    :return: 图片文件
    """
    image = Image.open(image_path)
    return image


def image_grayscale_deal(image):
    """
    图片转灰度处理
    :param image:图片文件
    :return: 转灰度处理后的图片文件
    """
    image = image.convert('L')
    # 取消注释后可以看到处理后的图片效果
    # image.show()
    return image


def image_thresholding_method(image):
    """
    图片二值化处理
    :param image:转灰度处理后的图片文件
    :return: 二值化处理后的图片文件
    """
    # 阈值，控制二值化程度，自行调整（不能超过256）
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    # 图片二值化，此处第二个参数为数字一
    image = image.point(table, '1')
    # 取消注释后可以看到处理后的图片效果
    image.show()
    return image


# def captcha_tesserocr_crack(image):
#     """
#     图像识别
#     :param image: 二值化处理后的图片文件
#     :return: 识别结果
#     """
#     result = tesserocr.image_to_text(image)
#     return result


if __name__ == '__main__':
    # image_download()
    image = get_image(r'D:\test1.jpg')
    img1 = image_grayscale_deal(image)
    img2 = image_thresholding_method(img1)
    # print(captcha_tesserocr_crack(img2))
