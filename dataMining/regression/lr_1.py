import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
import os

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

length = len(datasets_X)
datasets_X = np.array(datasets_X).reshape([length, 1])
datasets_Y = np.array(datasets_Y)

minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX, maxX).reshape([-1, 1])

linear = linear_model.LinearRegression()
linear.fit(datasets_X, datasets_Y)

# 图像中显示
plt.scatter(datasets_X, datasets_Y, color='red')
plt.plot(X, linear.predict(X), color='blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
