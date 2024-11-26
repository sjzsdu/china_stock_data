import akshare as ak
from .base_fetcher import BaseFetcher
import pandas as pd
from typing import Any
from china_stock_data import generate_stable_string
from china_stock_data.config import CACHE_PATH, CSV_EXT


class StockChipFetcher(BaseFetcher):
    """
    获取股票的筹码分布等
    """
    name = "chip"
    def __init__(self, stock_data: Any):
        self.stock_data = stock_data
        original_file = f"{StockChipFetcher.name}_{stock_data.adjust}"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        super().__init__(path)
        
    def fetch_data(self):
        try:
            print("Fetching stock chip data!")
            data = ak.stock_cyq_em(
                symbol=self.stock_data.symbol, 
                adjust=self.stock_data.adjust
            )
            if data is None or data.empty:
                raise ValueError("No data returned from the API.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()
        
