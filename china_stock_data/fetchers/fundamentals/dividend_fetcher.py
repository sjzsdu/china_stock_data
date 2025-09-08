import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string


class DividendFetcher(BaseFetcher):
    """分红派息情况"""
    name = "dividend"

    def __init__(self, stock_data):
        self.stock_data = stock_data
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        super().__init__(path)

    def fetch_data(self) -> pd.DataFrame:
        try:
            data = ak.stock_fhps_em(symbol=self.stock_data.symbol)
            if data is None or data.empty:
                return pd.DataFrame()
            return data
        except Exception:
            return pd.DataFrame()
