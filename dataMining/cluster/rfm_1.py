import pandas as pd
from sklearn.cluster import KMeans

import os

if __name__ == '__main__':
    base_path = os.getcwd()
    base_path = base_path[:base_path.find("python_study" + os.path.sep) + 13]

    data_path = base_path + os.path.sep + "dataMining" + os.path.sep + "files" + os.path.sep + "cluster" \
                + os.path.sep + "rfm.csv"

    data = pd.read_csv(data_path, encoding='gbk', parse_dates=[0], index_col=0)

    data_zs = 1.0 * (data - data.mean()) / data.std()

    print(data.mean)
    print(data.std)

    k = 5

    iteration = 100

    model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)

    model.fit(data_zs)

    r1 = pd.Series(model.labels_).value_counts()

    print(r1)
    r2 = pd.DataFrame(model.cluster_centers_)
    print(r2)

    r = pd.concat([r2, r1], axis=1)

    print(r)
    print(r.columns)
    print(data.columns)

    r.columns = list(data.columns) + [u'类别数目']

    print(r)
    print(model.labels_)
    print(pd.Series(model.labels_, index=data.index))

    r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)  # 输出每个会员对应的类别
    r.columns = list(data.columns) + [u'类别数目']

    print(r)