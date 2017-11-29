# -*- coding:utf-8 -*-
import urllib
import requests
import json
import urllib2
import re
import os


class BaiduImage2(object):
    def __init__(self):
        super(BaiduImage2, self).__init__()
        print
        u'图片获取中,CTRL+C 退出程序...'
        self.page = 60  # 当前页数
        if not os.path.exists(r'./image'):
            os.mkdir(r'./image')

    def request(self):
        try:
            while 1:
                request_url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=%E7%BE%8E%E5%A5%B3&cg=girl&rn=60&pn=' + str(
                    self.page)
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
                           'Content-type': 'test/html'}
                # body = urllib.urlencode({'tn':'resultjsonavatarnew','ie':'utf-8','word':'%E7%BE%8E%E5%A5%B3','cg':'girl','pn':self.page,'rn':'60'})
                r = requests.get( request_url, headers=headers)
                # print r.status
                if r.status == 200:
                    data = r.read()

                    data = unicode(data, errors='ignore')
                    decode = json.loads(data)
                    self.download(decode['imgs'])

                self.page += 60
        except Exception:
            print("exception")

    def download(self, data):

        for d in data:
            # url = d['thumbURL']   缩略图  尺寸200
            # url = d['hoverURL']           尺寸360
            url = d['objURL']
            data = urllib2.urlopen(url).read()

            pattern = re.compile(r'.*/(.*?)\.jpg', re.S)
            item = re.findall(pattern, url)
            FileName = str('image/') + item[0] + str('.jpg')

            with open(FileName, 'wb') as f:
                f.write(data)


if __name__ == '__main__':
    bi = BaiduImage2()
    bi.request()
