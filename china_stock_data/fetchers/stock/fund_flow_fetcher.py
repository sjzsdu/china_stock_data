import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days


class StockFundFlowFetcher(BaseFetcher):
    """个股资金流向排行或明细 (短期资金面)
    当前选用 ak.stock_individual_fund_flow_rank()
    可扩展: 按日/3日/5日/10日分类拆分
    """
    name = "fund_flow_rank"

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
            data = ak.stock_individual_fund_flow_rank(sector_type="全部", indicator="今日")
            if data is None or data.empty:
                return pd.DataFrame()
            return data
        except Exception:
            return pd.DataFrame()
