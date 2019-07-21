import numpy as np
from scipy.stats import chi2
import pandas as pd

# chi square distribution

percents = [0.95, 0.90, 0.5, 0.1, 0.05, 0.025, 0.01, 0.005]

# 获取自由度从1到30的卡方分布
df = pd.DataFrame(np.array([chi2.isf(percents, df=i) for i in range(1, 30)]))

# 设置列明为对应的相关性
df.columns = percents

df.index = df.index + 1

pd.set_option('precision', 3)

print(df)
