# -*- coding: utf-8 -*-

# 导入requests库
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

file_xinfadi = open('d:\\xinfadi_1_2000.csv', 'w', encoding='utf-8')

for page_num in range(1, 2):

    url_address = 'http://www.xinfadi.com.cn/marketanalysis/0/list/' + str(page_num) + '.shtml'
    r = requests.get(url_address, headers=headers)  # 像目标url地址发送get请求，返回一个response对象
    r.encoding = r.apparent_encoding
    print(r.encoding)

    #print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')
    hq_table = soup.find_all('table', class_='hq_table')  # 获取网页中的class为hq_table的所有a标签

    #file_xinfadi.write(str(hq_table) + '\r\n')
    print(str(hq_table))

file_xinfadi.close()
