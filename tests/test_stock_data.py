import unittest
from unittest.mock import patch, MagicMock
from china_stock_data.stock_data import StockData

class TestStockData(unittest.TestCase):
    def setUp(self):
        self.symbol = '600519'
        self.type = 'stock'
        self.start_date = '2020-01-01'
        self.end_date = '2020-12-31'
        self.days = 365
        self.period = 'daily'
        self.adjust = 'qfq'
        self.stock_data = StockData(
            self.symbol, 
            self.type, 
            self.start_date, 
            self.end_date, 
            self.days, 
            self.period, 
            self.adjust
        )

    @patch('china_stock_data.stock_data.stock_fetchers')
    def test_get_data(self, mock_stock_fetchers):
        mock_fetcher = MagicMock()
        mock_fetcher.fetch_and_cache_data.return_value = 'mocked data'
        mock_stock_fetchers.__getitem__.return_value = mock_fetcher
        
        # 修改：直接设置 self.stock_data.fetchers
        self.stock_data.fetchers = {'fetcher1': mock_fetcher}
        
        data = self.stock_data.get_data('fetcher1')
        self.assertEqual(data, 'mocked data')

    def test_get_data_with_unknown_name(self):
        with self.assertRaises(ValueError):
            self.stock_data.get_data('unknown')

    def test_getattr(self):
        # 修改：直接设置 self.stock_data.fetchers
        mock_fetcher = MagicMock()
        mock_fetcher.fetch_and_cache_data.return_value = 'mocked data'
        self.stock_data.fetchers = {'fetcher1': mock_fetcher}
        
        data = self.stock_data.fetcher1
        self.assertEqual(data, 'mocked data')

    def test_getattr_with_unknown_name(self):
        data = self.stock_data.unknown
        self.assertEqual(data, 'unknown is not found')

    @patch('china_stock_data.stock_data.stock_fetchers')
    def test_getitem(self, mock_stock_fetchers):
        mock_fetcher = MagicMock()
        mock_fetcher.__getitem__.return_value = 'mocked data'
        mock_stock_fetchers.__getitem__.return_value = mock_fetcher
        
        # 修改：直接设置 self.stock_data.fetchers
        self.stock_data.fetchers = {'fetcher1': mock_fetcher}
        
        data = self.stock_data['key1']
        self.assertEqual(data, 'mocked data')

    def test_getitem_with_unknown_key(self):
        with self.assertRaises(KeyError):
            self.stock_data['unknown']

if __name__ == '__main__':
    unittest.main()
