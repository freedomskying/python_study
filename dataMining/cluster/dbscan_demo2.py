import numpy as np
import sklearn.cluster as skc
from sklearn import metrics
import matplotlib.pyplot as plt
import os

#这个例子不算太好，因为虽然使用了dbscan算法进行聚类，但是由于是对上网时间（几点钟）进行聚类，且eps设定为0.01所以，最后的聚类其实就是直方图。

mac2id = dict()
onlinetimes = []

base_path = os.getcwd()
base_path = base_path[:base_path.find("python_study\\") + 13]
file_path = base_path + "dataMining\\files\\cluster\\TestData.txt"

#学生月上网时间分布-TestData
f = open(file_path, encoding='utf-8')
for line in f:
    #读取每条记录中的mac地址、开始上网时间、上网时长
    mac = line.split(',')[2]
    onlinetime = int(line.split(',')[6])
    starttime = int(line.split(',')[4].split(' ')[1].split(':')[0])

    #查看MAC地址是否在MAC字典中，如果不在，则将MAC加入字典，MAC对应的value是加入时的顺序，从len(onlinetimes)中获取
    #这里做了一个假设，就是所有的学生在上网时，并不重复，不存在22点上网半小时，然后23点再上网半小时的情况
    #程序中，上网时长，如果发现一个id上网次数超过1次，会直接使用后一次覆盖前一次的上网时长。
    #onlinetimes数组是按照mac2id中mac对应的value作为下标，存储开始时间和上网时长。
    if mac not in mac2id:
        mac2id[mac] = len(onlinetimes)
        onlinetimes.append((starttime, onlinetime))
    else:
        onlinetimes[mac2id[mac]] = [(starttime, onlinetime)]
#print(mac2id)
#print(onlinetimes)

#将onlinetimes从元组数据类型reshape成为列表数据类型，存储在real_X中
#()代表元组，[]代表列表，{}代表字典
real_X = np.array(onlinetimes).reshape((-1, 2))

#以列表形式，获取上网时长，存入X中
X = np.log(1+real_X[:,1:])

#调用dbscan算法进行训练
#eps：两个样本被看做邻居节点的最大距离
#min_samples：簇的样本数
db = skc.DBSCAN(eps=0.14, min_samples=10).fit(X)
labels = db.labels_

#使用dbscan算法进行聚类后，会将异常点排除在外，在打印labels时会看到部分点的标签为-1，就是异常点。
print('Labels:')
print(labels)

#计算噪声数据的比例
raito = len(labels[labels[:] == -1]) / len(labels)
print('Noise raito:', format(raito, '.2%'))

#计算簇的个数，排除噪声后的簇的个数
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)
print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(X, labels))

#计算每个簇的个数、均值、标准差
for i in range(n_clusters_):
    print('Cluster ', i, ':')
    count = len(X[labels == i])
    mean = np.mean(real_X[labels == i][:,1])
    std = np.std(real_X[labels == i][:,1])
    print('\t number of sample: ', count)
    print('\t mean of sample: ', mean)
    print('\t std of sample: ', std)
