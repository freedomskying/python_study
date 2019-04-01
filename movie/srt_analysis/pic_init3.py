from PIL import Image
import pytesseract


def depoint(img):
    """传入二值化后的图片进行降噪"""
    pixdata = img.load()
    w, h = img.size
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:  # 上
                count = count + 1
            if pixdata[x, y + 1] > 245:  # 下
                count = count + 1
            if pixdata[x - 1, y] > 245:  # 左
                count = count + 1
            if pixdata[x + 1, y] > 245:  # 右
                count = count + 1
            if pixdata[x - 1, y - 1] > 245:  # 左上
                count = count + 1
            if pixdata[x - 1, y + 1] > 245:  # 左下
                count = count + 1
            if pixdata[x + 1, y - 1] > 245:  # 右上
                count = count + 1
            if pixdata[x + 1, y + 1] > 245:  # 右下
                count = count + 1
            if count > 4:
                pixdata[x, y] = 255
    return img


def binarizing(img, threshold):
    """传入image对象进行灰度、二值处理"""

    pixdata = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 255
            else:
                pixdata[x, y] = 0
    return img


if __name__ == '__main__':
    image_path = 'D:/test1.jpg'
    image = Image.open(image_path)

    img0 = image.convert("L")  # 转灰度
    img0.save(image_path.split('.')[0] + '-grey.jpg')

    img1 = binarizing(img0, 200)
    img1.save(image_path.split('.')[0] + '-bin.jpg')

    img2 = depoint(img1)
    img2.save(image_path.split('.')[0] + '-dep.jpg')

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img1, lang='chi_sim')

    print('test = ' + text)
