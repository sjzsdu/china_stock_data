import akshare as ak
from .base_fetcher import BaseFetcher
import pandas as pd
from typing import Any
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string

class StockRealtimeFetcher(BaseFetcher):
    """
    获取股票的实时交易数据
    """
    name = 'bid_ask'
    def __init__(self, stock_data: Any):
        self.stock_data = stock_data
        
        original_file = f"{StockRealtimeFetcher.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        super().__init__(path)
        
    def fetch_data(self):
        try:
            print("Fetching stock realtime data!")
            data = ak.stock_bid_ask_em(
                symbol=self.stock_data.symbol,
            )
            if data is None or data.empty:
                raise ValueError("No data returned from the API.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()
        
        
    def __getitem__(self, key):
        data = self.fetch_and_cache_data()
        try:
            value = data.loc[data['item'] == key, 'value']
            if not value.empty:
                return value.values[0]
            else:
                raise KeyError(f"Key '{key}' not found in DataFrame")
        except KeyError:
            raise KeyError(f"Key '{key}' not found in DataFrame")
