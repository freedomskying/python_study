# -*- coding: utf-8 -*-

# 导入requests库
import requests

url = "https://www.amazon.cn/gp/product/B071SDP8PC/ref=amb_link_10?ie=UTF8&m=A1AJ19PSB66TGU&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-1&pf_rd_r=7ZPBARPAKPM7B9W5EW8H&pf_rd_r=7ZPBARPAKPM7B9W5EW8H&pf_rd_t=101&pf_rd_p=b9c6613d-af56-4edb-ad84-848bf4d9e2a7&pf_rd_p=b9c6613d-af56-4edb-ad84-848bf4d9e2a7&pf_rd_i=658390051"

try:
    kv = {'wd': ''}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print("爬取失败")
