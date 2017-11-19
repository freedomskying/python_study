import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import os

# 读取文件
base_path = os.getcwd()
base_path = base_path[:base_path.find("python_study" + os.path.sep) + 13]

data_path = base_path + os.path.sep + "dataMining" + os.path.sep + "files" + os.path.sep + "classification" \
            + os.path.sep + "stock" + os.path.sep + "000777.csv"

data = pd.read_csv(data_path, encoding='gbk', parse_dates=[0], index_col=0)
data.sort_index(0, ascending=True, inplace=True)

# 选择5列作为特征：收盘价、最高价、最低价、开盘价、成交价
# day_feature：选取150天数据
# featurenum：5*150个特征
# x：记录5*150天个特征数据
# y：记录涨跌
day_feature = 150
featurenum = 5 * day_feature
x = np.zeros((data.shape[0] - day_feature, featurenum + 1))
y = np.zeros((data.shape[0] - day_feature))

for i in range(0, data.shape[0] - day_feature):
    #将收盘价、最高价、最低价、成交价放入x
    x[i, 0:featurenum] = np.array(data[i:i + day_feature] \
                                      [[u'收盘价', u'最高价', u'最低价', u'开盘价', u'成交量']]).reshape((1, featurenum))
    #最后一列记录开盘价
    x[i, featurenum] = data.ix[i + day_feature][u'开盘价']

#如果收盘价高于开盘价，则为涨，否则为跌
for i in range(0, data.shape[0] - day_feature):
    if data.ix[i + day_feature][u'收盘价'] >= data.ix[i + day_feature][u'开盘价']:
        y[i] = 1
    else:
        y[i] = 0

#创建SVM，并设置kernel参数，默认为rbf，其他有：linear，poly，sigmoid
clf = svm.SVC(kernel='rbf')
result = []

for i in range(5):
    # x和y的验证集和测试集，切分成80%-20%的测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    #训练数据
    clf.fit(x_train, y_train)

    #将预测数据与测试集的验证数据进行比对
    result.append(np.mean(y_test == clf.predict(x_test)))
print("svm classifier accuacy:")
print(result)
