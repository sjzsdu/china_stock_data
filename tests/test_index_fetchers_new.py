import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from china_stock_data.fetchers.index import IndexComponentsFetcher, IndexListFetcher, UsIndexFetcher


class TestIndexFetchers(unittest.TestCase):
    """Test cases for index-related fetchers."""
    
    def setUp(self):
        self.mock_stock_market = MagicMock()
        self.mock_stock_market.symbol = "market_symbol"
        self.mock_stock_market.index = "000300"
        self.mock_stock_market.key.return_value = "test_key"

    @patch('china_stock_data.fetchers.index.components_fetcher.ak.index_stock_cons_csindex')
    def test_index_components_fetcher(self, mock_ak):
        """Test IndexComponentsFetcher functionality."""
        mock_ak.return_value = pd.DataFrame({'stock_code': ['000001', '000002'], 'stock_name': ['Stock A', 'Stock B']})
        
        fetcher = IndexComponentsFetcher(self.mock_stock_market)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ak.assert_called_once()

    @patch('china_stock_data.fetchers.index.list_fetcher.ak.index_stock_info')
    def test_index_list_fetcher(self, mock_ak):
        """Test IndexListFetcher functionality."""
        mock_ak.return_value = pd.DataFrame({'index_code': ['000300', '399006'], 'index_name': ['CSI 300', 'ChiNext']})
        
        fetcher = IndexListFetcher(self.mock_stock_market)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ak.assert_called_once()

    @patch('china_stock_data.fetchers.index.us_fetcher.ak.index_us_stock_sina')
    def test_us_index_fetcher(self, mock_ak):
        """Test UsIndexFetcher functionality."""
        mock_ak.return_value = pd.DataFrame({'date': ['2023-01-01'], 'close': [4000]})
        
        fetcher = UsIndexFetcher(self.mock_stock_market)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ak.assert_called_once_with(symbol=".INX")

    def test_fetcher_names(self):
        """Test that fetcher names are correctly set."""
        self.assertEqual(IndexComponentsFetcher.name, "index_components|index_stock_cons_csindex")
        self.assertEqual(IndexListFetcher.name, "index_list|index_stock_info")
        self.assertEqual(UsIndexFetcher.name, "us_index|index_us_stock_sina")


if __name__ == '__main__':
    unittest.main()
