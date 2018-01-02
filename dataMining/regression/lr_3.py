import numpy as np
import os
from sklearn import model_selection
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

base_path = os.getcwd()
base_path = base_path[:base_path.find("python_study" + os.path.sep) + 13]
data_path = base_path + os.path.sep + "dataMining" + os.path.sep + "files" + os.path.sep + "regression" \
            + os.path.sep + "岭回归.csv"

data = np.genfromtxt(data_path, delimiter=',', skip_header=1, dtype=None)

plt.plot(data[:, 5])
plt.show()

# 用于保存0-3维数据
X = data[:, :5]

y = data[:, 5]

# 使用最高次的6次多项式特征，这个是多次试验后的结果
poly = PolynomialFeatures(6)

# X为创建后的多项式特征
X = poly.fit_transform(X)

# 将所有数据分为测试集与训练集，test_size表示测试集的比例，random_state是随机数种子
train_set_X, test_set_X, train_set_y, test_set_y = model_selection.train_test_split(X, y, test_size=0.3,
                                                                                    random_state=0)

# 创建岭回归实例，
# alpha表示正则化因子， 对应于损失函数中的a
# fit_intercept，表示是否计算截距
# solver，设置计算参数的方法，可选参数auto， svd， sag等
clf = Ridge(alpha=1.0, fit_intercept=True)

# 调用fit函数，使用训练集训练回归器
clf.fit(train_set_X, train_set_y)

# 利用测试集计算回归曲线的拟合优度，clf.score返回值为0.7375
# 拟合优度，用于评价拟合好坏，最大为1，无最小值，当对所有值都输出同一个值时，拟合优度为0
score = clf.score(test_set_X, test_set_y)

print(score)

start = 200
end = 400
y_pre = clf.predict(X)
time = np.arange(start, end)
plt.plot(time, y[start:end], 'b', label="real")
plt.plot(time, y_pre[start:end], 'r', label='predict')
plt.legend(loc='upper left')
plt.show()

