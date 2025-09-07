from typing import Optional, Dict, Any
import pandas as pd
from china_stock_data.fetchers import index_fetchers, market_fetchers


class StockMarket:
    """
    Stock market data class for fetching index and market-related data.
    
    Supports index components, index lists, US indices, and market sentiment data.
    """

    def __init__(self, symbol: Optional[str] = None, index: Optional[str] = None) -> None:
        """
        Initialize StockMarket instance.
        
        Args:
            symbol: Market symbol
            index: Index code for fetching index-related data
        """
        self.symbol: Optional[str] = symbol
        self.index: Optional[str] = index
        
        # Initialize fetchers
        self.fetchers: Dict[str, Any] = {}
        for fetcher in index_fetchers + market_fetchers:
            self.fetchers[fetcher.name] = fetcher(self)
            
    def key(self) -> str:
        """
        Generate unique key for this market instance.
        
        Returns:
            Unique identifier string
        """
        return self.symbol if self.symbol else f'I{self.index}'
        
    def get_data(self, name: str) -> pd.DataFrame:
        """
        Get data by fetcher name.
        
        Args:
            name: Fetcher name (e.g., "index_components", "index_list", "us_index")
            
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
