import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # get stock data
    stock_data = ts.get_hist_data('600848')

    # sort asc
    stock_data.sort_index(axis=0, inplace=True)

    # calc ma 30 60
    ma_list = [30, 60]

    for ma in ma_list:
        # 分别计算30日、60日的移动平均线
        stock_data['ma' + str(ma)] = pd.rolling_mean(stock_data['close'], ma)

        # 计算简单算术移动平均线MA - 注意：stock_data['close']为股票每天的收盘价
        stock_data['ewma' + str(ma)] = pd.ewma(stock_data['close'], span=ma)

    # stock_data.sort_index(axis=0, ascending=False, inplace=True)

    stock_plot = pd.DataFrame()
    stock_plot['ewma60'] = stock_data['ewma60']
    stock_plot['ma60'] = stock_data['ma60']
    stock_plot['ma20'] = stock_data['ma20']
    stock_plot['close'] = stock_data['close']
    stock_plot.plot()
    plt.show()

    '''
    plt.figure()
    stock_data.close.plot()
    plt.show()
    '''
