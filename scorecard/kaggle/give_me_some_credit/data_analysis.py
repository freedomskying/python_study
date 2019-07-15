import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

# 获取文件
data = pd.read_csv('data/cs-training.csv')
data = data.iloc[:, 1:]

age = data['age']
sns.distplot(age)
plt.show()
