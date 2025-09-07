import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from china_stock_data.fetchers.market import MarketSentimentFetcher


class TestMarketSentimentFetcher(unittest.TestCase):
    """Test cases for market sentiment fetcher."""
    
    def setUp(self):
        self.mock_stock_market = MagicMock()
        self.mock_stock_market.symbol = "market_symbol"
        self.mock_stock_market.index = None
        self.mock_stock_market.key.return_value = "test_key"

    @patch('china_stock_data.fetchers.market.sentiment_fetcher.ak.index_news_sentiment_scope')
    def test_market_sentiment_fetcher(self, mock_ak):
        """Test MarketSentimentFetcher functionality."""
        mock_ak.return_value = pd.DataFrame({'date': ['2023-01-01'], 'sentiment': [0.6]})
        
        fetcher = MarketSentimentFetcher(self.mock_stock_market)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        mock_ak.assert_called_once()

    @patch('china_stock_data.fetchers.market.sentiment_fetcher.ak.index_news_sentiment_scope')
    def test_market_sentiment_fetcher_error_handling(self, mock_ak):
        """Test MarketSentimentFetcher error handling."""
        mock_ak.side_effect = Exception("API Error")
        
        fetcher = MarketSentimentFetcher(self.mock_stock_market)
        result = fetcher.fetch_data()
        
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(result.empty)

    def test_fetcher_name(self):
        """Test that fetcher name is correctly set."""
        self.assertEqual(MarketSentimentFetcher.name, "market_sentiment")


if __name__ == '__main__':
    unittest.main()
