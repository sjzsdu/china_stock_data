from datetime import datetime, timedelta
from china_stock_data.config import HISTORY_DAYS
from china_stock_data.fetchers import stock_fetchers


class StockData:
    def __init__(
            self, 
            symbol, 
            type="stock", 
            start_date=None, 
            end_date=None, 
            days=None, 
            period="daily", 
            adjust="qfq"
        ):
        self.symbol = symbol
        self.type = type
        self.period = period
        self.adjust = adjust
        self.days_key = '&'.join([start_date or '', end_date or '', days or ''])
        self.days = days or HISTORY_DAYS
        self.end_date = end_date or datetime.now().strftime('%Y-%m-%d')
        if start_date:
            self.start_date = start_date
        else:
            end_date_obj = datetime.strptime(self.end_date, '%Y-%m-%d')
            self.start_date = (end_date_obj - timedelta(days=self.days)).strftime('%Y-%m-%d')
        self.fetchers = {}
        for fetcher in stock_fetchers:
            self.fetchers[fetcher.name] = fetcher(self)
        
    def get_data(self, name: str):
        if name not in self.fetchers:
            raise ValueError(f"Unknown data type: {name}")
        return self.fetchers[name].fetch_and_cache_data()
    
    def __getattr__(self, name: str):
        if name in self.fetchers:
            return self.get_data(name.strip())
        return f'{name} is not found'
    
    
    def __getitem__(self, key: str):
        for _, fetcher in self.fetchers.items():
            try:
                return fetcher[key.strip()]
            except KeyError:
                continue 
        raise KeyError(f"Key '{key}' not found in any fetcher")

