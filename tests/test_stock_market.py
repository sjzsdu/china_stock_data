class StockMarket:
    def __init__(self, symbol, index):
        self.symbol = symbol
        self.index = index
        self.fetchers = {fetcher.name: fetcher for fetcher in index_fetchers}

    def key(self):
        return self.symbol

    def get_data(self, name):
        if name not in self.fetchers:
            raise ValueError(f"Unknown fetcher: {name}")
        return self.fetchers[name].fetch_and_cache_data(self.symbol, self.index)

    def __getattr__(self, name):
        if name in self.fetchers:
            return self.get_data(name)
        return f"{name} is not found"

    def __getitem__(self, key):
        for fetcher in self.fetchers.values():
            try:
                return fetcher[key]
            except KeyError:
                continue
        raise KeyError(f"Key not found: {key}")
