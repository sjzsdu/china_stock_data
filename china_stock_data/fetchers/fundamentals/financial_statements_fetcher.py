import akshare as ak
import pandas as pd
from ..base_fetcher import BaseFetcher
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string


class FinancialStatementsFetcher(BaseFetcher):
    """三大财务报表统一抓取: 利润表, 资产负债表, 现金流量表
    合并后增加 statement_type 标识; 由上层传入 symbol
    """
    name = "financial_statements|stock_lrb_em|stock_zcfz_em|stock_xjll_em"

    def __init__(self, stock_data):
        self.stock_data = stock_data
        original_file = f"{self.name}_"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        super().__init__(path)

    def fetch_data(self) -> pd.DataFrame:
        symbol = self.stock_data.symbol
        try:
            lrb = ak.stock_lrb_em(symbol=symbol)
        except Exception:
            lrb = pd.DataFrame()
        try:
            zcfz = ak.stock_zcfz_em(symbol=symbol)
        except Exception:
            zcfz = pd.DataFrame()
        try:
            xjll = ak.stock_xjll_em(symbol=symbol)
        except Exception:
            xjll = pd.DataFrame()
        dfs = []
        if not lrb.empty:
            lrb['statement_type'] = 'P&L'
            dfs.append(lrb)
        if not zcfz.empty:
            zcfz['statement_type'] = 'BS'
            dfs.append(zcfz)
        if not xjll.empty:
            xjll['statement_type'] = 'CF'
            dfs.append(xjll)
        if not dfs:
            return pd.DataFrame()
        data = pd.concat(dfs, ignore_index=True, sort=False)
        return data
