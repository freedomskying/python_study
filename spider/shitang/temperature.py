# -*- coding: utf-8 -*-

import requests #导入requests库
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}

months = ['201601','201602','201603','201604','201605','201606','201607','201608','201609','201610','201611','201612','201701','201702','201703','201704','201705','201706','201707']

file_xinfadi = open('d:\\temp_beijing.csv','w')

for month_num in months:
    print(month_num)    
    
    url_address = 'http://lishi.tianqi.com/beijing/'+month_num+'.html'
    
    r = requests.get(url_address,headers = headers) #像目标url地址发送get请求，返回一个response对象
    
    hq_table = BeautifulSoup(r.text, 'lxml').find_all('div', class_='tqtongji2')  #获取网页中的class为cV68d的所有a标签
    
    
    file_xinfadi.write(str(hq_table) + '\r\n')
        
file_xinfadi.close()        