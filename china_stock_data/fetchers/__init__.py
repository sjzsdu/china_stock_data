from .base_fetcher import BaseFetcher
from .stock import StockChipFetcher, StockHistFetcher, StockInfoFetcher, StockRealtimeFetcher
from .index import IndexComponentsFetcher, IndexListFetcher, UsIndexFetcher  
from .market import (
    MarketSentimentFetcher, LHBFetcher, MarginFinancingFetcher, NorthboundHoldingsFetcher,
    SSESummaryFetcher, SZSESummaryFetcher, SZSEAreaSummaryFetcher, 
    SZSESectorSummaryFetcher, SSEDealDailyFetcher
)
from .fundamentals import (
    BlockTradeFetcher, DividendFetcher, EarningsFetcher, FinancialStatementsFetcher,
    RepurchaseFetcher, RestrictedReleaseFetcher, ShareChangeFetcher, TopShareholdersFetcher
)

stock_fetchers = [StockHistFetcher, StockInfoFetcher, StockChipFetcher, StockRealtimeFetcher]
index_fetchers = [IndexComponentsFetcher, IndexListFetcher, UsIndexFetcher]
market_fetchers = [
    MarketSentimentFetcher, LHBFetcher, MarginFinancingFetcher, NorthboundHoldingsFetcher,
    SSESummaryFetcher, SZSESummaryFetcher, SZSEAreaSummaryFetcher, 
    SZSESectorSummaryFetcher, SSEDealDailyFetcher
]
fundamentals_fetchers = [
    BlockTradeFetcher, DividendFetcher, EarningsFetcher, FinancialStatementsFetcher,
    RepurchaseFetcher, RestrictedReleaseFetcher, ShareChangeFetcher, TopShareholdersFetcher
]

__version__ = '0.1.7'