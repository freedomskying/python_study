# -*- coding: utf-8 -*-

# 导入requests库
import requests

keyword = "Python"

try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params=kv)
    r.raise_for_status()

    print(r.url)
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
    print(len(r.text))
except:
    print("爬取失败")

