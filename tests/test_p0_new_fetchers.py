import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

from china_stock_data.fetchers.market.northbound_holdings_fetcher import NorthboundHoldingsFetcher
from china_stock_data.fetchers.market.margin_financing_fetcher import MarginFinancingFetcher
from china_stock_data.fetchers.market.lhb_fetcher import LHBFetcher
from china_stock_data.fetchers.stock.fund_flow_fetcher import StockFundFlowFetcher
from china_stock_data.fetchers.fundamentals.financial_statements_fetcher import FinancialStatementsFetcher
from china_stock_data.fetchers.fundamentals.earnings_fetcher import EarningsFetcher
from china_stock_data.fetchers.fundamentals.dividend_fetcher import DividendFetcher
from china_stock_data.fetchers.fundamentals.restricted_release_fetcher import RestrictedReleaseFetcher
from china_stock_data.fetchers.fundamentals.top_shareholders_fetcher import TopShareholdersFetcher
from china_stock_data.fetchers.fundamentals.repurchase_fetcher import RepurchaseFetcher


class TestP0Fetchers(unittest.TestCase):
    def setUp(self):
        self.mock_stock_data = MagicMock()
        self.mock_stock_data.symbol = '600000'
        self.mock_stock_market = MagicMock()
        self.mock_stock_market.key.return_value = 'test_market'

    @patch('china_stock_data.fetchers.market.northbound_holdings_fetcher.ak.stock_hsgt_hold_stock_em')
    def test_northbound_holdings(self, mock_api):
        mock_api.return_value = pd.DataFrame({'代码': ['600000'], '持股量': [1000]})
        f = NorthboundHoldingsFetcher(self.mock_stock_market)
        df = f.fetch_data()
        self.assertFalse(df.empty)
        mock_api.assert_called_once()

    @patch('china_stock_data.fetchers.market.margin_financing_fetcher.ak.stock_margin_sse')
    @patch('china_stock_data.fetchers.market.margin_financing_fetcher.ak.stock_margin_szse')
    def test_margin_financing(self, mock_sz, mock_sh):
        mock_sh.return_value = pd.DataFrame({'日期': ['2025-01-01'], '融资余额': [1]})
        mock_sz.return_value = pd.DataFrame({'日期': ['2025-01-01'], '融资余额': [2]})
        f = MarginFinancingFetcher(self.mock_stock_market)
        df = f.fetch_data()
        self.assertEqual(len(df), 2)

    @patch('china_stock_data.fetchers.market.lhb_fetcher.ak.stock_lhb_detail_em')
    def test_lhb(self, mock_api):
        mock_api.return_value = pd.DataFrame({'代码': ['600000'], '上榜次数': [1]})
        f = LHBFetcher(self.mock_stock_market)
        df = f.fetch_data()
        self.assertFalse(df.empty)

    @patch('china_stock_data.fetchers.stock.fund_flow_fetcher.ak.stock_individual_fund_flow_rank')
    def test_fund_flow_rank(self, mock_api):
        mock_api.return_value = pd.DataFrame({'代码': ['600000'], '今日主力净流入': [1000000]})
        f = StockFundFlowFetcher(self.mock_stock_data)
        df = f.fetch_data()
        self.assertFalse(df.empty)

    @patch('china_stock_data.fetchers.fundamentals.financial_statements_fetcher.ak.stock_lrb_em')
    @patch('china_stock_data.fetchers.fundamentals.financial_statements_fetcher.ak.stock_zcfz_em')
    @patch('china_stock_data.fetchers.fundamentals.financial_statements_fetcher.ak.stock_xjll_em')
    def test_financial_statements(self, mock_cf, mock_bs, mock_pl):
        mock_pl.return_value = pd.DataFrame({'报告期': ['2024Q4'], '净利润': [10]})
        mock_bs.return_value = pd.DataFrame({'报告期': ['2024Q4'], '总资产': [100]})
        mock_cf.return_value = pd.DataFrame({'报告期': ['2024Q4'], '经营现金流': [20]})
        f = FinancialStatementsFetcher(self.mock_stock_data)
        df = f.fetch_data()
        self.assertEqual(df['statement_type'].nunique(), 3)

    @patch('china_stock_data.fetchers.fundamentals.earnings_fetcher.ak.stock_yjbb_em')
    @patch('china_stock_data.fetchers.fundamentals.earnings_fetcher.ak.stock_yjyg_em')
    def test_earnings(self, mock_forecast, mock_report):
        mock_report.return_value = pd.DataFrame({'报告期': ['2024Q4'], '每股收益': [1]})
        mock_forecast.return_value = pd.DataFrame({'报告期': ['2025Q1'], '预告类型': ['预增']})
        f = EarningsFetcher(self.mock_stock_data)
        df = f.fetch_data()
        self.assertEqual(df['source_type'].nunique(), 2)

    @patch('china_stock_data.fetchers.fundamentals.dividend_fetcher.ak.stock_fhps_em')
    def test_dividend(self, mock_api):
        mock_api.return_value = pd.DataFrame({'公告日期': ['2025-01-01'], '送转股数': [0.5]})
        f = DividendFetcher(self.mock_stock_data)
        df = f.fetch_data()
        self.assertFalse(df.empty)

    @patch('china_stock_data.fetchers.fundamentals.restricted_release_fetcher.ak.stock_restricted_release_queue_em')
    def test_restricted_release(self, mock_api):
        mock_api.return_value = pd.DataFrame({'解禁日期': ['2025-02-01'], '股票代码': ['600000']})
        f = RestrictedReleaseFetcher(self.mock_stock_data)
        df = f.fetch_data()
        self.assertFalse(df.empty)

    @patch('china_stock_data.fetchers.fundamentals.top_shareholders_fetcher.ak.stock_gdfx_free_top_10_em')
    def test_top_shareholders(self, mock_api):
        mock_api.return_value = pd.DataFrame({'截止日期': ['2025-03-31'], '股东名称': ['机构A']})
        f = TopShareholdersFetcher(self.mock_stock_data)
        df = f.fetch_data()
        self.assertFalse(df.empty)

    @patch('china_stock_data.fetchers.fundamentals.repurchase_fetcher.ak.stock_repurchase_em')
    def test_repurchase(self, mock_api):
        mock_api.return_value = pd.DataFrame({'公告日期': ['2025-01-10'], '回购金额': [5000000]})
        f = RepurchaseFetcher(self.mock_stock_data)
        df = f.fetch_data()
        self.assertFalse(df.empty)


if __name__ == '__main__':
    unittest.main()
