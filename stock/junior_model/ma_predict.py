import tushare as ts
import pandas as pd

if __name__ == '__main__':
    # 获取股票清单
    stock_list = ts.get_stock_basics().head()

    stock_hist_calc = pd.DataFrame()

    # 获取每只股票的交易历史
    for stock_list_index in stock_list.index:

        # 获取每只股票的交易数据
        stock_hist_data = ts.get_hist_data(code=stock_list_index)

        # 将每只股票数据按日期进行平移
        stock_hist_data_shift = stock_hist_data.shift(-1)

        # 计算两日之间的走势
        stock_hist_data['lastday_close'] =




        df = pd.DataFrame()

        stock_hist_data_shift = stock_hist_data.shift(-1)

        # 对每只股票，计算均线的拐点，举例上一次变化的日期
        for stock_hist_data_index in stock_hist_data.index:
            df['code'] = stock_list_index
            df['date'] = stock_hist_data_index
            df['close'] = stock_hist_data.loc(stock_hist_data_index).close
            df['ma20'] = stock_hist_data.loc(stock_hist_data_index).ma20
            df['lastday_close'] = stock_hist_data_shift.loc(stock_hist_data_index).close
            df['lastday_ma20'] = stock_hist_data_shift.loc(stock_hist_data_index).ma20
            df['gap_ma20'] = df['ma20'] - df['lastday_ma20']
            df['gap_close'] = df['close'] - df['lastday_close']
            df['trend_ma20'] = 1 if df['ma20'] > df['lastday_ma20'] else -1
            df['trend_close'] = 1 if df['close'] > df['lastday_close'] else -1

            df['change_point'] = df['trend_close'] - df.shift(-1)['trend_close']

        stock_hist_calc.append(df)

    # 判断每次拐点，价格的涨幅或者跌幅百分比是多少
    print(stock_hist_calc['change_point'] != 0)

    # 输出
