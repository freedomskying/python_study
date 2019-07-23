import math
import pandas as pd
from pandas import Series
import numpy as np

# 计算分数函数
from scorecard.kaggle.give_me_some_credit.data_binning import mono_bin


def get_score(coe, woe, p):
    scores = []
    for w in woe:
        score = round(coe * w * p, 0)
        scores.append(score)
    return scores


# 部分评分x1,x2,x3,x7,x9
# j和m相当于j是移动光标，m是跟着j，确定数的
def compute_score(series, cut, scores):
    i = 0
    list = []
    while i < len(series):
        value = series[i]
        j = len(cut) - 2
        m = len(cut) - 2
        while j >= 0:
            if value >= cut[j]:
                j = -1
            else:
                j = j - 1
                m = m - 1
        list.append(scores[m])
        i = i + 1
    return list


# list就是再x1里面挑一个值，这个值和series【i】是对应的
# score是等于模型系数*woe(一个woe对应一个score)*p值（比例因子）

coe = [9.738849, 0.638002, 0.505995, 1.032246, 1.790041, 1.131956]  # 回归系数

p = 20 / math.log(2)  # p值（比例因子）
q = 600 - 20 * math.log(20) / math.log(2)  #
base_score = round(q + p * coe[0], 0)

train_woe = pd.read_csv('data/train_data_woe.csv')

# 因为第一个是常数项
# 构建评分卡时候只需要选出那些，IV值高的特征就行，最后相加得到总分
x1 = get_score(coe[1], train_woe['RevolvingUtilizationOfUnsecuredLines'], p)
x2 = get_score(coe[2], train_woe['age'], p)
x3 = get_score(coe[3], train_woe['NumberOfTime30-59DaysPastDueNotWorse'], p)
x7 = get_score(coe[4], train_woe['NumberOfTimes90DaysLate'], p)
x9 = get_score(coe[5], train_woe['NumberOfTime60-89DaysPastDueNotWorse'], p)
# x1的四个值分别对应cut的四个区间.PDO Point Double Odds,    就是好坏比翻一倍， odds就是好坏比
print(x1)
print(x2)
print(x3)
print(x7)
print(x9)

# 非最优分箱
ninf = float('-inf')
pinf = float('inf')
cutx3 = [ninf, 0, 1, 3, 5, pinf]
cutx6 = [ninf, 1, 2, 3, 5, pinf]
cutx7 = [ninf, 0, 1, 3, 5, pinf]
cutx8 = [ninf, 0, 1, 2, 3, pinf]
cutx9 = [ninf, 0, 1, 3, pinf]
cutx10 = [ninf, 0, 1, 2, 3, 5, pinf]

# 获取文件
train = pd.read_csv('data/TrainData.csv')

# cut是对X取他的四分位，因为Y只有0  1  也不能取四分位。n=3因为最后有n-1，所以实际上是分成了四个桶，woe是四个值。
# goodattribute是好的属性的意思
dfx1, ivx1, woex1, cutx1 = mono_bin(train['SeriousDlqin2yrs'], train['RevolvingUtilizationOfUnsecuredLines'], n=10)
dfx2, ivx2, woex2, cutx2 = mono_bin(train['SeriousDlqin2yrs'], train['age'], n=10)
dfx4, ivx4, woex4, cutx4 = mono_bin(train['SeriousDlqin2yrs'], train['DebtRatio'], n=20)
dfx5, ivx5, woex5, cutx5 = mono_bin(train['SeriousDlqin2yrs'], train['MonthlyIncome'], n=10)

test1 = pd.read_csv('data/TestData.csv')
# 先构建好Series再加上也可以
# round可能要用到import math.
# 只需要对test计算分值，因为我们前面构建模型用的是train，计算分值要用test
test1['BaseScore'] = Series(np.zeros(len(test1)) + base_score)
test1['x1'] = Series(compute_score(test1['RevolvingUtilizationOfUnsecuredLines'], cutx1, x1))
test1['x2'] = Series(compute_score(test1['age'], cutx2, x2))
test1['x3'] = Series(compute_score(test1['NumberOfTime30-59DaysPastDueNotWorse'], cutx3, x3))
test1['x7'] = Series(compute_score(test1['NumberOfTimes90DaysLate'], cutx7, x7))
test1['x9'] = Series(compute_score(test1['NumberOfTime60-89DaysPastDueNotWorse'], cutx9, x9))
test1['score'] = test1['BaseScore'] + test1['x1'] + test1['x2'] + test1['x3'] + test1['x7'] + test1['x9']
test1.to_csv('data/score_data.csv')
