import matplotlib.pyplot as plt
# 读取数据
import pandas as pd

# 获取文件
data = pd.read_csv('data/cs-training.csv')
data = data.iloc[:, 1:]

# 打印表头
print(data.columns)

# 查看NumberOfTime30-59DaysPastDueNotWorse、NumberOfTimes90DaysLate、NumberOfTime60-89DaysPastDueNotWorse
data_box = data.iloc[:, [3, 7, 9]]
# 查看data_box对应的数据分布箱型图
data_box.boxplot()
plt.show()

# 查看年龄字段
dataage = data[['age']]
# 查看年龄的箱型图
dataage.boxplot()
plt.show()
