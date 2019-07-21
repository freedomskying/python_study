import pandas as pd
import numpy as np
from scipy.stats import chi2


def calc_chi_square(sample_set, feature, target):
    """
    计算某个特征每种属性值的卡方统计量
    params:
        sampleSet: 样本集
        feature: 目标特征
        target: 目标Y值 (0或1) Y值为二分类变量
    return:
        卡方统计量dataframe
        feature: 特征名称
        act_target_cnt: 实际坏样本数
        expected_target_cnt：期望坏样本数
        chi_square：卡方统计量
    """
    # 计算样本期望频率
    target_cnt = sample_set[target].sum()
    sample_cnt = len(sample_set[target])
    expected_ratio = target_cnt * 1.0 / sample_cnt

    # 对变量按属性值从大到小排序
    df = sample_set[[feature, target]]
    col_value = list(set(df[feature]))

    # 计算每一个属性值对应的卡方统计量等信息
    chi_list = []
    target_list = []
    expected_target_list = []

    # col_value是feature对应的每一个值，比如age = [21,22,23,24]
    for value in col_value:
        # feature坏样本个数
        df_target_cnt = df.loc[df[feature] == value, target].sum()
        # feature的总数
        df_cnt = len(df.loc[df[feature] == value, target])
        # feature的期望值
        expected_target_cnt = df_cnt * expected_ratio
        # 计算卡方值
        chi_square = (df_target_cnt - expected_target_cnt) ** 2 / expected_target_cnt
        # 将chi_square添加到卡方值列表chi_list
        chi_list.append(chi_square)
        # 将坏样本个数添加到目标清单target_list中
        target_list.append(df_target_cnt)
        # 将feature的期望添加到期望列表中
        expected_target_list.append(expected_target_cnt)

    # 结果输出到dataframe, 对应字段为特征属性值, 卡方统计量, 实际坏样本量, 期望坏样本量
    chi_stats = pd.DataFrame({feature: col_value, 'chi_square': chi_list,
                              'act_target_cnt': target_list, 'expected_target_cnt': expected_target_list})

    return chi_stats[[feature, 'act_target_cnt', 'expected_target_cnt', 'chi_square']]


def chi_merge_max_interval(chi_stats, feature, max_interval=5):
    """
    卡方分箱合并--最大区间限制法
    params:
        chi_stats: 卡方统计量dataframe
        feature: 目标特征
        maxInterval：最大分箱数阈值
    return:
        卡方合并结果dataframe, 特征分割split_list
    """
    # 获取当前箱体长度
    group_cnt = len(chi_stats)
    # 从chi_stats[feature]最小的值开始进行分箱
    split_list = [chi_stats[feature].min()]

    # 如果变量区间超过最大分箱限制，则根据合并原则进行合并
    while group_cnt > max_interval:

        min_index = chi_stats[chi_stats['chi_square'] == chi_stats['chi_square'].min()].index.tolist()[0]

        # 如果分箱区间在最前,则向下合并
        if min_index == 0:
            chi_stats = merge_chi_square(chi_stats, min_index + 1, min_index)

        # 如果分箱区间在最后，则向上合并
        elif min_index == group_cnt - 1:
            chi_stats = merge_chi_square(chi_stats, min_index - 1, min_index)

        # 如果分箱区间在中间，则判断与其相邻的最小卡方的区间，然后进行合并
        else:
            if chi_stats.loc[min_index - 1, 'chi_square'] > chi_stats.loc[min_index + 1, 'chi_square']:
                chi_stats = merge_chi_square(chi_stats, min_index, min_index + 1)
            else:
                chi_stats = merge_chi_square(chi_stats, min_index - 1, min_index)

        # 重新计算待分箱列表长度
        group_cnt = len(chi_stats)

    chi_merge_result = chi_stats
    split_list.extend(chi_merge_result[feature].tolist())
    return chi_merge_result, split_list


