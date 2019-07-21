import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 获取文件
    train = pd.read_csv('data/TrainData.csv')

    corr = train.corr()
    xticks = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']

    fig = plt.figure()
    fig.set_size_inches(16, 6)
    ax1 = fig.add_subplot(111)

    # 默认是0到1的，vmin和vmax可自定义设置
    sns.heatmap(corr, vmin=-1, vmax=1, cmap='hsv', annot=True, square=True)
    ax1.set_xticklabels(xticks, rotation=0)
    plt.show()
