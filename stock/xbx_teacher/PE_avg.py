# -*- coding: utf-8 -*-

import os
import pandas as pd
import tushare as ts

stock_code_list = ts.get_stock_basics()

for code in stock_code_list:
    if code[0] != '3':
        continue

    #计算净利润 PE_TTM = 总市值 /
    stock_code_list['net_income'] = stock_code_list['totalAssets']  / stock_code_list['pe']
