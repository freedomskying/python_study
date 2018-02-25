import sys, os
import numpy as np
from sklearn.cluster import KMeans


def loadData(file_path):
    fr = open(file_path, 'r+')
    lines = fr.readlines()
    retData = []
    retCityName = []
    for line in lines:
        items = line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1, len(items))])
    return retData, retCityName


if __name__ == '__main__':

    #获取聚类文件地址
    base_path = os.getcwd()
    base_path = base_path[:base_path.find("python_study\\") + 13]
    data, cityName = loadData(base_path + "dataMining\\files\\cluster\\city.txt")

    print(data)

    #使用KMeans算法进行聚类，聚类数为3，
    km = KMeans(n_clusters=3)
    #label为每条记录对应的聚类标签，该例中为城市对应的聚类标签（0,1,2）
    label = km.fit_predict(data)

    #km.cluster_centers_为聚类中心，如果为三类，则有三个聚类中心，对应着每一类数据每一个维度的欧氏距离平均值
    #np.sum，对聚类中心的点的各个维度的值进行求和，该例中表示对每个分类的聚类中心的各个维度值求和
    expenses = np.sum(km.cluster_centers_, axis=1)

    #print(km.cluster_centers_)
    # print(expenses)
    CityCluster = [[], [], []]
    for i in range(len(cityName)):
        CityCluster[label[i]].append(cityName[i])
    for i in range(len(CityCluster)):
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])
