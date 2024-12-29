from .base_fetcher import BaseFetcher
from .stock_chip_fetcher import StockChipFetcher
from .stock_hist_fetcher import StockHistFetcher
from .stock_info_fetcher import StockInfoFetcher
from .stock_realtime_fetcher import StockRealtimeFetcher
from .index_components_fetcher import IndexComponentsFetcher
from .index_list_fetcher import IndexListFetcher
from .market_motion_fetcher import MarketMotionFetcher
from .us_index_fetcher import UsIndexFetcher
stock_fetchers = [StockHistFetcher, StockInfoFetcher, StockChipFetcher, StockRealtimeFetcher]
index_fetchers = [IndexComponentsFetcher, IndexListFetcher, MarketMotionFetcher, UsIndexFetcher]


__version__ = '0.1.7'