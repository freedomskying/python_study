# -*- coding: utf-8 -*-

import requests

# HTTP，基于“请求与响应”模式的、无状态的应用层协议。

# HTTP 协议对资源的操作：
# GET 请求获取URL位置的资源
# HEAD 获取URL的响应消息报告，的头部资源
# POST 请求向URL位置的资源后附加新的数据
# PUT 请求向URL位置存储一个资源，覆盖原URL位置的资源
# PATCH 请求局部更新URL位置的资源，即改变该处资源的部分内容
# DELETE 请求删除URL位置存储的资源

r = requests.head('http://httpbin.org/get')
print(r.headers)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

r = requests.post('http://httpbin.org/post', data='ABC')
print(r.text)
