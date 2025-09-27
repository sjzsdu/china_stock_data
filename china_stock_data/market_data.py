from typing import Dict, Any, Optional
import pandas as pd
from datetime import datetime
from china_stock_data.fetchers import market_fetchers


class MarketData:
    """
    Stock market data class for fetching market-wide information.
    
    Supports market sentiment, margin financing, northbound holdings, and LHB data.
    """

    def __init__(self, date: Optional[str] = None, symbol: str = "当月", **kwargs) -> None:
        """
        Initialize MarketData instance for market-wide data.
        
        Args:
            date: Date for data fetching in YYYY-MM-DD or YYYYMM format (defaults to current date)
            symbol: Symbol parameter for sector summary (defaults to "当月")
            **kwargs: Additional parameters for backward compatibility (e.g., index)
        """
        # Set date with default to current date
        current_date = datetime.now()
        raw_date = date or current_date.strftime('%Y%m%d')
        
        # Backward compatibility: support old StockMarket API
        self.index = kwargs.get('index', None)  # For backward compatibility
        
        # Handle symbol parameter with backward compatibility
        if 'index' in kwargs and 'symbol' not in kwargs and symbol == "当月":
            # If only index is provided, set symbol to None for backward compatibility
            self.symbol = None
        else:
            self.symbol = symbol
        
        # Normalize date format to YYYYMMDD
        if len(raw_date) == 10 and '-' in raw_date:  # YYYY-MM-DD format
            self.date = raw_date.replace('-', '')  # Convert to YYYYMMDD
        elif len(raw_date) == 8:  # Already YYYYMMDD format
            self.date = raw_date
        elif len(raw_date) == 6:  # YYYYMM format, add default day
            self.date = raw_date + '01'
        else:
            self.date = current_date.strftime('%Y%m%d')  # Fallback to current date
        
        # Pre-format dates for different API requirements
        self.date_yyyymm = self.date[:6]  # YYYYMM format
        self.date_yyyymmdd = self.date  # YYYYMMDD format
        
        # Initialize fetchers
        self.fetchers: Dict[str, Any] = {}
        for fetcher in market_fetchers:
            fetcher_instance = fetcher(self)
            # Handle names with "|" separator
            if "|" in fetcher.name:
                names = fetcher.name.split("|")
                for name in names:
                    self.fetchers[name.strip()] = fetcher_instance
            else:
                self.fetchers[fetcher.name] = fetcher_instance
            
    def key(self) -> str:
        """
        Generate unique key for this market instance.
        
        Returns:
            Unique identifier string for market data
        """
        # Backward compatibility: mimic old StockMarket key logic
        if self.index:
            return f"I{self.index}"
        elif self.symbol and self.symbol != "当月":
            return self.symbol
        else:
            return 'market'
        
    def get_data(self, name: str) -> pd.DataFrame:
        """
        Get market data by fetcher name.
        
        Args:
            name: Fetcher name (e.g., "market_sentiment", "lhb", "margin_financing", "northbound_holdings")
            
        Returns:
            DataFrame containing the requested market data
            
        Raises:
            ValueError: If the data type is unknown
        """
        if name not in self.fetchers:
            raise ValueError(f"Unknown market data type: {name}")
        
        return self.fetchers[name].fetch_and_cache_data()
    
    def __getattr__(self, name: str) -> Any:
        """Get market data using attribute access."""
        if name in self.fetchers:
            return self.get_data(name.strip())
        return f'{name} is not found'
    
    def __getitem__(self, key: str) -> Any:
        """Get market data using bracket notation."""
        for _, fetcher in self.fetchers.items():
            try:
                return fetcher[key.strip()]
            except KeyError:
                continue 
        raise KeyError(f"Key '{key}' not found in any market fetcher")
