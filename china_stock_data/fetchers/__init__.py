from .base_fetcher import BaseFetcher
from .stock import StockChipFetcher, StockHistFetcher, StockInfoFetcher, StockRealtimeFetcher
from .index import IndexComponentsFetcher, IndexListFetcher, UsIndexFetcher  
from .market import (
    LHBFetcher, MarginFinancingFetcher, NorthboundHoldingsFetcher,
    SSESummaryFetcher, SZSESummaryFetcher, SZSEAreaSummaryFetcher, 
    SZSESectorSummaryFetcher, SSEDealDailyFetcher
)
from .fundamentals import (
    DividendFetcher, EarningsFetcher, FinancialStatementsFetcher,
    RepurchaseFetcher, RestrictedReleaseFetcher, TopShareholdersFetcher
)

stock_fetchers = [StockHistFetcher, StockInfoFetcher, StockChipFetcher, StockRealtimeFetcher]
index_fetchers = [IndexComponentsFetcher, IndexListFetcher, UsIndexFetcher]
market_fetchers = [
    LHBFetcher, MarginFinancingFetcher, NorthboundHoldingsFetcher,
    SSESummaryFetcher, SZSESummaryFetcher, SZSEAreaSummaryFetcher, 
    SZSESectorSummaryFetcher, SSEDealDailyFetcher
]
fundamentals_fetchers = [
    DividendFetcher, EarningsFetcher, FinancialStatementsFetcher,
    RepurchaseFetcher, RestrictedReleaseFetcher, TopShareholdersFetcher
]

__version__ = '0.1.7'