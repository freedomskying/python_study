from sklearn.cross_validation import train_test_split
import pandas as pd


# 将数据进行切分
def data_split(data):
    y = data['SeriousDlqin2yrs']
    x = data.ix[:, 1:]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    train = pd.concat([y_train, x_train], axis=1)
    test = pd.concat([y_test, x_test], axis=1)

    train.to_csv('data/TrainData.csv', index=False)
    test.to_csv('data/TestData.csv', index=False)


