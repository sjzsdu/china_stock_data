import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import MARKET_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string, is_within_days


class MarginFinancingFetcher(BaseFetcher):
    """融资融券余额 (沪深) 合并表
    上证: stock_margin_sh  深证: stock_margin_sz -> 合并
    """
    name = "margin_financing|stock_margin_sse|stock_margin_szse"

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
            # Use available margin functions
            sh = ak.stock_margin_sse()
            sz = ak.stock_margin_szse()
            if sh is None or sh.empty:
                sh = pd.DataFrame()
            if sz is None or sz.empty:
                sz = pd.DataFrame()
            if sh.empty and sz.empty:
                return pd.DataFrame()
            # Combine data if both have data
            if not sh.empty and not sz.empty:
                return pd.concat([sh, sz], ignore_index=True)
            elif not sh.empty:
                return sh
            else:
                return sz
        except Exception:
            return pd.DataFrame()
