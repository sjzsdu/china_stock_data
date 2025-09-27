import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import MARKET_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days
from datetime import datetime


class SZSESummaryFetcher(BaseFetcher):
    """深圳证券交易所市场总貌-证券类别统计"""
    name = "szse_summary|stock_szse_summary"

    def __init__(self, market_data):
        self.market_data = market_data
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{MARKET_PATH}/main/{file}"
        super().__init__(path)

    def check_saved_date(self, saved_date):
        return is_within_days(saved_date)

    def fetch_data(self) -> pd.DataFrame:
        try:
            # Use yesterday's date as default
            date = datetime.now().strftime('%Y%m%d')
            data = ak.stock_szse_summary(date=date)
            if data is None or data.empty:
                return pd.DataFrame()
            return data
        except Exception:
            return pd.DataFrame()