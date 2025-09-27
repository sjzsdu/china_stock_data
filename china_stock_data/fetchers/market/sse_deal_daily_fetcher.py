import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import MARKET_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days
from datetime import datetime, timedelta


class SSEDealDailyFetcher(BaseFetcher):
    """上海证券交易所每日成交概况"""
    name = "sse_deal_daily|stock_sse_deal_daily"

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
            # Get pre-formatted YYYYMMDD date from entry class instance
            date = self.market_data.date_yyyymmdd
            
            data = ak.stock_sse_deal_daily(date=date)
            if data is None or data.empty:
                return pd.DataFrame()
            return data
        except Exception:
            return pd.DataFrame()