from china_stock_data.fetchers import index_fetchers
class StockMarket:

    def __init__(self, symbol):
        self.symbol = symbol
        self.fetchers = {}
        for fetcher in index_fetchers:
            self.fetchers[fetcher.name] = fetcher(self)
        
    def get_data(self, data_type: str):
        if data_type not in self.fetches:
            raise ValueError(f"Unknown data type: {data_type}")
        return self.fetches[data_type].fetch_and_cache_data()
    
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

