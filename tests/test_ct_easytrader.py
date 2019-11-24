# coding: utf-8
import os
import sys
import time
import unittest
from threading import Thread
import easytrader
sys.path.append(".")

TEST_CLIENTS = os.environ.get("EZ_TEST_CLIENTS", "")

IS_WIN_PLATFORM = sys.platform != "darwin"

account='' #todo:
password='' #todo:

class TestCTClientTrader(unittest.TestCase):

    def setUp(self):
        import easytrader

        _ACCOUNT = os.environ.get("EZ_TEST_YH_ACCOUNT") or account
        _PASSWORD = (
                os.environ.get("EZ_TEST_YH_PASSWORD") or password
        )

        self._user = easytrader.use("ct_client")
        self._user.prepare(user=_ACCOUNT, password=_PASSWORD)
        time.sleep(3)
        result = self._user.balance
        print(result)

    def test_balance(self):
        _ACCOUNT = os.environ.get("EZ_TEST_YH_ACCOUNT") or account
        _PASSWORD = (
                os.environ.get("EZ_TEST_YH_PASSWORD") or password
        )

        self._user = easytrader.use("ct_client")
        self._user.prepare(user=_ACCOUNT, password=_PASSWORD)
        time.sleep(3)
        result = self._user.balance
        print(result)
        res=self._user.position
        print(res)
    def test_login(self):
        _ACCOUNT = os.environ.get("EZ_TEST_YH_ACCOUNT") or account
        _PASSWORD = (
                os.environ.get("EZ_TEST_YH_PASSWORD") or password
        )

        self._user = easytrader.use("ct_client")
        self._user.prepare(user=_ACCOUNT, password=_PASSWORD)
        time.sleep(3)
        result = self._user.balance
        print(result)
    def test_balance(self):
        '''
        <class 'dict'>
{'资金余额': 100.0, '可用金额': 4899.51, '可取金额': 100.0, '股票市值': 95743.76, '总资产': 101144.33}
        :return:
        '''
        time.sleep(2)
        result = self._user.balance
        print(type(result))
        print(result)
    def test_position(self):
        '''
        <class 'list'>
[{'证券代码': '="002027"', '证券名称': '分众传媒', '股票余额': 2700, '可用余额': 2700, '冻结数量': 0, '盈亏': 1394.36, '成本价': 5.3229999999999995, '盈亏比例(%)': 9.713, '市价': 5.84, '市值': 15768.0, '买入成本': 14372.1, '市场代码': 1, '交易市场': '深圳Ａ股', '股东帐户': '="0259071814"', '实际数量': 2700, 'Unnamed: 15': ''}, {'证券代码': '="128026"', '证券名称': '众兴转债', '股票余额': 10, '可用余额': 10, '冻结数量': 0, '盈亏': -13.06, '成本价': 94.652, '盈亏比例(%)': -1.485, '市价': 93.24600000000001, '市值': 932.46, '买入成本': 946.52, '市场代码': 1, '交易市场': '深圳Ａ股', '股东帐户': '="0259071814"', '实际数量': 10, 'Unnamed: 15': ''}, {'证券代码': '="162411"', '证券名称': '华宝油气', '股票余额': 7000, '可用余额': 7000, '冻结数量': 0, '盈亏': -111.12, '成本价': 0.397, '盈亏比例(%)': -4.03, '市价': 0.381, '市值': 2667.0, '买入成本': 2779.0, '市场代码': 1, '交易市场': '深圳Ａ股', '股东帐户': '="0259071814"', '实际数量': 7000, 'Unnamed: 15': ''}, {'证券代码': '="510050"', '证券名称': '50ETF', '股票余额': 3300, '可用余额': 3300, '冻结数量': 0, '盈亏': 502.56, '成本价': 2.815, '盈亏比例(%)': 5.4, '市价': 2.967, '市值': 9791.1, '买入成本': 9289.5, '市场代码': 2, '交易市场': '上海Ａ股', '股东帐户': '="A418921208"', '实际数量': 3300, 'Unnamed: 15': ''}, {'证券代码': '="510900"', '证券名称': 'H股ETF', '股票余额': 13200, '可用余额': 13200, '冻结数量': 0, '盈亏': 59.1, '成本价': 1.193, '盈亏比例(%)': 0.419, '市价': 1.198, '市值': 15813.6, '买入成本': 15747.6, '市场代码': 2, '交易市场': '上海Ａ股', '股东帐户': '="A418921208"', '实际数量': 13200, 'Unnamed: 15': ''}, {'证券代码': '="512000"', '证券名称': '券商ETF', '股票余额': 10000, '可用余额': 10000, '冻结数量': 0, '盈亏': -268.84, '成本价': 0.882, '盈亏比例(%)': -3.0610000000000004, '市价': 0.855, '市值': 8550.0, '买入成本': 8820.0, '市场代码': 2, '交易市场': '上海Ａ股', '股东帐户': '="A418921208"', '实际数量': 10000, 'Unnamed: 15': ''}, {'证券代码': '="518880"', '证券名称': '黄金ETF', '股票余额': 800, '可用余额': 800, '冻结数量': 0, '盈亏': 35.99, '成本价': 3.242, '盈亏比例(%)': 1.3880000000000001, '市价': 3.287, '市值': 2629.6, '买入成本': 2593.6, '市场代码': 2, '交易市场': '上海Ａ股', '股东帐户': '="A418921208"', '实际数量': 800, 'Unnamed: 15': ''}, {'证券代码': '="600030"', '证券名称': '中信证券', '股票余额': 600, '可用余额': 600, '冻结数量': 0, '盈亏': -1922.48, '成本价': 24.7, '盈亏比例(%)': -12.995999999999999, '市价': 21.49, '市值': 12894.0, '买入成本': 14820.0, '市场代码': 2, '交易市场': '上海Ａ股', '股东帐户': '="A418921208"', '实际数量': 600, 'Unnamed: 15': ''}, {'证券代码': '="601166"', '证券名称': '兴业银行', '股票余额': 1400, '可用余额': 1400, '冻结数量': 0, '盈亏': 2544.57, '成本价': 17.250999999999998, '盈亏比例(%)': 10.544, '市价': 19.07, '市值': 26698.0, '买入成本': 24151.4, '市场代码': 2, '交易市场': '上海Ａ股', '股东帐户': '="A418921208"', '实际数量': 1400, 'Unnamed: 15': ''}]

        :return:
        '''
        time.sleep(2)
        result = self._user.position
        print(type(result))
        print(result)
    def test_today_entrusts(self):
        '''
        当日委托
        :return:
        <class 'list'>
[{'委托时间': '09:39:30', '申报编号': 124, '证券代码': '="002027"', '证券名称': '分众传媒', '操作': '买入', '备注': ':未报', '委托价格': 5.0, '委托数量': 100, '成交均价': 0.0, '成交数量': 0, '撤单数量': 0, '股东帐户': '="0259071814"', '合同编号': '="217"', '交易市场': '深圳Ａ股', '保护价格': 0.0, 'Unnamed: 15': ''}]

        '''
        time.sleep(2)
        result = self._user.today_entrusts
        print(type(result))
        print(result)
    def test_today_trades(self):
        time.sleep(2)
        result = self._user.today_trades
        print(type(result))
        print(result)
    def test_cancel_entrusts(self):
        '''
        <class 'list'>
[{'委托时间': '09:39:30', '申报编号': 124, '证券代码': '="002027"', '证券名称': '分众传媒', '操作': '买入', '备注': ':未报', '委托价格': 5.0, '委托数量': 100, '成交均价': 0.0, '成交数量': 0, '撤单数量': 0, '股东帐户': '="0259071814"', '合同编号': '="217"', '交易市场': '深圳Ａ股', '保护价格': 0.0, 'Unnamed: 15': ''}]

        :return:
        '''
        time.sleep(2)
        result = self._user.cancel_entrusts
        print(type(result))
        print(result)
    # def test_buy(self):
    #     self._user.buy('002027',5,100)


if __name__ == "__main__":
    unittest.main()
