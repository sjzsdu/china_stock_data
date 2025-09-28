import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string


class DividendFetcher(BaseFetcher):
    """分红派息情况"""
    name = "dividend|stock_fhps_em"

    def __init__(self, stock_data):
        self.stock_data = stock_data
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        super().__init__(path)

    def fetch_data(self) -> pd.DataFrame:
        try:
            # Use date parameter for this API
            data = ak.stock_fhps_em(date="20231231")
            if data is None or data.empty:
                return pd.DataFrame()
            # Filter by symbol if data contains multiple stocks
            if '股票代码' in data.columns:
                data = data[data['股票代码'] == self.stock_data.symbol]
            return data
        except Exception:
            return pd.DataFrame()
