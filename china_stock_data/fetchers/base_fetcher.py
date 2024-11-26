import os
import pandas as pd
import time
from datetime import datetime
from china_stock_data.config import FETCHER_DEBOUNCE_TIME
from china_stock_data import TradingTimeChecker
from china_stock_data import api_dict 


class BaseFetcher:
    def __init__(self, path: str):
        self.path = path
        self.last_call_time = None

    def fetch_data(self):
        raise NotImplementedError("Subclasses should implement this method.")
    
    def handle_data(self, data: pd.DataFrame):
        pass

    def load_data_from_csv(self):
        if os.path.exists(self.path):
            data = pd.read_csv(self.path)
            self.handle_data(data)
            return data
        return pd.DataFrame()

    def save_data_to_csv(self, data):
        if not data.empty:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            data.to_csv(self.path, index=False)
            api_dict.set(self.path, datetime.now().strftime('%Y-%m-%d'))

    def is_data_up_to_date(self, data):
        # 从api_dict中检索保存的日期
        saved_date = api_dict.get(self.path)
        if not saved_date:
            return False
        return TradingTimeChecker.compare_with_nearest_trade_date(saved_date)
    
    def fetch_and_cache_data(self):
        if not TradingTimeChecker.is_trading_time():
            data = self.load_data_from_csv()
            if not data.empty and self.is_data_up_to_date(data):
                return data
            else:
                data = self.fetch_data()
                self.save_data_to_csv(data)
                return data
        else:
            current_time = time.time()
            if self.last_call_time is not None:
                if current_time - self.last_call_time < FETCHER_DEBOUNCE_TIME:
                    return self.load_data_from_csv()
            data = self.fetch_data()
            self.save_data_to_csv(data)
            self.last_call_time = time.time()
            return data

    def __getitem__(self, key):
        raise KeyError(f"Key '{key}' not found in {self.__class__.__name__}")