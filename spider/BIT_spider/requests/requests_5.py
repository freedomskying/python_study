# -*- coding: utf-8 -*-

import requests

kv = {'key1': 'value1', 'key2': 'value2'}

# params
r = requests.request('GET', 'http://python123.io/ws', params=kv)
print(r.url)

# data
r = requests.request('POST', 'http://python123.io/ws', data=kv)
print(r.url)

body = 'test'
r = requests.request('POST', 'http://python123.io/ws', data=body)
print(r.url)

# JSON
kv1 = {'key3': 'value3'}
r = requests.request('POST', 'http://python123.io/ws', json=kv1)
print(r.url)
