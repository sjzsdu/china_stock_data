import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import os
import tempfile
import shutil
from datetime import datetime
from china_stock_data.persistent_dict import api_dict
from china_stock_data.fetchers import BaseFetcher
from china_stock_data.trading_time_checker import TradingTimeChecker

class TestBaseFetcher(unittest.TestCase):

    def setUp(self):
        # 创建临时目录
        self.test_dir = tempfile.mkdtemp()
        # 使用完整路径
        self.test_path = os.path.join(self.test_dir, 'test_data.csv')
        # 初始化 BaseFetcher 实例
        self.fetcher = BaseFetcher(self.test_path)

    def tearDown(self):
        # 清理临时目录
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    @patch('pandas.read_csv')
    def test_load_data_from_csv(self, mock_read_csv):
        # 模拟 CSV 数据
        mock_data = pd.DataFrame({'column1': [1, 2, 3]})
        mock_read_csv.return_value = mock_data
        
        # 创建空文件
        with open(self.test_path, 'w') as f:
            pass
        
        # 测试加载
        loaded_data = self.fetcher.load_data_from_csv()
        self.assertTrue(mock_read_csv.called)
        pd.testing.assert_frame_equal(loaded_data, mock_data)

    def test_save_data_to_csv(self):
        # 创建测试数据
        test_data = pd.DataFrame({'column1': [1, 2, 3]})
        
        # Mock api_dict.set
        with patch.object(api_dict, 'set') as mock_set:
            # 测试保存数据到 CSV
            self.fetcher.save_data_to_csv(test_data)
            
            # 验证文件是否被创建
            self.assertTrue(os.path.exists(self.test_path))
            
            # 验证 api_dict.set 是否被调用
            mock_set.assert_called_once_with(
                self.test_path, 
                datetime.now().strftime('%Y-%m-%d')
            )

    def test_is_data_up_to_date(self):
        # Mock api_dict 和 TradingTimeChecker
        with patch.object(api_dict, 'get', return_value='2023-10-10') as mock_get:
            with patch.object(TradingTimeChecker, 'compare_with_nearest_trade_date', return_value=True):
                # 测试数据是否为最新
                result = self.fetcher.is_data_up_to_date(pd.DataFrame())
                self.assertTrue(result)
                mock_get.assert_called_once_with(self.test_path)

    def test_fetch_and_cache_data(self):
        # Mock 所需的方法
        mock_data = pd.DataFrame({'column1': [1, 2, 3]})
        
        with patch.object(TradingTimeChecker, 'is_trading_time', return_value=False):
            with patch.object(BaseFetcher, 'fetch_data', return_value=mock_data):
                # 测试数据获取和缓存
                data = self.fetcher.fetch_and_cache_data()
                pd.testing.assert_frame_equal(data, mock_data)
                # 验证文件是否被创建
                self.assertTrue(os.path.exists(self.test_path))

if __name__ == '__main__':
    unittest.main()
