import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days


class RestrictedReleaseFetcher(BaseFetcher):
    """限售解禁队列"""
    name = "restricted_release"

    def __init__(self, stock_data):
        self.stock_data = stock_data
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        super().__init__(path)

    def check_saved_date(self, saved_date):
        return is_within_days(saved_date)

    def fetch_data(self) -> pd.DataFrame:
        try:
            data = ak.stock_restricted_release_queue_em()
            if data is None or data.empty:
                return pd.DataFrame()
            # 可由上层再按 symbol 过滤
            return data
        except Exception:
            return pd.DataFrame()
