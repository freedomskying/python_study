import pandas as pd

"""
 pandas.read_html(io, match='.+', flavor=None, header=None, index_col=None, skiprows=None, attrs=None, parse_dates=False, tupleize_cols=None, thousands=', ', encoding=None, decimal='.', converters=None, na_values=None, keep_default_na=True, displayed_only=True)
 
 常用的参数：
 io:可以是url、html文本、本地文件等；
 flavor：解析器；
 header：标题行；
 skiprows：跳过的行；
 attrs：属性，比如 attrs = {'id': 'table'}；
 parse_dates：解析日
 
 URL说明：
 http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=i
 a：表示A股，把a替换为h，表示港股；把a替换为xsb，则表示新三板。那么，在网址分页for循环外部再加一个for循环，就可以爬取这三个股市的股票了。
"""

for i in range(1, 179):  # 爬取全部177页数据
    url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s' % (str(i))
    tb = pd.read_html(url)[3]  # 经观察发现所需表格是网页中第4个表格，故为[3]
    tb.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    print('第' + str(i) + '页抓取完成')
