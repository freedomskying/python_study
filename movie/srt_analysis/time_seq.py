# coding=utf-8

import re

srt_path = r'D:\movie\Game of Thrones 2011 Season 1 S01\Game.of.Thrones.S01E01.srt'


# 获取人名清单
def name_list_init(exclude_url):
    exclude_d = {}
    with open(exclude_url) as exclude_file:
        for exclude_line in exclude_file:
            exclude_line = exclude_line.strip()
            exclude_line = exclude_line.lower()
            if exclude_line in exclude_d.keys():
                exclude_d[exclude_line] = exclude_d[exclude_line] + 1
            else:
                exclude_d[exclude_line] = 1

            exclude_list = exclude_line.split(' ')
            for exclude_list_name in exclude_list:
                exclude_list_name = exclude_list_name.lower()
                if exclude_list_name in exclude_d.keys():
                    exclude_d[exclude_list_name] = exclude_d[exclude_list_name] + 1
                else:
                    exclude_d[exclude_list_name] = 1
    return exclude_d


if __name__ == '__main__':
    name_list = name_list_init('name_list.txt')
    print(name_list)

    time_line = ''

    # 每一条字母的行数，条数-1， 时间-2， 中文-3，英文-4， 空格-5
    line_num = 0

    # 正则替换字符
    pattern = re.compile('<i>|</i>|[.,-<>?!]+|[.,-<>?!]+</i>')

    # 打开字幕文件，进行词频统计分析
    with open(srt_path) as f:

        for line in f.readlines():

            line_num = line_num + 1

            # if re.match('[0-9]+$', line):
            #     print('srt line %s', line.strip())

            if re.match('\d{2}:\d{2}:\d{2},\d{3}\s-->\s\d{2}:\d{2}:\d{2},\d{3}', line):
                # print('time line %s', line.strip())
                time_line = line.strip()

            # if line_num == 3:
            # print('Chinese srt is %s', line.strip())

            # 英文字幕，将每一行用
            if line_num == 4:
                # print('English srt is %s', re.sub(pattern, '', line.strip()))
                word_list = line.strip().split(' ')
                for word_str in word_list:
                    word_str = word_str.lower()
                    if word_str in name_list.keys():
                        print(time_line + ' ' + word_str)

            if len(line.strip()) == 0:
                line_num = 0
