import pandas as pd

from sklearn.ensemble import RandomForestRegressor


def data_desc(data):
    # 设置DataFrame调用head时，能够打印所有的列
    pd.set_option('display.max_columns', None)
    # 设置DataFrame调用head时，一行打印所有列，不换行
    pd.set_option('expand_frame_repr', False)

    # 查看数据前5行
    print(data.head())

    # 数据大小
    print(data.shape)

    # 数据整体预览
    print(data.describe())

    # 数据信息查看
    print(data.info())


# （1） 直接删除含有缺失值的样本。
# （2） 根据样本之间的相似性填补缺失值。
# （3） 根据变量之间的相关关系填补缺失值。

# 缺失值处理
# 变量MonthlyIncome缺失率比较大，所以我们根据变量之间的相关关系填补缺失值，采用随机森林法进行填补。
def add_monthly_income(df):
    # 从新排序df列，将MonthlyIncome放在首位，同时由于NumberOfDependts同样存在缺失，不作为变量之间的关系。
    process_df = df.ix[:, [5, 0, 1, 2, 3, 4, 6, 7, 8, 9]]

    # 分成已知特征值和未知特征值两部分
    # process_df['MonthlyIncome']获取MonthlyIncome列，转换为Series
    # 通过isnull和notnull，获取process_df中MonthlyIncome分别为真和为假的记录，并转换为numpy.ndarray
    known = process_df[process_df['MonthlyIncome'].notnull()].values
    unknown = process_df[process_df['MonthlyIncome'].isnull()].values

    # 获取第一列 MonthlyIncome
    y = known[:, 0]
    # 获取其他列
    x = known[:, 1:]

    # random_state
    # n_estimators 子树个数
    # max_depth 子树深度
    rfr = RandomForestRegressor(random_state=0, n_estimators=200, max_depth=3, n_jobs=-1)
    rfr.fit(x, y)

    predicted = rfr.predict(unknown[:, 1:])
    df.loc[df['MonthlyIncome'].isnull(), "MonthlyIncome"] = predicted

    return df


if __name__ == '__main__':
    # 导入训练数据
    data = pd.read_csv('data/cs-training.csv')
    # 删除第一列id
    data = data.iloc[:, 1:]

    # 对数据进行描述
    # 1.通过head查看数据
    # 2.查看数据集shape
    # 3.查看数据描述desc
    # 4.查看数据信息info
    data_desc(data)

    # 对MonthlyIncome列添加缺失值
    data = add_monthly_income(data)

    # 因为NumberOfDependents变量确实较少，可以直接删除，对总体模型不会造成太大影响
    data = data.dropna()
    data = data.drop_duplicates()

    # 剔除异常值
    data = data[data['age'] > 0]
    data = data[data['age'] < 90]
    data = data[data['NumberOfTimes90DaysLate'] < 90]
    data = data[data['NumberOfTime30-59DaysPastDueNotWorse'] < 90]
    data = data[data['NumberOfTime60-89DaysPastDueNotWorse'] < 90]
    # 变量SeriousDlqin2yrs取反
    data['SeriousDlqin2yrs'] = 1 - data['SeriousDlqin2yrs']

    # 对处理后数据进行描述
    data_desc(data)

    # 保存处理缺失值之后的数据
    data.to_csv('data/train_add_missing.csv', index=False)
