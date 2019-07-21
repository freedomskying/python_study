import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# 获取文件
data = pd.read_csv('data/train_add_missing.csv')
data = data.iloc[:, 1:]

# 绘制箱型图
# fig, ax = plt.subplots(2, 5)
#
# m = 0
# for i in range(2):
#     for j in range(5):
#         data.hist(column=data.columns[m], bins=12, ax=ax[i, j], figsize=(20, 18))
#         m += 1

age = data['age']
sns.distplot(age)
plt.show()

income = data[data['MonthlyIncome'] < 50000]['MonthlyIncome']
sns.distplot(income)
plt.show()

# 授信额度，分布不均匀
RevolvingUtilizationOfUnsecuredLines = data['RevolvingUtilizationOfUnsecuredLines']
sns.distplot(RevolvingUtilizationOfUnsecuredLines)
plt.show()

# M2数据，分布不均匀，不合适进行最优分箱操作
m2 = data['NumberOfTime30-59DaysPastDueNotWorse']
sns.distplot(m2)
plt.show()

# 每月偿还债务
DebtRatio = data['DebtRatio']
sns.distplot(DebtRatio)
plt.show()

# 未偿还贷款，可进行最优分箱
NumberOfOpenCreditLinesAndLoans = data['NumberOfOpenCreditLinesAndLoans']
sns.distplot(NumberOfOpenCreditLinesAndLoans)
plt.show()

# M4， 不合适最优分箱
NumberOfTimes90DaysLate = data['NumberOfTimes90DaysLate']
sns.distplot(NumberOfTimes90DaysLate)
plt.show()

# 抵押贷款数量，笔数
NumberRealEstateLoansOrLines = data['NumberRealEstateLoansOrLines']
sns.distplot(NumberRealEstateLoansOrLines)
plt.show()

# M3
m3 = data['NumberOfTime60-89DaysPastDueNotWorse']
sns.distplot(m3)
plt.show()

NumberOfDependents = data['NumberOfDependents']
sns.distplot(NumberOfDependents)
plt.show()
