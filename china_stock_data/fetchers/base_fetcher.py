
import os
import logging
import pandas as pd
import time
from datetime import datetime
from typing import Optional
from china_stock_data.config import FETCHER_DEBOUNCE_TIME
from china_stock_data import TradingTimeChecker
from china_stock_data import api_dict



class BaseFetcher:
    """
    Base class for all data fetchers.
    Handles caching, file IO, and update checks.
    """
    def __init__(self, path: str):
        self.path: str = path
        self.last_call_time: Optional[float] = None
        self._ensure_dir_exists()

    def _ensure_dir_exists(self) -> None:
        if self.path:
            dirname = os.path.dirname(self.path)
            if dirname:
                os.makedirs(dirname, exist_ok=True)


    def fetch_data(self) -> pd.DataFrame:
        raise NotImplementedError("Subclasses should implement this method.")

    def handle_data(self, data: pd.DataFrame) -> None:
        pass


    def load_data_from_csv(self) -> pd.DataFrame:
        if os.path.exists(self.path):
            data = pd.read_csv(self.path)
            self.handle_data(data)
            return data
        return pd.DataFrame()


    def save_data_to_csv(self, data: pd.DataFrame) -> None:
        """Save DataFrame to CSV file."""
        if not isinstance(data, pd.DataFrame) or data.empty:
            logging.warning("Invalid data, not saving to CSV file.")
            return
        self._ensure_dir_exists()
        data.to_csv(self.path, index=False)
        api_dict.set(self.path, datetime.now().strftime('%Y-%m-%d'))
            

    def check_saved_date(self, saved_date: str) -> bool:
        return TradingTimeChecker.compare_with_nearest_trade_date(saved_date)


    def is_data_up_to_date(self, data: pd.DataFrame) -> bool:
        saved_date = api_dict.get(self.path)
        if not saved_date:
            return False
        return self.check_saved_date(saved_date)
    

    def fetch_and_cache_data(self) -> pd.DataFrame:
        """Fetch and cache data, return DataFrame."""
        if not TradingTimeChecker.is_trading_time():
            data = self.load_data_from_csv()
            if not data.empty and self.is_data_up_to_date(data):
                return data
            data = self.fetch_data()
            if isinstance(data, pd.DataFrame) and not data.empty:
                self.save_data_to_csv(data)
                return data
            logging.warning("Fetched data is invalid, returning empty DataFrame.")
            return pd.DataFrame()
        current_time = time.time()
        if self.last_call_time is not None:
            if current_time - self.last_call_time < FETCHER_DEBOUNCE_TIME:
                return self.load_data_from_csv()
        data = self.fetch_data()
        if isinstance(data, pd.DataFrame) and not data.empty:
            self.save_data_to_csv(data)
            self.last_call_time = time.time()
            return data
        logging.warning("Fetched data is invalid, returning empty DataFrame.")
        return pd.DataFrame()


    def __getitem__(self, key):
        raise KeyError(f"Key '{key}' not found in {self.__class__.__name__}")