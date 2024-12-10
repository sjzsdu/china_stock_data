import akshare as ak
from .base_fetcher import BaseFetcher
import pandas as pd
from typing import Any
from china_stock_data.config import MARKET_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days

class MarketMotionFetcher(BaseFetcher):
    """
    市场情绪指数
    """
    name = 'market_motion'
    def __init__(self, stock_market: Any):
        self.stock_market = stock_market
        original_file = f"{MarketMotionFetcher.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{MARKET_PATH}/main/{file}"
        super().__init__(path)
        
        
    def fetch_data(self):
        try:
            print("Fetching market motion data!")
            data = ak.index_news_sentiment_scope()
            if data is None or data.empty:
                raise ValueError("No data returned from the API.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()
