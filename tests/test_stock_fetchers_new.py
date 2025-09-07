import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from china_stock_data.fetchers.stock import StockHistFetcher, StockInfoFetcher, StockRealtimeFetcher, StockChipFetcher


class TestStockFetchers(unittest.TestCase):
    """Test cases for stock-related fetchers."""
    
    def setUp(self):
        self.mock_stock_data = MagicMock()
        self.mock_stock_data.symbol = "000001"
        self.mock_stock_data.start_date = "2023-01-01"
        self.mock_stock_data.end_date = "2023-12-31"
        self.mock_stock_data.period = "daily"
        self.mock_stock_data.adjust = "qfq"
        self.mock_stock_data.days_key = "2023-01-01&2023-12-31&"

    @patch('china_stock_data.fetchers.stock.hist_fetcher.ak.stock_zh_a_hist')
    def test_stock_hist_fetcher(self, mock_ak):
        """Test StockHistFetcher functionality."""
        mock_ak.return_value = pd.DataFrame({'price': [100, 101, 102]})
        
        fetcher = StockHistFetcher(self.mock_stock_data)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ak.assert_called_once()

    @patch('china_stock_data.fetchers.stock.info_fetcher.ak.stock_individual_info_em')
    def test_stock_info_fetcher(self, mock_ak):
        """Test StockInfoFetcher functionality."""
        mock_ak.return_value = pd.DataFrame({'name': ['Test Stock'], 'industry': ['Technology']})
        
        fetcher = StockInfoFetcher(self.mock_stock_data)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ak.assert_called_once()

    @patch('china_stock_data.fetchers.stock.realtime_fetcher.ak.stock_bid_ask_em')
    def test_stock_realtime_fetcher(self, mock_ak):
        """Test StockRealtimeFetcher functionality."""
        mock_ak.return_value = pd.DataFrame({'bid': [100], 'ask': [101]})
        
        fetcher = StockRealtimeFetcher(self.mock_stock_data)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ak.assert_called_once()

    @patch('china_stock_data.fetchers.stock.chip_fetcher.ak.stock_cyq_em')
    def test_stock_chip_fetcher(self, mock_ak):
        """Test StockChipFetcher functionality."""
        mock_ak.return_value = pd.DataFrame({'distribution': [0.1, 0.2, 0.3]})
        
        fetcher = StockChipFetcher(self.mock_stock_data)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ak.assert_called_once()

    def test_fetcher_names(self):
        """Test that fetcher names are correctly set."""
        self.assertEqual(StockHistFetcher.name, "kline")
        self.assertEqual(StockInfoFetcher.name, "info")
        self.assertEqual(StockRealtimeFetcher.name, "bid_ask")
        self.assertEqual(StockChipFetcher.name, "chip")


if __name__ == '__main__':
    unittest.main()
