import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import MARKET_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days
from datetime import datetime


class SZSEAreaSummaryFetcher(BaseFetcher):
    """深圳证券交易所市场总貌-地区交易排序"""
    name = "szse_area_summary|stock_szse_area_summary"

    def __init__(self, market_data):
        self.market_data = market_data
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{MARKET_PATH}/main/{file}"
        super().__init__(path)

    def check_saved_date(self, saved_date):
        return is_within_days(saved_date, days=30)  # Monthly data, cache for 30 days

    def fetch_data(self) -> pd.DataFrame:
        try:
            # Get pre-formatted YYYYMM date from entry class instance
            date = self.market_data.date_yyyymm
            
            data = ak.stock_szse_area_summary(date=date)
            if data is None or data.empty:
                return pd.DataFrame()
            return data
        except Exception:
            return pd.DataFrame()