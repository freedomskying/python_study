# -*- coding:utf-8 -*-
import tushare as ts

import pandas as pd
import matplotlib as mpl

from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.utils import stats


# 设置策略
class K401Strategy(strategy.BacktestingStrategy):
    def __init__(self, feed):
        strategy.BacktestingStrategy.__init__(self, feed, 1000000)

        # We wan't to use adjusted close prices instead of close.
        self.setUseAdjustedValues(True)

        # Place the orders to get them processed on the first bar.
        orders = {
            "中信证券": 600030,
            "华夏幸福": 600340,
            "白云机场": 600004,
            "新华保险": 601336,
        }
        for instrument, quantity in orders.items():
            self.marketOrder(instrument, quantity, onClose=True, allOrNone=True)

    def onBars(self, bars):
        pass


def ret2csv(ftg):
    xd = retAnalyzer.getReturns()
    x8 = [];
    for x1 in xd:
        x8 = x8 + [x1];
    xs1 = pd.Series(x8);
    print(xs1.tail())
    xs1.to_csv(ftg)
    print(ftg)

    return xs1


# 获取4支股票信息
# 600030 中信证券
# 600340 华夏幸福
# 600004 白云机场
# 601336 新华保险

pro = ts.pro_api()
# [ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount]
df = pro.daily(ts_code='600030.SH', start_date='20180701', end_date='20180718')

# 模拟收益率计算
