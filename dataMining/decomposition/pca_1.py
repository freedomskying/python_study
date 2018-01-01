import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

#主成分分析PCA Pricipal Component Analysis

# 导入鸢尾花数据集
data = load_iris()
y = data.target
X = data.data

# 建立二维PCA模型
pca = PCA(n_components=2)

# 训练鸢尾花数据集，将原始数据进行降维
reduced_X = pca.fit_transform(X)

# 设定三类降维后的数据，并根据y值进行分类，显示不同的颜色
red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []

# 根据y值，将不同的数据添加到不同的现在颜色中
for i in range(len(reduced_X)):
    if y[i] == 0:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])

plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()
