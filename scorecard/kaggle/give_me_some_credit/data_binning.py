import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series


# 最优分箱
def mono_bin(Y, X, n):
    # 设置DataFrame调用head时，能够打印所有的列
    pd.set_option('display.max_columns', None)
    # 设置DataFrame调用head时，一行打印所有列，不换行
    pd.set_option('expand_frame_repr', False)

    # 获取好客户数量
    good = Y.sum()
    # 获取坏客户数量
    bad = Y.count() - good

    r = 0
    # 使用pandas的qcut进行分箱，同时使用spearman相关系数与显著性系数，判断分箱是否成功。
    # 该端程序选择相关系数为1，完全相关的分箱，作为某一列变量的分享结果。
    while np.abs(r) < 1:
        # 第一列是好坏客户，第二列是分箱列，第三列是对应的分箱区间
        d1 = pd.DataFrame({'X': X, 'Y': Y, 'Bucket': pd.qcut(X, n)})

        # 按照分箱区间，进行groupby汇总
        d2 = d1.groupby(['Bucket'])

        # 计算spearman相关系数
        # r 相关系数，X与Y的相关性
        # p 显著性系数，相关是否显著，p小于0.01则发生概率为99%，如果0.01<p<0.05，则发生概率为95%
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


def self_bin(Y, X, cat):
    # 获取好客户数量
    good = Y.sum()
    # 获取坏客户数量
    bad = Y.count() - good

    # X列为好坏客户判断，Y为需要分箱的列，Bucket
    d1 = pd.DataFrame({'X': X, 'Y': Y, 'Bucket': pd.cut(X, cat)})
    d2 = d1.groupby(['Bucket'])
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
    print(d4)
    print('-' * 40)
    woe = list(d3['woe'].values)
    return d4, iv, woe


# 对于每一列，将值映射到分箱，然后根据分箱获取woe，然后返回对应列的woe值，用于后续建模使用。
def replace_woe(series, cut, woe):
    # woe返回列表，最后的返回值，
    list = []
    i = 0

    # 对于列表中的每一个至，计算该值所在的分箱，然后获取WOE值
    while i < len(series):
        # 每一行的值
        value_k = series[i]

        # 分箱的值的长度，一般比如分3三箱，则有4个值，减2，作为坐标，0、1、2
        j = len(cut) - 2
        m = len(cut) - 2

        # 寻找第一个满足分箱的值，赋值woe
        while j >= 0:
            if value_k >= cut[j]:
                j = -1
            else:
                j -= 1
                m -= 1
        list.append(woe[m])
        i += 1
    return list


