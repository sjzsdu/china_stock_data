import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import MARKET_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days


class NorthboundHoldingsFetcher(BaseFetcher):
    """北向持股每日持仓 (沪深港通)
    ak: stock_hsgt_hold_stock_em 每日全量, 需按 symbol 过滤
    当前实现: 缓存整表, 上层可自行过滤
    """
    name = "northbound_holdings|stock_hsgt_hold_stock_em"

    def __init__(self, stock_market):
        self.stock_market = stock_market
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{MARKET_PATH}/main/{file}"
        super().__init__(path)

    def check_saved_date(self, saved_date):
        return is_within_days(saved_date)

    def fetch_data(self) -> pd.DataFrame:
        try:
            data = ak.stock_hsgt_hold_stock_em()
            if data is None or data.empty:
                return pd.DataFrame()
            return data
        except Exception:
            return pd.DataFrame()
