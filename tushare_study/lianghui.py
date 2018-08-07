import tushare as ts
import pandas as pd
from pandas import DataFrame

stocks = ts.get_stock_basics()

# stocks.to_csv('stocks.csv', sep=',')

df = DataFrame()

for stock_code in stocks.index:
    stock_info = ts.get_hist_data(stock_code, '2017-02-26', '2017-03-03', 'D')
    df = pd.concat([df, stock_info], axis=0)

df.to_csv('stocks_trans.csv', sep=',')
