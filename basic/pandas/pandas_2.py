import numpy as np
from pandas import Series, DataFrame
import pandas as pd
import tushare as ts

df = ts.get_hist_data('600848', start='2018-01-01', end='2018-01-05')

print(type(df))
print(df)

print(df.describe())

df.rename(columns={'date': 'dt'}, inplace=True)

print(df.index.name)

# 一种是按行列排序，即按照索引（行名）或者列名进行排序，可调用dataframe.sort_index，
# 指定axis=0表示按索引（行名）排序，axis=1表示按列名排序，并可指定升序或者降序
print("Order by column names, descending:")
print(df.sort_index(axis=1, ascending=False).head())

# 第二种排序是按值排序，可指定列名和排序方式，默认的是升序排序：

print("Order by column value, ascending:")
print(df.sort_values(by='open').head())

print("Order by multiple columns value:")
df = df.sort_values(by=['open', 'close'], ascending=[False, True])
print(df.head())

print(df.iloc[1:4][:])

# 我们可以扩展上篇介绍的使用布尔类型的向量获取数据的方法，可以很方便地过滤数据，例如，我们要选出收盘价在均值以上的数据：
print(df[df.close > df.close.mean()].head())

# isin()函数可方便地过滤DataFrame中的数据：

df = ts.get_index()

print(df[df['code'].isin(['000001', '000008', '000300'])].head())
print(df.shape)

# 原始数据的中很可能存在一些数据的缺失，就如同现在处理的这个样例数据一样，
# 处理缺失数据有多种方式。通常使用dataframe.dropna()，dataframe.dropna()可以按行丢弃带有nan的数据；
# 若指定how=‘all’（默认是’any’），则只在整行全部是nan时丢弃数据；
# 若指定thresh，则表示当某行数据非缺失列数超过指定数值时才保留；要指定根据某列丢弃可以通过subset完成。

print("Data size before filtering:")
print(df.shape)

print("Drop all rows that have any NaN values:")
print("Data size after filtering:")
print(df.dropna().shape)
print(df.dropna().head(10))

print("Drop only if all columns are NaN:")
print("Data size after filtering:")
print(df.dropna(how='all').shape)
print(df.dropna(how='all').head(10))

print("Drop rows who do not have at least six values that are not NaN")
print("Data size after filtering:")
print(df.dropna(thresh=6).shape)
print(df.dropna(thresh=6).head(10))

print("Drop only if NaN in specific column:")
print("Data size after filtering:")
print(df.dropna(subset=['close']).shape)
print(df.dropna(subset=['close']).head(10))

# 有数据缺失时也未必是全部丢弃，dataframe.fillna(value=value)可以指定填补缺失值的数值

print(df.fillna(value=20150101).head())

# Series和DataFrame的类函数提供了一些函数，如mean()、sum()等，指定0按列进行，指定1按行进行：

print('calculate mean value')
print(df.mean(0))

# value_counts函数可以方便地统计频数：
print('value_counts:')
print(df['close'].value_counts().head())

# 在panda中，Series可以调用map函数来对每个元素应用一个函数，
# DataFrame可以调用apply函数对每一列（行）应用一个函数，
# applymap对每个元素应用一个函数。这里面的函数可以是用户自定义的一个lambda函数，
# 也可以是已有的其他函数。下例展示了将收盘价调整到[0, 1]区间：
print('data standardization')
print(df[['close']].apply(lambda x: (x - x.min()) / (x.max() - x.min())).head())

# 使用append可以在Series后添加元素，以及在DataFrame尾部添加一行：

dat1 = df[['code', 'name', 'change']].head()
dat2 = df[['code', 'name', 'change']].iloc[2]
print("Before appending:")
print(dat1)
dat = dat1.append(dat2, ignore_index=True)
print("After appending:")
print(dat)

# DataFrame可以像在SQL中一样进行合并，在上篇中，我们介绍了使用concat函数创建DataFrame，
# 这就是一种合并的方式。另外一种方式使用merge函数，需要指定依照哪些列进行合并，
# 下例展示了如何根据security ID和交易日合并数据：
dat1 = df[['code', 'name', 'close']]
dat2 = df[['code', 'name', 'open']]
dat = dat1.merge(dat2, on=['code', 'name'])
print("The first DataFrame:")
print(dat1.head())
print("The second DataFrame:")
print(dat2.head())
print("Merged DataFrame:")
print(dat.head())

# DataFrame另一个强大的函数是groupby，可以十分方便地对数据分组处理，
# 我们对2015年一月内十支股票的开盘价，最高价，最低价，收盘价和成交量求平均值：
df_grp = df.groupby('code')
grp_mean = df_grp.mean()
print(grp_mean)
