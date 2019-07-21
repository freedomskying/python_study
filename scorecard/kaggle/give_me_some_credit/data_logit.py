import statsmodels.api as sm
import pandas as pd

data = pd.read_csv('data/train_data_woe.csv')

Y = data['SeriousDlqin2yrs']
X = data.drop(['SeriousDlqin2yrs', 'DebtRatio', 'MonthlyIncome', 'NumberOfOpenCreditLinesAndLoans',
               'NumberRealEstateLoansOrLines', 'NumberOfDependents'], axis=1)

X1 = sm.add_constant(X)
logit = sm.Logit(Y, X1)
result = logit.fit()
print(result.summary())
