import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string


class ShareChangeFetcher(BaseFetcher):
    """股东增减持 / 股本变动 (聚合)"""
    name = "share_change|stock_share_change_em"

    def __init__(self, stock_data):
        self.stock_data = stock_data
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        super().__init__(path)

    def fetch_data(self) -> pd.DataFrame:
        # AkShare 中增减持接口: stock_share_change_em
        try:
            data = ak.stock_share_change_em(symbol=self.stock_data.symbol)
            if data is None or data.empty:
                return pd.DataFrame()
            return data
        except Exception:
            return pd.DataFrame()
