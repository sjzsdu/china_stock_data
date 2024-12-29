import os

# 获取包的根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 设置数据存储目录
DATA_DIR = os.path.join(BASE_DIR, 'data')

# 设置字典文件路径
API_DICT_FILE = os.path.join(DATA_DIR, 'api_dict.json')
APP_DICT_FILE = os.path.join(DATA_DIR, 'app_dict.json')

CACHE_PATH = "cache"
MARKET_PATH = "market"
PRICE_COL = "收盘"
DATE_COL= "日期"
SYMBOL_COL = "股票代码"

HISTORY_DAYS = 360
CURRENT_DAYS = 360
FETCHER_DEBOUNCE_TIME = 120

CSV_EXT = ".csv"