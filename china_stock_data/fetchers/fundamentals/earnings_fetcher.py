import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days


class EarningsFetcher(BaseFetcher):
    """业绩快报 + 业绩预告 (symbol 聚合)"""
    name = "earnings|stock_yjbb_em|stock_yjyg_em"

    def __init__(self, stock_data):
        self.stock_data = stock_data
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        super().__init__(path)

    def check_saved_date(self, saved_date):
        return is_within_days(saved_date)

    def fetch_data(self) -> pd.DataFrame:
        symbol = self.stock_data.symbol
        try:
            report = ak.stock_yjbb_em(symbol=symbol)
        except Exception:
            report = pd.DataFrame()
        try:
            forecast = ak.stock_yjyg_em(symbol=symbol)
        except Exception:
            forecast = pd.DataFrame()
        dfs = []
        if report is not None and not report.empty:
            report['source_type'] = 'report'
            dfs.append(report)
        if forecast is not None and not forecast.empty:
            forecast['source_type'] = 'forecast'
            dfs.append(forecast)
        if not dfs:
            return pd.DataFrame()
        return pd.concat(dfs, ignore_index=True, sort=False)
