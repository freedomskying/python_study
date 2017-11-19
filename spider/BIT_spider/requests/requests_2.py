# -*- coding: utf-8 -*-

import requests

# r.status_code HTTP请求的返回状态，200表示联机成功，404表示失败
# r.text HTTP响应内容的字符串形式，即，url对应的页面内容
# r.encoding 从HTTP header种猜测的响应内容编码方式
# r.apparent_encoding 从内容分析出的响应内容编码方式（备选编码方式）
# r.content HTTP响应内容的二进制形式

r = requests.get("http://www.baidu.com")
r = requests.get("https://weibo.com/")

print(r.status_code)

print(r.encoding)
print(r.apparent_encoding)

r.encoding = r.apparent_encoding

print(r.text)
