## P0 新增数据抓取示例

```python
from china_stock_data import StockData, StockMarket
from china_stock_data.fetchers.market.northbound_holdings_fetcher import NorthboundHoldingsFetcher
from china_stock_data.fetchers.market.margin_financing_fetcher import MarginFinancingFetcher
from china_stock_data.fetchers.market.lhb_fetcher import LHBFetcher
from china_stock_data.fetchers.stock.fund_flow_fetcher import StockFundFlowFetcher
from china_stock_data.fetchers.fundamentals.financial_statements_fetcher import FinancialStatementsFetcher
from china_stock_data.fetchers.fundamentals.earnings_fetcher import EarningsFetcher
from china_stock_data.fetchers.fundamentals.dividend_fetcher import DividendFetcher
from china_stock_data.fetchers.fundamentals.share_change_fetcher import ShareChangeFetcher
from china_stock_data.fetchers.fundamentals.restricted_release_fetcher import RestrictedReleaseFetcher
from china_stock_data.fetchers.fundamentals.top_shareholders_fetcher import TopShareholdersFetcher
from china_stock_data.fetchers.fundamentals.block_trade_fetcher import BlockTradeFetcher
from china_stock_data.fetchers.fundamentals.repurchase_fetcher import RepurchaseFetcher

symbol = '600519'
sd = StockData(symbol, 'stock', '2024-01-01', '2024-12-31', 365, 'daily', 'qfq')
sm = StockMarket()

# 财务报表
financials = FinancialStatementsFetcher(sd).fetch_and_cache_data()
print(financials.head())

# 业绩快报 + 预告
earnings = EarningsFetcher(sd).fetch_and_cache_data()
print(earnings.head())

# 分红
dividend = DividendFetcher(sd).fetch_and_cache_data()
print(dividend.head())

# 股东增减持
share_change = ShareChangeFetcher(sd).fetch_and_cache_data()
print(share_change.head())

# 限售解禁
restricted = RestrictedReleaseFetcher(sd).fetch_and_cache_data()
print(restricted.head())

# 前十大流通股东
top_holders = TopShareholdersFetcher(sd).fetch_and_cache_data()
print(top_holders.head())

# 大宗交易
block_trades = BlockTradeFetcher(sd).fetch_and_cache_data()
print(block_trades.head())

# 回购信息
repurchase = RepurchaseFetcher(sd).fetch_and_cache_data()
print(repurchase.head())

# 龙虎榜
lhb = LHBFetcher(sm).fetch_and_cache_data()
print(lhb.head())

# 北向持股
north = NorthboundHoldingsFetcher(sm).fetch_and_cache_data()
print(north.head())

# 融资融券
margin = MarginFinancingFetcher(sm).fetch_and_cache_data()
print(margin.head())

# 个股资金流排行 (全市场, 上层可筛选 symbol)
fund_flow_rank = StockFundFlowFetcher(sd).fetch_and_cache_data()
print(fund_flow_rank.head())
```
