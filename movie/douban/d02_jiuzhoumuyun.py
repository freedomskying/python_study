# 爬取电影《我不是药神》的短评
import requests
from lxml import etree
from tqdm import tqdm
import time
import random
import pandas as pd
import re

name_list, content_list, date_list, score_list, city_list = [], [], [], [], []
movie_name = ""


def get_city(url, i):
    time.sleep(round(random.uniform(3, 7), 2))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    cookies = {
        'cookie': 'bid=8Pi-KEFBPg8; __yadk_uid=2l8sSjcAdFD0Yp1okiVMrbWmnDV1Sd1P; loc-last-index-location-id="108288"; ll="108288"; gr_user_id=a4e90ecf-4e9e-492c-a110-cfd02b16a52d; douban-fav-remind=1; ct=y; dbcl2="193625597:Olknt0R0avU"; ck=rnJq; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1552982109%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; ap_v=0,6.0; _pk_id.100001.4cf6=75e6351dc23bcd54.1552883214.7.1552982590.1552971538.; _pk_ses.100001.4cf6=*; __utma=30149280.755394970.1552883190.1552975276.1552981238.10; __utmb=30149280.11.10.1552981238; __utmc=30149280; __utmz=30149280.1552975276.9.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.19362; __utma=223695111.1745635151.1552883214.1552971538.1552982109.7; __utmb=223695111.0.10.1552982109; __utmc=223695111; __utmz=223695111.1552982109.7.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=D2307D86FF2E347BF938BBDDD851DFBBB|bb4d857776a850246a4f730aa85c95b9'}  # 2018.7.25修改，
    res = requests.get(url, cookies=cookies, headers=headers)
    if res.status_code == 200:
        print("\n成功获取第{}个用户城市信息！".format(i))
    else:
        print("\n第{}个用户城市信息获取失败".format(i))
    pattern = re.compile('<div class="user-info">.*?<a href=".*?">(.*?)</a>', re.S)

    try:
        item = re.findall(pattern, res.text)  # list类型
        return item[0]  # 只有一个元素，所以直接返回
    except OSError as err:
        print("OS error: {0}".format(err))
    else:
        print("number [%d] url [%s] is reject" % (i, url))

    return '被屏蔽了'


def get_content(movie_id, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'}
    cookies = {
        'cookie': 'll="108288"; bid=qiNaWXBOiJU; __utmz=30149280.1552971218.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); push_doumail_num=0; __utmv=30149280.460; push_noty_num=0; douban-profile-remind=1; _vwo_uuid_v2=D7845C2C2D7E248E98B7041486566020C|5f57cff2f508e39bfde24cb18e25fa09; __utma=30149280.916845649.1552971218.1552971218.1552983358.2; __utmc=30149280; __utmt=1; dbcl2="4604881:gSp/Z2J08d4"; ck=GwBk; ap_v=0,6.0; __utmb=30149280.5.10.1552983358; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1552983388%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fsource%3Dsuggest%26q%3D%25E4%25B9%259D%25E5%25B7%259E%22%5D; _pk_id.100001.4cf6=cbd06f3c38fc06b1.1552971291.2.1552983388.1552971325.; _pk_ses.100001.4cf6=*; __utma=223695111.1816338466.1552971292.1552971292.1552983389.2; __utmb=223695111.0.10.1552983389; __utmc=223695111; __utmz=223695111.1552983389.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search'}

    # 获取热门的全部评论信息
    # https://movie.douban.com/subject/26683723/comments?start=20&limit=20&sort=new_score&status=P
    # 获取热门信息，percent_type h 好评 m 一般 l 差评
    # https://movie.douban.com/subject/26683723/comments?start=0&limit=20&sort=new_score&status=P&percent_type=h

    url = "https://movie.douban.com/subject/" + str(movie_id) + "/comments?start=" + str(
        page * 20) + "&limit=20&sort=new_score&status=P"
    res = requests.get(url, headers=headers, cookies=cookies)

    # 获取电影名称
    pattern = re.compile('<div id="wrapper">.*?<div id="content">.*?<h1>(.*?) 短评</h1>', re.S)
    global movie_name
    movie_name = re.findall(pattern, res.text)[0]  # list类型

    try:
        movie_name = re.findall(pattern, res.text)[0]  # list类型
    except OSError as err:
        print("OS error: {0}".format(err))
    else:
        movie_name = '被屏蔽了'

    res.encoding = "utf-8"
    if res.status_code == 200:
        print("\n第{}页短评爬取成功！".format(page + 1))
        print(url)
    else:
        print("\n第{}页爬取失败！".format(page + 1))

    with open('html.html', 'w', encoding='utf-8') as f:
        f.write(res.text)
        f.close()
    x = etree.HTML(res.text)
    for i in range(1, 21):  # 每页20个评论用户
        name = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a/text()'.format(i))

        # 下面是个大bug，如果有的人没有评分，但是评论了，那么score解析出来是日期，而日期所在位置spen[3]为空
        score = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[2]/@title'.format(i))
        date = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[3]/@title'.format(i))
        m = '\d{4}-\d{2}-\d{2}'
        try:
            match = re.compile(m).match(score[0])
        except IndexError:
            break
        if match is not None:
            date = score
            score = ["null"]
        else:
            pass
        content = x.xpath('//*[@id="comments"]/div[{}]/div[2]/p/span/text()'.format(i))
        movie_id = x.xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a/@href'.format(i))

        try:
            city = get_city(movie_id[0], i)  # 调用评论用户的ID城市信息获取
        except IndexError:
            city = " "

        name_list.append(str(name[0]))
        score_list.append(str(score[0]).strip('[]\''))  # bug 有些人评论了文字，但是没有给出评分
        date_list.append(str(date[0]).strip('[\'').split(' ')[0])
        content_list.append(str(content[0]).strip())
        city_list.append(city)


def main(movie_id, pages):
    global movie_name
    for i in tqdm(range(0, pages)):  # 豆瓣只开放500条评论
        get_content(movie_id, i)  # 第一个参数是豆瓣电影对应的id序号，第二个参数是想爬取的评论页数
        time.sleep(round(random.uniform(3, 5), 2))
    infos = {'name': name_list, 'city': city_list, 'content': content_list, 'score': score_list, 'date': date_list}
    data = pd.DataFrame(infos, columns=['name', 'city', 'content', 'score', 'date'])
    data.to_csv(movie_name + ".csv")  # 存储名为  电影名.csv


if __name__ == '__main__':
    main(26322999, 5)  # 26752088    26366496  评论电影的ID号+要爬取的评论页面数
