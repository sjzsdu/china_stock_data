# Copilot Instructions for China Stock Data

## Architecture Overview

This is a modern Python library for Chinese stock market data fetching, built around a **fetcher-based architecture** with intelligent caching. The core design separates data types into distinct classes while sharing common infrastructure.

### Core Components

- **StockData**: Individual stock analysis (27 fetchers) - basic + fundamentals data
- **IndexMarket**: Index-related data (6 fetchers) - components, lists, US indices  
- **MarketData**: Market-wide data (9 fetchers) - sentiment, margin financing, LHB
- **BaseFetcher**: Abstract base with caching, debouncing, and CSV persistence

### Multi-Name Fetcher Pattern

**Critical**: All fetchers support pipe-separated names (`"business_name|akshare_method"`):
```python
name = "kline|stock_zh_a_hist"  # Creates 2 access keys for same instance
name = "margin_financing|stock_margin_sse|stock_margin_szse"  # Creates 3 keys
```

**Implementation**: During initialization, names are split and each creates a dict entry pointing to the same fetcher instance for memory efficiency.

## Development Patterns

### Adding New Fetchers

1. **Inherit from BaseFetcher**: Place in appropriate subdirectory (`stock/`, `market/`, `fundamentals/`, `index/`)
2. **Set multi-name**: `name = "business_name|akshare_method_name"`  
3. **Constructor pattern**: Accept parent class instance (`stock_data`, `stock_market`, etc.)
4. **Register**: Add to appropriate list in `fetchers/__init__.py`
5. **Path convention**: Use `generate_stable_string()` for consistent filenames

### Caching Strategy

- **Location**: `.data_cache/{symbol}/` for stocks, `.market_cache/main/` for market data
- **Persistence**: CSV files with hash-based names via `generate_stable_string()`
- **Validation**: Override `check_saved_date()` for custom cache invalidation
- **Trading-aware**: Uses `TradingTimeChecker` for intelligent cache expiry

### Data Class Integration

Classes initialize fetchers with pipe-separated name handling:
```python
# In stock_data.py
all_fetchers = stock_fetchers + fundamentals_fetchers
for fetcher in all_fetchers:
    fetcher_instance = fetcher(self)
    if "|" in fetcher.name:
        names = fetcher.name.split("|")
        for name in names:
            self.fetchers[name.strip()] = fetcher_instance
    else:
        self.fetchers[fetcher.name] = fetcher_instance
```

## Testing & Development

### Running Tests
```bash
# From project root
PYTHONPATH=. python tests/test_basic_functionality.py
python -m pytest tests/ -v  # All tests
```

### Project Structure
- `china_stock_data/fetchers/` - Organized by data type (stock/, market/, index/, fundamentals/)
- `tests/` - Comprehensive test suite with README
- `examples/` - Demo scripts and Jupyter notebooks
- `docs/` - MkDocs documentation

### Dependencies
- **Core**: `akshare` (data source), `pandas` (data processing)
- **Dev**: `pytest` (testing), `mkdocs` (docs)
- **Management**: Poetry for dependency management

## Key Patterns to Follow

### Error Handling
```python
def fetch_data(self) -> pd.DataFrame:
    try:
        data = ak.some_function()
        if data is None or data.empty:
            return pd.DataFrame()
        return data
    except Exception:
        return pd.DataFrame()  # Always return empty DataFrame on error
```

### File Naming
- Use `generate_stable_string()` for cache file names
- Include relevant parameters in original filename before hashing
- Always append `CSV_EXT` from config

### Access Methods
Every data class supports 3 access patterns:
- Attribute: `stock.dividend`
- Dictionary: `stock["dividend"]` 
- Method: `stock.get_data("dividend")`

### Configuration
Key settings in `config.py`: cache paths, debounce times, default periods. Trading time awareness built into cache validation.

## Code Quality Principles

### Write Compact and Efficient Code
- **Prefer comprehensions** over loops where readable: `[f.name for f in fetchers if "|" in f.name]`
- **Use early returns** to reduce nesting: `if data is None: return pd.DataFrame()`
- **Leverage pandas operations** instead of iterating: `data['平均'] = (data['最低'] + data['最高']) / 2`
- **Chain operations** when logical: `data.dropna().reset_index(drop=True).to_csv(path)`

### Avoid Code Duplication (DRY Principle)
- **Extract common patterns**: The fetcher initialization logic is centralized in data classes
- **Use inheritance wisely**: All fetchers inherit from `BaseFetcher` for shared functionality
- **Create utility functions**: `generate_stable_string()` handles filename standardization across all fetchers
- **Shared constants**: Use `config.py` values instead of hardcoding paths/settings

### Design Patterns and Principles

#### Template Method Pattern
```python
class BaseFetcher:
    def fetch_and_cache_data(self):  # Template method
        # Common workflow, subclasses override fetch_data()
        if self.should_update():
            data = self.fetch_data()  # Abstract method
            self.save_data(data)      # Common implementation
```

#### Factory Pattern
```python
# fetchers/__init__.py organizes fetcher creation by type
stock_fetchers = [StockHistFetcher, StockInfoFetcher, ...]
fundamentals_fetchers = [DividendFetcher, EarningsFetcher, ...]
```

#### Open/Closed Principle
- **Open for extension**: Add new fetchers by inheriting from `BaseFetcher`
- **Closed for modification**: Core fetcher logic in `BaseFetcher` stays unchanged
- **Plugin architecture**: New data types added via fetcher lists without modifying data classes

#### Single Responsibility Principle
- **BaseFetcher**: Handles caching, file I/O, update logic only
- **StockData/IndexMarket/MarketData**: Manage fetcher collections for their domain
- **Individual fetchers**: Each handles one specific data source/transformation

### Implementation Guidelines
- **Composition over inheritance**: Data classes compose fetchers rather than inheriting data logic
- **Fail gracefully**: Always return empty DataFrame on errors, never raise exceptions to users
- **Immutable where possible**: Use tuple/frozenset for constants, avoid mutable defaults
- **Type hints**: Provide clear interfaces with `typing` annotations for better IDE support