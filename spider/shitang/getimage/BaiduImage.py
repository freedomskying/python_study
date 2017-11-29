# -*- coding:utf-8 -*-
import httplib
import urllib
import json
import urllib2
import re
import os


class BaiduImage(object):
    def __init__(self):
        super(BaiduImage, self).__init__()
        print
        u'图片获取中,CTRL+C 退出程序...'
        self.page = 60  # 当前页数

    def request(self):
        while 1:
            conn = httplib.HTTPConnection('image.baidu.com')
            request_url = '/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&cg=girl&rn=60&pn=' + str(
                self.page)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
                       'Content-type': 'test/html'}

            conn.request('GET', request_url, headers=headers)
            r = conn.getresponse()
            print
            r.status
            self.page += 60


if __name__ == '__main__':
    bi = BaiduImage()
    bi.request()  