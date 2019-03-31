# coding=utf-8

import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

r'''
C:\Users\wkxt\Desktop\字幕\权力的游戏\01.简体&英文.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E01.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E02.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E03.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E04.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E05.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E06.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E07.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E08.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E09.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E10.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt
'''
srt_path = r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E10.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt'

file_path_list = [
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E01.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E02.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E03.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E04.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E05.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E06.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E07.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E08.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E09.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
    r'C:\Users\wkxt\Desktop\字幕\权力的游戏\Game_of_Thrones_S01_BD_Subs_Freesand\Game.of.Thrones.S01E10.1080p.BluRay.x264.DTS-WiKi.Freesand.chs&eng.srt',
]

background_path = r'C:\Users\wkxt\Desktop\字幕\权力的游戏\xuzheng.jpg'

'''
第一个周，帮你们做权游的分析，针对有现成字幕的情况，第二个周，帮你们做九州的分析，针对没有字幕，需要从视频里边提取字幕的情况
然后针对九州，我需要你们提供一个词典，如果你们先需要人物的分析，那么就给我一个词典，包括九州所有的人名
分析的内容，只针对字幕来说，第一个是字幕的各种词出现的频率，第二个是每个人物在字幕中出现的时间
第三个周开始，会做图像识别，把视频变成图片，比如1秒钟截取一张图片，那么40分钟的一集，就是60秒 * 40分钟  = 2400张图片，然后从这些图片中，再提取每张图片是否出现了某个人
然后就能回答，视频中，某个人什么时候出现，或者比如说，在第1、4、6、12分钟出现，每集出现的时间占比，然后还有你说的事件，我理解就是某两个人同时出现，比如小囧脸和异鬼同时出现在画面
我能做的是，把视频变成图片，然后识别图片里边是不是有人，目前不好做的是，这个人是龙马，还是小囧脸，这个有难度，而且几个人同时出现在同一个图片，如何进行识别，其实也有难度
等我做视频的时候，我会先找一个人物进行试验，比如在网上找好几百张小囧脸的图片，让计算机认识图片的人是小囧脸，然后再看权游的所有图片，哪些图片有小囧脸

'''

count_dict = {}


# 词频统计分析函数
def wordcount(line_str):
    # 文章字符串前期处理
    str_list = line_str.replace('\n', '').lower().split(' ')

    global count_dict

    # 如果字典里有该单词则加1，否则添加入字典
    for line_str in str_list:
        if line_str not in exclude_dict.keys():
            if line_str in count_dict.keys():
                count_dict[line_str] = count_dict[line_str] + 1
            else:
                count_dict[line_str] = 1


# 过滤单词
def exclude_word_init(exclude_url):
    exclude_d = {}
    with open(exclude_url) as exclude_file:
        for exclude_line in exclude_file:
            exclude_line = exclude_line.strip()
            if exclude_line in exclude_d.keys():
                exclude_d[exclude_line] = exclude_d[exclude_line] + 1
            else:
                exclude_d[exclude_line] = 1
    return exclude_d


if __name__ == '__main__':

    line_num = 0

    # 正则替换字符
    pattern = re.compile('<i>|</i>|[.,-<>?!]+|[.,-<>?!]+</i>')

    exclude_dict = exclude_word_init(r'C:\Users\wkxt\Desktop\字幕\权力的游戏\exclude.txt')

    print(exclude_dict)

    # 打开字幕文件，进行词频统计分析
    with open(srt_path) as f:

        for line in f.readlines():

            line_num = line_num + 1

            # if re.match('[0-9]+$', line):
            #     print('srt line %s', line.strip())
            # elif re.match('\d{2}:\d{2}:\d{2},\d{3}\s-->\s\d{2}:\d{2}:\d{2},\d{3}', line):
            #     print('time line %s', line.strip())

            # if line_num == 3:
            # print('Chinese srt is %s', line.strip())
            if line_num == 4:
                # print('English srt is %s', re.sub(pattern, '', line.strip()))
                wordcount(re.sub(pattern, '', line.strip()))

            if len(line.strip()) == 0:
                line_num = 0

    # 按照词频从高到低排列
    count_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    print(count_list)

    f_w = open('test.txt', 'w')  # 若是'wb'就表示写二进制文件

    for file_path in file_path_list:
        print(file_path)
        with open(file_path) as f:

            line_num = 0

            for line in f.readlines():
                line_num = line_num + 1

                if line_num == 4:
                    # print('English srt is %s', re.sub(pattern, '', line.strip()))
                    f_w.write(line.strip() + ' ')

                if len(line.strip()) == 0:
                    line_num = 0

    f_w.close()

    # 屏蔽词
    stopwords = STOPWORDS.copy()
    with open(r'C:\Users\wkxt\Desktop\字幕\权力的游戏\exclude.txt', 'r') as f:
        for i in f.readlines():
            stopwords.add(i.strip())
        f.close()

    # 设置背景图
    background_image = plt.imread(background_path)

    with open('test.txt', 'r') as f_r:
        text = f_r.read()
        word_cloud = WordCloud(width=1024, height=768, background_color='white', mask=background_image,
                               stopwords=stopwords, max_font_size=400,
                               random_state=50)
        word_cloud.generate_from_text(text)
        img_colors = ImageColorGenerator(background_image)
        word_cloud.recolor(color_func=img_colors)
        plt.imshow(word_cloud)
        plt.axis("off")
        plt.show()

    # max_font_size设定生成词云中的文字最大大小
    # width,height,margin可以设置图片属性
    # generate 可以对全部文本进行自动分词,但是他对中文支持不好
    # wordcloud = WordCloud(max_font_size=66).generate(text)
    # plt.figure()
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

    # pil方式展示生成的词云图像（如果你没有matplotlib）
    # image = wordcloud.to_image()
    # image.show()
