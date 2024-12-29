try:
    from importlib.metadata import version
    __version__ = version("china-stock-data")
except ImportError:
    from .__version__ import __version__

from .trading_time_checker import TradingTimeChecker
from .utils import generate_stable_string, friendly_number, get_first_line
from .persistent_dict import PersistentDict, app_dict, api_dict
from .stock_data import StockData
from .stock_market import StockMarket

__all__ = [
    'TradingTimeChecker',
    'generate_stable_string',
    'friendly_number',
    'get_first_line',
    'PersistentDict',
    'app_dict',
    'api_dict',
    'StockData',
    'StockMarket',
]