if __name__ == '__main__':
    # 获取文件
    train = pd.read_csv('data/TrainData.csv')
    test = pd.read_csv('data/TestData.csv')

    # cut是对X取他的四分位，因为Y只有0  1  也不能取四分位。n=3因为最后有n-1，所以实际上是分成了四个桶，woe是四个值。
    # goodattribute是好的属性的意思
    dfx1, ivx1, woex1, cutx1 = mono_bin(train['SeriousDlqin2yrs'], train['RevolvingUtilizationOfUnsecuredLines'], n=10)
    dfx2, ivx2, woex2, cutx2 = mono_bin(train['SeriousDlqin2yrs'], train['age'], n=10)
    dfx4, ivx4, woex4, cutx4 = mono_bin(train['SeriousDlqin2yrs'], train['DebtRatio'], n=20)
    dfx5, ivx5, woex5, cutx5 = mono_bin(train['SeriousDlqin2yrs'], train['MonthlyIncome'], n=10)

    # 非最优分箱
    ninf = float('-inf')
    pinf = float('inf')
    cutx3 = [ninf, 0, 1, 3, 5, pinf]
    cutx6 = [ninf, 1, 2, 3, 5, pinf]
    cutx7 = [ninf, 0, 1, 3, 5, pinf]
    cutx8 = [ninf, 0, 1, 2, 3, pinf]
    cutx9 = [ninf, 0, 1, 3, pinf]
    cutx10 = [ninf, 0, 1, 2, 3, 5, pinf]

    dfx3, ivx3, woex3 = self_bin(train['SeriousDlqin2yrs'], train['NumberOfTime30-59DaysPastDueNotWorse'], cutx3)
    dfx6, ivx6, woex6 = self_bin(train['SeriousDlqin2yrs'], train['NumberOfOpenCreditLinesAndLoans'], cutx6)
    dfx7, ivx7, woex7 = self_bin(train['SeriousDlqin2yrs'], train['NumberOfTimes90DaysLate'], cutx7)
    dfx8, ivx8, woex8 = self_bin(train['SeriousDlqin2yrs'], train['NumberRealEstateLoansOrLines'], cutx8)
    dfx9, ivx9, woex9 = self_bin(train['SeriousDlqin2yrs'], train['NumberOfTime60-89DaysPastDueNotWorse'], cutx9)
    dfx10, ivx10, woex10 = self_bin(train['SeriousDlqin2yrs'], train['NumberOfDependents'], cutx10)

    # 通过图表，显示IV值，并进行选择。
    ivall = pd.Series([ivx1, ivx2, ivx3, ivx4, ivx5, ivx6, ivx7, ivx8, ivx9, ivx10],
                      index=['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10'])

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ivall.plot(kind='bar', ax=ax1)
    plt.show()

    # 顺序是第一种反着来，
    train['RevolvingUtilizationOfUnsecuredLines'] = Series(
        replace_woe(train['RevolvingUtilizationOfUnsecuredLines'], cutx1, woex1))
    train['age'] = Series(replace_woe(train['age'], cutx2, woex2))
    train['NumberOfTime30-59DaysPastDueNotWorse'] = Series(
        replace_woe(train['NumberOfTime30-59DaysPastDueNotWorse'], cutx3, woex3))
    train['DebtRatio'] = Series(replace_woe(train['DebtRatio'], cutx4, woex4))
    train['MonthlyIncome'] = Series(replace_woe(train['MonthlyIncome'], cutx5, woex5))
    train['NumberOfOpenCreditLinesAndLoans'] = Series(
        replace_woe(train['NumberOfOpenCreditLinesAndLoans'], cutx6, woex6))
    train['NumberOfTimes90DaysLate'] = Series(replace_woe(train['NumberOfTimes90DaysLate'], cutx7, woex7))
    train['NumberRealEstateLoansOrLines'] = Series(replace_woe(train['NumberRealEstateLoansOrLines'], cutx8, woex8))
    train['NumberOfTime60-89DaysPastDueNotWorse'] = Series(
        replace_woe(train['NumberOfTime60-89DaysPastDueNotWorse'], cutx9, woex9))
    train['NumberOfDependents'] = Series(replace_woe(train['NumberOfDependents'], cutx10, woex10))

    train.to_csv('data/train_data_woe.csv', index=False)

    # 对测试集进行分箱
    test = pd.read_csv('data/TestData.csv')

    # cut是对X取他的四分位，因为Y只有0  1  也不能取四分位。n=3因为最后有n-1，所以实际上是分成了四个桶，woe是四个值。
    # goodattribute是好的属性的意思
    dfx1, ivx1, woex1, cutx1 = mono_bin(test['SeriousDlqin2yrs'], test['RevolvingUtilizationOfUnsecuredLines'], n=10)
    dfx2, ivx2, woex2, cutx2 = mono_bin(test['SeriousDlqin2yrs'], test['age'], n=10)
    dfx4, ivx4, woex4, cutx4 = mono_bin(test['SeriousDlqin2yrs'], test['DebtRatio'], n=20)
    dfx5, ivx5, woex5, cutx5 = mono_bin(test['SeriousDlqin2yrs'], test['MonthlyIncome'], n=10)

    # 非最优分箱
    ninf = float('-inf')
    pinf = float('inf')
    cutx3 = [ninf, 0, 1, 3, 5, pinf]
    cutx6 = [ninf, 1, 2, 3, 5, pinf]
    cutx7 = [ninf, 0, 1, 3, 5, pinf]
    cutx8 = [ninf, 0, 1, 2, 3, pinf]
    cutx9 = [ninf, 0, 1, 3, pinf]
    cutx10 = [ninf, 0, 1, 2, 3, 5, pinf]

    dfx3, ivx3, woex3 = self_bin(test['SeriousDlqin2yrs'], test['NumberOfTime30-59DaysPastDueNotWorse'], cutx3)
    dfx6, ivx6, woex6 = self_bin(test['SeriousDlqin2yrs'], test['NumberOfOpenCreditLinesAndLoans'], cutx6)
    dfx7, ivx7, woex7 = self_bin(test['SeriousDlqin2yrs'], test['NumberOfTimes90DaysLate'], cutx7)
    dfx8, ivx8, woex8 = self_bin(test['SeriousDlqin2yrs'], test['NumberRealEstateLoansOrLines'], cutx8)
    dfx9, ivx9, woex9 = self_bin(test['SeriousDlqin2yrs'], test['NumberOfTime60-89DaysPastDueNotWorse'], cutx9)
    dfx10, ivx10, woex10 = self_bin(test['SeriousDlqin2yrs'], test['NumberOfDependents'], cutx10)

    # 替换成woe
    test['RevolvingUtilizationOfUnsecuredLines'] = Series(
        replace_woe(test['RevolvingUtilizationOfUnsecuredLines'], cutx1, woex1))
    test['age'] = Series(replace_woe(test['age'], cutx2, woex2))
    test['NumberOfTime30-59DaysPastDueNotWorse'] = Series(
        replace_woe(test['NumberOfTime30-59DaysPastDueNotWorse'], cutx3, woex3))
    test['DebtRatio'] = Series(replace_woe(test['DebtRatio'], cutx4, woex4))
    test['MonthlyIncome'] = Series(replace_woe(test['MonthlyIncome'], cutx5, woex5))
    test['NumberOfOpenCreditLinesAndLoans'] = Series(replace_woe(test['NumberOfOpenCreditLinesAndLoans'], cutx6, woex6))
    test['NumberOfTimes90DaysLate'] = Series(replace_woe(test['NumberOfTimes90DaysLate'], cutx7, woex7))
    test['NumberRealEstateLoansOrLines'] = Series(replace_woe(test['NumberRealEstateLoansOrLines'], cutx8, woex8))
    test['NumberOfTime60-89DaysPastDueNotWorse'] = Series(
        replace_woe(test['NumberOfTime60-89DaysPastDueNotWorse'], cutx9, woex9))
    test['NumberOfDependents'] = Series(replace_woe(test['NumberOfDependents'], cutx10, woex10))

    train.to_csv('data/test_data_woe.csv', index=False)
