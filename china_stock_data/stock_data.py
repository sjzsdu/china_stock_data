from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import pandas as pd
from china_stock_data.config import HISTORY_DAYS
from china_stock_data.fetchers import stock_fetchers


class StockData:
    """
    Stock data class for fetching and managing stock-related data.
    
    Supports various data types including historical prices, real-time data,
    stock information, and chip distribution.
    """
    
    def __init__(
        self, 
        symbol: str, 
        type: str = "stock", 
        start_date: Optional[str] = None, 
        end_date: Optional[str] = None, 
        days: Optional[int] = None, 
        period: str = "daily", 
        adjust: str = "qfq"
    ) -> None:
        """
        Initialize StockData instance.
        
        Args:
            symbol: Stock symbol (e.g., "000001")
            type: Data type, defaults to "stock"
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            days: Number of days from end_date backwards
            period: Data period ("daily", "weekly", "monthly")
            adjust: Price adjustment ("qfq", "hfq", "")
        """
        self.symbol: str = symbol
        self.type: str = type
        self.period: str = period
        self.adjust: str = adjust
        self.days_key: str = '&'.join([start_date or '', end_date or '', str(days) or ''])
        self.days: int = days or HISTORY_DAYS
        self.end_date: str = end_date or datetime.now().strftime('%Y-%m-%d')
        
        if start_date:
            self.start_date = start_date
        else:
            end_date_obj = datetime.strptime(self.end_date, '%Y-%m-%d')
            self.start_date = (end_date_obj - timedelta(days=self.days)).strftime('%Y-%m-%d')
        
        # Initialize fetchers
        self.fetchers: Dict[str, Any] = {}
        for fetcher in stock_fetchers:
            self.fetchers[fetcher.name] = fetcher(self)
        
    def get_data(self, name: str) -> pd.DataFrame:
        """
        Get data by fetcher name.
        
        Args:
            name: Fetcher name (e.g., "kline", "info", "bid_ask", "chip")
            
        Returns:
            DataFrame containing the requested data
            
        Raises:
            ValueError: If the data type is unknown
        """
        if name not in self.fetchers:
            raise ValueError(f"Unknown data type: {name}")
        return self.fetchers[name].fetch_and_cache_data()
    
    def __getattr__(self, name: str) -> Any:
        """Get data using attribute access."""
        if name in self.fetchers:
            return self.get_data(name.strip())
        return f'{name} is not found'
    
    def __getitem__(self, key: str) -> Any:
        """Get data using bracket notation."""
        for _, fetcher in self.fetchers.items():
            try:
                return fetcher[key.strip()]
            except KeyError:
                continue 
        raise KeyError(f"Key '{key}' not found in any fetcher")

