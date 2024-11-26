import pytest
import os
from datetime import datetime, timedelta
from china_stock_data import PersistentDict, TradingTimeChecker

@pytest.fixture
def setup_persistent_dict():
    filename = 'test_trade_dates_cache.json'
    pdict = PersistentDict(filename)
    yield pdict
    if os.path.exists(filename):
        os.remove(filename)

def test_persistent_dict(setup_persistent_dict):
    pdict = setup_persistent_dict
    pdict.set('key1', 'value1')
    assert pdict.get('key1') == 'value1'
    pdict.set('key2', 'value2')
    assert pdict.get('key2') == 'value2'
    pdict.delete('key1')
    assert pdict.get('key1') is None
    assert pdict.get('key2') == 'value2'

@pytest.fixture
def setup_trading_time_checker():
    # 使用临时缓存文件进行测试
    TradingTimeChecker.appDict = PersistentDict('test_trade_dates_cache.json')
    yield
    # 清理测试缓存文件
    if os.path.exists('test_trade_dates_cache.json'):
        os.remove('test_trade_dates_cache.json')

def test_is_trading_time(setup_trading_time_checker):
    # 假设今天是交易日，并在交易时间内
    assert TradingTimeChecker.is_trading_time('2023-10-23 10:00:00') is True
    # 假设今天是交易日，但不在交易时间内
    assert TradingTimeChecker.is_trading_time('2023-10-23 16:00:00') is False
    # 假设今天不是交易日
    assert TradingTimeChecker.is_trading_time('2023-10-22 10:00:00') is False

def test_get_nearest_trade_date(setup_trading_time_checker):
    nearest_trade_date = TradingTimeChecker.get_nearest_trade_date('2023-10-23')
    assert nearest_trade_date <= '2023-10-23'

def test_compare_with_nearest_trade_date(setup_trading_time_checker):
    assert TradingTimeChecker.compare_with_nearest_trade_date('2023-10-23', '2023-10-23') is True
    assert TradingTimeChecker.compare_with_nearest_trade_date('2023-10-22', '2023-10-23') is False

# 确保替换 'your_module' 为包含 PersistentDict 和 TradingTimeChecker 类的实际模块名。
