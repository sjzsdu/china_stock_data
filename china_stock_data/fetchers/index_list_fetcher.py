import akshare as ak
from .base_fetcher import BaseFetcher
import pandas as pd
from typing import Any
from china_stock_data.config import MARKET_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string

class IndexListFetcher(BaseFetcher):
    """
    获取所有的指数
    """
    name = 'index_list'
    def __init__(self, stock_market: Any):
        self.stock_market = stock_market
        original_file = f"{IndexListFetcher.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{MARKET_PATH}/main/{file}"
        super().__init__(path)
        
    def fetch_data(self):
        try:
            print("Fetching index list data!")
            data = ak.index_stock_info()
            if data is None or data.empty:
                raise ValueError("No data returned from the API.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()
