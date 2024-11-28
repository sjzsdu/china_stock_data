import akshare as ak
from .base_fetcher import BaseFetcher
import pandas as pd
from typing import Any
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days

class IndexComponentsFetcher(BaseFetcher):
    """
    获取指定指数的成分股
    """
    name = 'index_components'
    def __init__(self, stock_market: Any):
        self.stock_market = stock_market
        original_file = f"{IndexComponentsFetcher.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_market.symbol}/{file}"
        super().__init__(path)
        
    def fetch_data(self):
        if self.stock_market.symbol is None:
            return pd.DataFrame()
        try:
            print("Fetching index components data!")
            data = ak.index_stock_cons_csindex(self.stock_market.symbol)
            if data is None or data.empty:
                raise ValueError("No data returned from the API.")
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return pd.DataFrame()
        
    def check_saved_date(self, saved_date):
        return is_within_days(saved_date)
        
    def fetch_and_cache_data(self):
        data = super().fetch_and_cache_data()
        data['成分券代码'] = data['成分券代码'].astype(str).apply(lambda x: x.zfill(6))
        return data

    def __getitem__(self, key):
        data = self.fetch_and_cache_data()
        try:
            if key == 'index_market':
                return data['交易所'].value_counts()
            elif key == 'index_codes':
                return data['成分券代码'].unique()
            elif key == 'index_names':
                return data['成分券名称'].unique()
            elif key == 'index_codes_names':
                return data['成分券代码', '成分券名称']
            else:
                raise KeyError(f"Key '{key}' not found in DataFrame")
        except KeyError:
            raise KeyError(f"Key '{key}' not found in DataFrame")