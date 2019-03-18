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
    time.sleep(round(random.uniform(2, 3), 2))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    cookies = {'cookie': 'll="108288"; bid=Ubx_Hih13O4; __yadk_uid=o84yXkt4E5gkM1CW5tfzYEnSXTmNE0z0; viewed="5344973"; gr_user_id=87a31d2b-cd1d-4a97-8d19-422e18b7e7d3; dbcl2="4604881:ZdXs/QM2GNw"; ck=7UOX; ap_v=0,6.0; __utmt=1; __utma=30149280.1917653763.1550369325.1550374142.1552915297.3; __utmb=30149280.7.10.1552915297; __utmc=30149280; __utmz=30149280.1550374142.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.460; __utma=223695111.1796498454.1550369353.1550369353.1552916017.2; __utmb=223695111.0.10.1552916017; __utmc=223695111; __utmz=223695111.1552916017.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1552916017%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fsource%3Dsuggest%26q%3D%25E6%2588%2591%25E4%25B8%258D%25E6%2598%25AF%25E8%258D%25AF%25E7%25A5%259E%22%5D; _pk_id.100001.4cf6=d6cae140ab83f8bc.1550369354.2.1552916017.1550369726.; _pk_ses.100001.4cf6=*; push_noty_num=0; push_doumail_num=0; _vwo_uuid_v2=D9BDEEEA8B7A4B59FEB43DB0DEE38A37B|34d3a50819382a2e5ddaf56f65cf0232'}  # 2018.7.25修改，
    res = requests.get(url, cookies=cookies, headers=headers)
    if res.status_code == 200:
        print("\n成功获取第{}个用户城市信息！".format(i))
    else:
        print("\n第{}个用户城市信息获取失败".format(i))
    pattern = re.compile('<div class="user-info">.*?<a href=".*?">(.*?)</a>', re.S)
    item = re.findall(pattern, res.text)  # list类型
    return item[0]  # 只有一个元素，所以直接返回


def get_content(movie_id, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    cookies = {
        'cookie': 'bid=GOOb4vXwNcc; douban-fav-remind=1; ps=y; ue="maplekonghou@163.com"; push_noty_num=0; push_doumail_num=0; ap=1; ll="108288"; dbcl2="181095881:BSb6IVAXxCI"; ck=Fd1S; ct=y'}

    # 获取热门的全部评论信息
    # https://movie.douban.com/subject/26683723/comments?start=20&limit=20&sort=new_score&status=P
    # 获取热门信息，percent_type h 好评 m 一般 l 差评
    # https://movie.douban.com/subject/26683723/comments?start=0&limit=20&sort=new_score&status=P&percent_type=h

    url = "https://movie.douban.com/subject/" + str(movie_id) + "/comments?start=" + str(
        page * 10) + "&limit=20&sort=new_score&status=P"
    res = requests.get(url, headers=headers, cookies=cookies)

    # 获取电影名称
    pattern = re.compile('<div id="wrapper">.*?<div id="content">.*?<h1>(.*?) 短评</h1>', re.S)
    global movie_name
    movie_name = re.findall(pattern, res.text)[0]  # list类型

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
    main(26683723, 5)  # 26752088    26366496  评论电影的ID号+要爬取的评论页面数
