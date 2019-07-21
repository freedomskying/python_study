from sklearn.metrics import roc_curve, auc

import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

train = pd.read_csv('data/train_data_woe.csv')
test = pd.read_csv('data/test_data_woe.csv')

matplotlib.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
matplotlib.rcParams['axes.unicode_minus'] = False

# 训练部分
Y = train['SeriousDlqin2yrs']
X = train.drop(['SeriousDlqin2yrs', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans',
                'NumberRealEstateLoansOrLines', 'NumberOfDependents'], axis=1)

X1 = sm.add_constant(X)
logit = sm.Logit(Y, X1)
result_train = logit.fit()
# print(result.summary())

Y_test = test['SeriousDlqin2yrs']
X_test = test.drop(['SeriousDlqin2yrs', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans',
                    'NumberRealEstateLoansOrLines', 'NumberOfDependents'], axis=1)

# 通过ROC曲线和AUC来评估模型的拟合能力。
X2 = sm.add_constant(X_test)
result_test = result_train.predict(X2)
fpr, tpr, threshold = roc_curve(Y_test, result_test)

# %f,%d,%s输出
rocauc = auc(fpr, tpr)
plt.plot(fpr, tpr, 'b', label='AUC=%0.2f' % rocauc)
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.show()
