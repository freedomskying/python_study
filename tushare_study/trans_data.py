import tushare as ts

# 一次性获取全部日k线数据
dataset = ts.get_hist_data('600848')

print(dataset)

# 设定历史数据的时间：
dataset = ts.get_hist_data('600848', start='2017-01-05', end='2017-01-09')
print(dataset)

ts.get_hist_data('600848', ktype='W')  # 获取周k线数据
ts.get_hist_data('600848', ktype='M')  # 获取月k线数据
ts.get_hist_data('600848', ktype='5')  # 获取5分钟k线数据
ts.get_hist_data('600848', ktype='15')  # 获取15分钟k线数据
ts.get_hist_data('600848', ktype='30')  # 获取30分钟k线数据
ts.get_hist_data('600848', ktype='60')  # 获取60分钟k线数据
ts.get_hist_data('sh')  # 获取上证指数k线数据，其它参数与个股一致，下同
ts.get_hist_data('sz')  # 获取深圳成指k线数据
ts.get_hist_data('hs300')  # 获取沪深300指数k线数据
ts.get_hist_data('sz50')  # 获取上证50指数k线数据
ts.get_hist_data('zxb')  # 获取中小板指数k线数据
ts.get_hist_data('cyb')  # 获取创业板指数k线数据

# 获取复权数据
df = ts.get_stock_basics()
date = df.ix['600848']['timeToMarket']  # 上市日期YYYYMMDD

print(df)

ts.get_h_data('002337')  # 前复权
ts.get_h_data('002337', autype='hfq')  # 后复权
ts.get_h_data('002337', autype=None)  # 不复权
ts.get_h_data('002337', start='2015-01-01', end='2015-03-16')  # 两个日期之间的前复权数据

# 实时行情
ts.get_today_all()

'''
返回值说明：

code：代码
name:名称
changepercent:涨跌幅
trade:现价
open:开盘价
high:最高价
low:最低价
settlement:昨日收盘价
volume:成交量
turnoverratio:换手率
amount:成交量
per:市盈率
pb:市净率
mktcap:总市值
nmc:流通市值
'''

ts.get_h_data('399106', index=True)  # 深圳综合指数
