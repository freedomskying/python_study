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


def get_content(movie_id, page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    cookies = {
        'cookie': 'bid=8Pi-KEFBPg8; dbcl2="4604881:ZdXs/QM2GNw"; ck=7UOX; loc-last-index-location-id="108288"; ll="108288"; gr_user_id=a4e90ecf-4e9e-492c-a110-cfd02b16a52d; douban-fav-remind=1; _vwo_uuid_v2=D2307D86FF2E347BF938BBDDD851DFBBB|bb4d857776a850246a4f730aa85c95b9; ap_v=0,6.0; __utma=30149280.755394970.1552883190.1552957454.1552962768.6; __utmc=30149280; __utmz=30149280.1552883190.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.460; push_noty_num=0; push_doumail_num=0'}

    # 获取热门的全部评论信息
    # https://movie.douban.com/subject/26683723/comments?start=20&limit=20&sort=new_score&status=P
    # 获取热门信息，percent_type h 好评 m 一般 l 差评
    # https://movie.douban.com/subject/26683723/comments?start=0&limit=20&sort=new_score&status=P&percent_type=h

    url = "https://movie.douban.com/subject/" + str(movie_id) + "/comments?start=" + str(
        page * 20) + "&limit=20&sort=new_score&status=P"
    res = requests.get(url, headers=headers, cookies=cookies)

    with open('html.html', 'w', encoding='utf-8') as f:
        f.write(res.text)
        f.close()

    # 获取电影名称
    pattern = re.compile('<div id="wrapper">.*?<div id="content">.*?<h1>(.*?) 短评</h1>', re.S)
    global movie_name
    print()
    movie_name = re.findall(pattern, res.text)[0]  # list类型

    res.encoding = "utf-8"
    if res.status_code == 200:
        print("\n第{}页短评爬取成功！".format(page + 1))
        print(url)
    else:
        print("\n第{}页爬取失败！".format(page + 1))


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
    main(26752088, 25)  # 26752088    26366496  评论电影的ID号+要爬取的评论页面数
