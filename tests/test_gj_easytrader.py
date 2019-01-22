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


class TestGjClientTrader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import easytrader

        # input your test account and password
        cls._ACCOUNT = os.environ.get("EZ_TEST_YH_ACCOUNT") or "your account"
        cls._PASSWORD = (
            os.environ.get("EZ_TEST_YH_PASSWORD") or "your password"
        )

        cls._user = easytrader.use("gj_client")
        cls._user.prepare(user=cls._ACCOUNT, password=cls._PASSWORD)

    def test_balance(self):
        _ACCOUNT = os.environ.get("EZ_TEST_YH_ACCOUNT") or "your account"
        _PASSWORD = (
                os.environ.get("EZ_TEST_YH_PASSWORD") or "your password"
        )

        self._user = easytrader.use("gj_client")
        self._user.prepare(user=_ACCOUNT, password=_PASSWORD)
        time.sleep(3)
        result = self._user.balance
        print(result)
    def login(self):
        _ACCOUNT = os.environ.get("EZ_TEST_YH_ACCOUNT") or "your account"
        _PASSWORD = (
                os.environ.get("EZ_TEST_YH_PASSWORD") or "your password"
        )

        self._user = easytrader.use("gj_client")
        self._user.prepare(user=_ACCOUNT, password=_PASSWORD)
        time.sleep(3)
        result = self._user.balance
        print(result)
    def balance(self):
        time.sleep(20)
        while True:
            result = self._user.balance
            print(result)



if __name__ == "__main__":
    unittest.main()
