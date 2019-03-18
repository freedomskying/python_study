from datetime import time
from random import random

import requests

page = 1
id = 26752088

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
cookies = {
    'cookie': 'll="108288"; bid=8Pi-KEFBPg8; __utmt=1; dbcl2="4604881:ZdXs/QM2GNw"; ck=7UOX; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1552883214%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; __yadk_uid=2l8sSjcAdFD0Yp1okiVMrbWmnDV1Sd1P; _pk_id.100001.4cf6=75e6351dc23bcd54.1552883214.1.1552883232.1552883214.; _pk_ses.100001.4cf6=*; __utma=30149280.755394970.1552883190.1552883190.1552883190.1; __utmb=30149280.3.10.1552883190; __utmc=30149280; __utmz=30149280.1552883190.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.460; __utma=223695111.1745635151.1552883214.1552883214.1552883214.1; __utmb=223695111.0.10.1552883214; __utmc=223695111; __utmz=223695111.1552883214.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=D2307D86FF2E347BF938BBDDD851DFBBB|bb4d857776a850246a4f730aa85c95b9'}
url = "https://movie.douban.com/subject/" + str(id) + "/comments?start=" + str(
    page * 20) + "&limit=20&sort=new_score&status=P"

print(url)
res = requests.get(url, headers=headers, cookies=cookies)
res.encoding = "utf-8"
if res.status_code == 200:
    print("\n第{}页短评爬取成功！".format(page + 1))
    print(url)
else:
    print("\n第{}页爬取失败！".format(page + 1))

time.sleep(round(random.uniform(1, 2), 2))
