import scipy.stats as stats
import pandas as pd
import numpy as np


def mono_bin(Y, X, n):

    good = Y.sum()
    bad = Y.count() - good
    r = 0
    while np.abs(r) < 1:
        d1 = pd.DataFrame({'X': X, 'Y': Y, 'Bucket': pd.qcut(X, n)})
        d2 = d1.groupby(['Bucket'])
        r, p = stats.spearmanr(d2['X'].mean(), d2['Y'].mean())
        n = n - 1
    # 同时得到了某个d2和n
    print(r, n)
    d3 = pd.DataFrame(d2['X'].min(), columns=['min'])
    d3['min'] = d2['X'].min()
    d3['max'] = d2['X'].max()
    d3['sum'] = d2['Y'].sum()
    d3['total'] = d2['Y'].count()
    d3['rate'] = d2['Y'].mean()
    d3['goodattribute'] = d3['sum'] / good
    d3['badattribute'] = (d3['total'] - d3['sum']) / bad
    d3['woe'] = np.log(d3['goodattribute'] / d3['badattribute'])
    iv = ((d3['goodattribute'] - d3['badattribute']) * d3['woe']).sum()
    d4 = d3.sort_values(by='min')
    woe = list(d4['woe'].values)
    print(d4)
    print('-' * 30)
    cut = []
    # float('inf') 为正无穷，而不是直接写inf
    cut.append(float('-inf'))
    for i in range(1, n + 1):
        qua = X.quantile(i / (n + 1))
        cut.append(round(qua, 4))
    cut.append(float('inf'))
    return d4, iv, woe, cut


train = pd.read_csv('data/cs-training.csv')
train = train.iloc[:, 1:]

# cut是对X取他的四分位，因为Y只有0  1  也不能取四分位。n=3因为最后有n-1，所以实际上是分成了四个桶，woe是四个值。goodattribute是好的属性的意思
dfx1, ivx1, woex1, cutx1 = mono_bin(train['SeriousDlqin2yrs'], train['RevolvingUtilizationOfUnsecuredLines'], n=10)
dfx2, ivx2, woex2, cutx2 = mono_bin(train['SeriousDlqin2yrs'], train['age'], n=10)
dfx4, ivx4, woex4, cutx4 = mono_bin(train['SeriousDlqin2yrs'], train['DebtRatio'], n=20)
dfx5, ivx5, woex5, cutx5 = mono_bin(train['SeriousDlqin2yrs'], train['MonthlyIncome'], n=10)
