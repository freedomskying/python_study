import numpy as np
from pandas import Series, DataFrame

a = np.random.randn(5)
print("a is an array:")
print(a)
s = Series(a)
print("s is a Series:")
print(s)

s = Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s.index)

# 添加name
s = Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'], name='my_series')
print(s)
print(s.name)

# Series还可以从字典（dict）创建：
d = {'a': 0., 'b': 1, 'c': 2}
print("d is a dict:")
print(d)
s = Series(d)
print("s is a Series:")
print(s)

s = Series(d, index=['b', 'c', 'd', 'a'])
print(s)

# 如果数据就是一个单一的变量，如数字4，那么Series将重复这个变量：
s = Series(4., index=['a', 'b', 'c', 'd', 'e'])
print(s)

# 访问Series数据可以和数组一样使用下标，也可以像字典一样使用索引，还可以使用一些条件过滤：
s = Series(np.random.randn(10), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(s[0])

print(s[:2])

print(s[[2, 0, 4]])

print(s[['e', 'i']])

print(s[s > 0.5])

print('e' in s)
