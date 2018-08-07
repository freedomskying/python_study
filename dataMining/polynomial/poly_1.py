from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge

##样本数据(Xi,Yi)，需要转换成数组(列表)形式
Xi = np.array(
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]).reshape(-1,
                                                                                                                     1)
# Yi=np.array([9,18,31,48,69,94])
# Yi = np.array([9.1, 18.3, 32, 47, 69.5, 94.8]).reshape(-1, 1)

Yi = np.array(
    [1, 4, 9, 16, 9, 4, 1, -1, -4, -9, -16, -9, -4, -1, 11, 4, 9, 16, 9, 4, 1, -1, -4, -9, -16, -9, -4, -1]).reshape(-1,
                                                                                                                     1)

##这里指定使用岭回归作为基函数
model = make_pipeline(PolynomialFeatures(6), Ridge())
model.fit(Xi, Yi)
##根据模型预测结果
y_plot = model.predict(Xi)

##绘图
plt.scatter(Xi, Yi, color='red', label="样本数据", linewidth=2)
plt.plot(Xi, y_plot, color='green', label="拟合直线", linewidth=2)
plt.legend(loc='lower right')
plt.show()
