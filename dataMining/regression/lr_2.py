import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

a = 1
base_path = os.getcwd()
base_path = base_path[:base_path.find("python_study" + os.path.sep) + 13]
data_path = base_path + os.path.sep + "dataMining" + os.path.sep + "files" + os.path.sep + "regression" \
            + os.path.sep + "prices.txt"

# 读取数据集
datasets_X = []
datasets_Y = []
fr = open(data_path, 'r')
lines = fr.readlines()
for line in lines:
    items = line.strip().split(',')
    datasets_X.append(int(items[0]))
    datasets_Y.append(int(items[1]))

# 获取 X轴面积 Y轴价格
# test
length = len(datasets_X)

# 将X转换为二维数组，以符合线性回归拟合方程的需要
datasets_X = np.array(datasets_X).reshape([length, 1])
# 将Y转化为数组
datasets_Y = np.array(datasets_Y)

# 设置matplotlib.pyplot的X轴数据，以X的最大值和最小值为边界，建立等差数列
minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX, maxX).reshape([-1, 1])

# degree = 2 表示为2次多项式，然后创建线性回归，使用线性模型学习X_poly和datasets_Y之间的关系
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(datasets_X)
lin_reg_2 = linear_model.LinearRegression()
lin_reg_2.fit(X_poly, datasets_Y)

# 图像中显示
plt.scatter(datasets_X, datasets_Y, color='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