def chi_merge_min_chi_square(chi_stats, feature, d_free=4, cf=0.1, max_interval=5):
    """
    卡方分箱合并--卡方阈值法
    params:
        chi_stats: 卡方统计量dataframe
        feature: 目标特征
        maxInterval: 最大分箱数阈值, default 5
        dfree: 自由度, 最大分箱数-1, default 4
        cf: 显著性水平, default 10%
    return:
        卡方合并结果dataframe, 特征分割split_list
    """

    # 获取自由度为d_free、显著性为cf的卡方分布值
    threshold = get_chi_square_distribution(d_free, cf)

    # 初始化数据，获取最小的卡方值，列表长度，以及将最小卡方值放入返回列表中
    min_chi_square = chi_stats['chi_square'].min()
    group_cnt = len(chi_stats)
    split_list = [chi_stats[feature].min()]

    # 如果变量区间的最小卡方值小于阈值，则继续合并直到最小值大于等于阈值
    while min_chi_square < threshold and group_cnt > max_interval:
        min_index = chi_stats[chi_stats['chi_square'] == chi_stats['chi_square'].min()].index.tolist()[0]

        # 如果分箱区间在最前,则向下合并
        if min_index == 0:
            chi_stats = merge_chi_square(chi_stats, min_index + 1, min_index)

        # 如果分箱区间在最后，则向上合并
        elif min_index == group_cnt - 1:
            chi_stats = merge_chi_square(chi_stats, min_index - 1, min_index)

        # 如果分箱区间在中间，则判断与其相邻的最小卡方的区间，然后进行合并
        else:
            if chi_stats.loc[min_index - 1, 'chi_square'] > chi_stats.loc[min_index + 1, 'chi_square']:
                chi_stats = merge_chi_square(chi_stats, min_index, min_index + 1)
            else:
                chi_stats = merge_chi_square(chi_stats, min_index - 1, min_index)
        min_chi_square = chi_stats['chi_square'].min()
        group_cnt = len(chi_stats)
    chi_merge_result = chi_stats
    split_list.extend(chi_merge_result[feature].tolist())
    return chi_merge_result, split_list


def get_chi_square_distribution(d_free=4, cf=0.1):
    """
    根据自由度和置信度得到卡方分布和阈值
    params:
        dfree: 自由度, 最大分箱数-1, default 4
        cf: 显著性水平, default 10%
    return:
        卡方阈值
    """
    percents = [0.95, 0.90, 0.5, 0.1, 0.05, 0.025, 0.01, 0.005]
    df = pd.DataFrame(np.array([chi2.isf(percents, df=i) for i in range(1, 30)]))
    df.columns = percents
    df.index = df.index + 1
    # 显示小数点后面数字
    pd.set_option('precision', 3)
    return df.loc[d_free, cf]


def merge_chi_square(chi_result, index, merge_index, a='expected_target_cnt',
                     b='act_target_cnt', c='chi_square'):
    """
    params:
        chi_result: 待合并卡方数据集
        index: 合并后的序列号
        mergeIndex: 需合并的区间序号
        a, b, c: 指定合并字段
    return:
        分箱合并后的卡方dataframe
    """
    chi_result.loc[merge_index, a] = chi_result.loc[merge_index, a] + chi_result.loc[index, a]
    chi_result.loc[merge_index, b] = chi_result.loc[merge_index, b] + chi_result.loc[index, b]
    chi_result.loc[merge_index, c] = (chi_result.loc[merge_index, b] - chi_result.loc[merge_index, a]) ** 2 / \
                                     chi_result.loc[merge_index, a]
    chi_result = chi_result.drop([index])
    chi_result = chi_result.reset_index(drop=True)
    return chi_result


if __name__ == '__main__':
    # 获取文件
    train = pd.read_csv('data/TrainData.csv')

    chi_stat = calc_chi_square(train, 'age', 'SeriousDlqin2yrs')

    merge_df, split_list = chi_merge_max_interval(chi_stats=chi_stat, feature='age', max_interval=10)

    print(split_list)

    # chi_stat = calc_chi_square(train, 'age', 'SeriousDlqin2yrs')
    #
    # merge_df, split_list = chi_merge_min_chi_square(chi_stats=chi_stat, feature='age', d_free=4, cf=0.05,
    #                                                 max_interval=10)
    #
    # print(split_list)
