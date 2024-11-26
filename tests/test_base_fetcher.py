import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
from datetime import datetime
from stock_data.fetchers import BaseFetcher, api_dict
from stock_data import TradingTimeChecker, api_dict

class TestBaseFetcher(unittest.TestCase):

    def setUp(self):
        # 创建一个测试路径
        self.test_path = 'test_data.csv'
        # 初始化 BaseFetcher 实例
        self.fetcher = BaseFetcher(self.test_path)

    @patch('your_module.api_dict')
    @patch('your_module.TradingTimeChecker')
    @patch('pandas.read_csv')
    def test_load_data_from_csv(self, mock_read_csv, mock_trading_time_checker, mock_api_dict):
        # 模拟 CSV 数据
        mock_data = pd.DataFrame({'column1': [1, 2, 3]})
        mock_read_csv.return_value = mock_data

        # 测试数据加载
        data = self.fetcher.load_data_from_csv()
        self.assertTrue(mock_read_csv.called)
        pd.testing.assert_frame_equal(data, mock_data)

    @patch('your_module.api_dict')
    @patch('pandas.DataFrame.to_csv')
    def test_save_data_to_csv(self, mock_to_csv, mock_api_dict):
        # 创建一个模拟的 DataFrame
        data = pd.DataFrame({'column1': [1, 2, 3]})

        # 测试保存数据到 CSV
        self.fetcher.save_data_to_csv(data)
        mock_to_csv.assert_called_once_with(self.test_path, index=False)
        mock_api_dict.set.assert_called_once_with(self.test_path, datetime.now().strftime('%Y-%m-%d'))

    @patch('your_module.api_dict')
    @patch('your_module.TradingTimeChecker')
    def test_is_data_up_to_date(self, mock_trading_time_checker, mock_api_dict):
        # 设置模拟返回值
        mock_api_dict.get.return_value = '2023-10-10'
        mock_trading_time_checker.compare_with_nearest_trade_date.return_value = True

        # 测试数据是否为最新
        result = self.fetcher.is_data_up_to_date(pd.DataFrame())
        self.assertTrue(result)
        mock_api_dict.get.assert_called_once_with(self.test_path)

    @patch('your_module.TradingTimeChecker.is_trading_time', return_value=False)
    @patch('your_module.BaseFetcher.fetch_data')
    def test_fetch_and_cache_data(self, mock_fetch_data, mock_is_trading_time):
        # 设置模拟返回值
        mock_data = pd.DataFrame({'column1': [1, 2, 3]})
        mock_fetch_data.return_value = mock_data

        # 测试数据获取和缓存
        data = self.fetcher.fetch_and_cache_data()
        mock_fetch_data.assert_called_once()
        pd.testing.assert_frame_equal(data, mock_data)

    def tearDown(self):
        # 清理测试数据文件
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

if __name__ == '__main__':
    unittest.main()
