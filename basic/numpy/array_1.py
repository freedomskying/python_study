import numpy as np

a = np.arange(10) ** 3

print(a)

print(a[2])

print(a[2:5])

# 相当于a[0:6:2]，从0开始到位置6结束，不包括位置6，每隔两个数字，第二个
a[:6:2] = -1000
print(a)

