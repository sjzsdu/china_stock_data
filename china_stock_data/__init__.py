try:
    from importlib.metadata import version
    __version__ = version("china_stock_data")
except ImportError:
    from .__version__ import __version__

from .trading_time_checker import TradingTimeChecker
from .utils import generate_stable_string, friendly_number, get_first_line
from .persistent_dict import PersistentDict, app_dict, api_dict
from .stock_data import StockData
from .index_data import IndexData
from .market_data import MarketData

# Backward compatibility aliases
IndexMarket = IndexData  # For backward compatibility
StockMarket = MarketData

__all__ = [
    'TradingTimeChecker',
    'generate_stable_string',
    'friendly_number',
    'get_first_line',
    'PersistentDict',
    'app_dict',
    'api_dict',
    'StockData',
    'IndexData',
    'MarketData',
    'StockMarket',  # Alias for MarketData
    'IndexMarket',  # Alias for IndexData
]
