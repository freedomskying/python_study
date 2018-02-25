import numpy as np
from pandas import Series, DataFrame
import pandas as pd

# 首先来看如何从字典创建DataFrame。DataFrame是一个二维的数据结构，
# 是多个Series的集合体。我们先创建一个值是Series的字典，并转换为DataFrame：
d = {'one': Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = DataFrame(d)
print(df)

df = DataFrame(d, index=['r', 'd', 'a'], columns=['two', 'three'])
print(df)

# 可以使用dataframe.index和dataframe.columns来查看DataFrame的行和列，dataframe.values则以数组的形式返回DataFrame的元素：
print("DataFrame index:")
print(df.index)
print("DataFrame columns:")
print(df.columns)
print("DataFrame values:")
print(df.values)

# DataFrame也可以从值是数组的字典创建，但是各个数组的长度需要相同：
d = {'one': [1., 2., 3., 4.], 'two': [4., 3., 2., 1.]}
df = DataFrame(d, index=['a', 'b', 'c', 'd'])
print(df)

# 值非数组时，没有这一限制，并且缺失值补成NaN：
d = [{'a': 1.6, 'b': 2}, {'a': 3, 'b': 6, 'c': 9}]
df = DataFrame(d)
print(df)

# 空 dataframe
df = DataFrame()
print(df)

# 另一种创建DataFrame的方法十分有用，那就是使用concat函数基于Serie或者DataFrame创建一个DataFrame
a = Series(range(5))
b = Series(np.linspace(4, 20, 5))
df = pd.concat([a, b], axis=1)
print(df)

df = DataFrame()
index = ['alpha', 'beta', 'gamma', 'delta', 'eta']
for i in range(5):
    a = DataFrame([np.linspace(i, 5 * i, 5)], index=[index[i]])
    df = pd.concat([df, a], axis=0)
print(df)

# 首先，再次强调一下DataFrame是以列作为操作的基础的，全部操作都想象成先从DataFrame里取一列，
# 再从这个Series取元素即可。可以用datafrae.column_name选取列，
# 也可以使用dataframe[]操作选取列，我们可以马上发现前一种方法只能选取一列，
# 而后一种方法可以选择多列。若DataFrame没有列名，[]可以使用非负整数，也就是“下标”选取列；
# 若有列名，则必须使用列名选取，另外datafrae.column_name在没有列名的时候是无效的：

print(df[1])
print(type(df[1]))
df.columns = ['a', 'b', 'c', 'd', 'e']
print(df['b'])
print(type(df['b']))
print(df.b)
print(type(df.b))
print(df[['a', 'd']])
print(type(df[['a', 'd']]))

# 以上代码使用了dataframe.columns为DataFrame赋列名，并且我们看到单独取一列出来，
# 其数据结构显示的是Series，取两列及两列以上的结果仍然是DataFrame。访问特定的元素可以如Series一样使用下标或者是索引:
print(df['b'][2])
print(df['b']['gamma'])

# 若需要选取行，可以使用dataframe.iloc按下标选取，或者使用dataframe.loc按索引选取：
print(df.iloc[1])
print(df.loc['beta'])

# 选取行还可以使用切片的方式或者是布尔类型的向量：
print("Selecting by slices:")
print(df[1:3])
bool_vec = [True, False, True, True, False]
print("Selecting by boolean vector:")
print(df[bool_vec])

# 行列组合起来选取数据：
print(df[['b', 'd']].iloc[[1, 3]])
print(df.iloc[[1, 3]][['b', 'd']])
print(df[['b', 'd']].loc[['beta', 'delta']])
print(df.loc[['beta', 'delta']][['b', 'd']])

# 如果不是需要访问特定行列，而只是某个特殊位置的元素的话，dataframe.at和dataframe.iat是最快的方式，
# 它们分别用于使用索引和下标进行访问：
print(df.iat[2, 3])
print(df.at['gamma', 'd'])

# dataframe.ix可以混合使用索引和下标进行访问，唯一需要注意的地方是行列内部需要一致，
# 不可以同时使用索引和标签访问行或者列，不然的话，将会得到意外的结果：
print(df.ix['gamma', 4])
print(df.ix[['delta', 'gamma'], [1, 4]])
print(df.ix[[1, 2], ['b', 'e']])
print("Unwanted result:")
print(df.ix[['beta', 2], ['b', 'e']])
print(df.ix[[1, 2], ['b', 4]])

# 为了看数据方便一些，我们设置一下输出屏幕的宽度
pd.set_option('display.width', 200)

dates = pd.date_range('20150101', periods=5)
print(dates)

# 将这个日期Series作为索引赋给一个DataFrame：
df = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))
print(df)

# 只要是能转换成Series的对象，都可以用于创建DataFrame：
df2 = pd.DataFrame({'A': 1., 'B': pd.Timestamp('20150214'), 'C': pd.Series(1.6, index=list(range(4)), dtype='float64'),
                    'D': np.array([4] * 4, dtype='int64'), 'E': 'hello pandas!'})
print(df2)
