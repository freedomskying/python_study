import numpy as np

a = np.arange(10) ** 3

print(a)

print(a[2])

print(a[2:5])

# 相当于a[0:6:2]，从0开始到位置6结束，不包括位置6，每隔两个数字，第二个
a[:6:2] = -1000
print(a)

# 利用’:'可以访问到某一维的全部数据，例如取矩阵中的指定列：
a = np.arange(20).reshape(4, 5)
print("a:")
print(a)
print("the 2nd and 4th column of a:")
print(a[:, [1, 3]])

# 稍微复杂一些，我们尝试取出满足某些条件的元素，这在数据的处理中十分常见，
# 通常用在单行单列上。下面这个例子是将第一列大于5的元素（10和15）对应的第三列元素（12和17）取出来：
print(a[0:2, 2])
print(a[:, 2])
print(a[:, 2][a[:, 0] > 5])
