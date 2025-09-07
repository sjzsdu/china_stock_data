import unittest
from unittest.mock import patch, MagicMock
from china_stock_data.stock_market import StockMarket


class TestStockMarket(unittest.TestCase):
    """Test cases for StockMarket class."""
    
    def setUp(self):
        self.symbol = 'SH000001'
        self.index = '000300'
        self.stock_market = StockMarket(symbol=self.symbol, index=self.index)

    def test_init_with_symbol(self):
        """Test StockMarket initialization with symbol."""
        market = StockMarket(symbol="test_symbol")
        self.assertEqual(market.symbol, "test_symbol")
        self.assertIsNone(market.index)
        self.assertIsInstance(market.fetchers, dict)

    def test_init_with_index(self):
        """Test StockMarket initialization with index."""
        market = StockMarket(index="000300")
        self.assertIsNone(market.symbol)
        self.assertEqual(market.index, "000300")
        self.assertIsInstance(market.fetchers, dict)

    def test_key_method_with_symbol(self):
        """Test key method when symbol is provided."""
        market = StockMarket(symbol="test_symbol")
        self.assertEqual(market.key(), "test_symbol")

    def test_key_method_with_index(self):
        """Test key method when index is provided."""
        market = StockMarket(index="000300")
        self.assertEqual(market.key(), "I000300")

    def test_get_data(self):
        """Test get_data method."""
        mock_fetcher = MagicMock()
        mock_fetcher.fetch_and_cache_data.return_value = 'mocked data'
        self.stock_market.fetchers = {'test_fetcher': mock_fetcher}
        
        data = self.stock_market.get_data('test_fetcher')
        self.assertEqual(data, 'mocked data')

    def test_get_data_with_unknown_name(self):
        """Test get_data with unknown fetcher name."""
        with self.assertRaises(ValueError):
            self.stock_market.get_data('unknown')

    def test_getattr(self):
        """Test __getattr__ method."""
        mock_fetcher = MagicMock()
        mock_fetcher.fetch_and_cache_data.return_value = 'mocked data'
        self.stock_market.fetchers = {'test_fetcher': mock_fetcher}
        
        data = self.stock_market.test_fetcher
        self.assertEqual(data, 'mocked data')

    def test_getattr_with_unknown_name(self):
        """Test __getattr__ with unknown name."""
        data = self.stock_market.unknown
        self.assertEqual(data, 'unknown is not found')

    def test_getitem(self):
        """Test __getitem__ method."""
        mock_fetcher = MagicMock()
        mock_fetcher.__getitem__.return_value = 'mocked data'
        self.stock_market.fetchers = {'test_fetcher': mock_fetcher}
        
        data = self.stock_market['test_key']
        self.assertEqual(data, 'mocked data')

    def test_getitem_with_unknown_key(self):
        """Test __getitem__ with unknown key."""
        with self.assertRaises(KeyError):
            self.stock_market['unknown']


if __name__ == '__main__':
    unittest.main()
