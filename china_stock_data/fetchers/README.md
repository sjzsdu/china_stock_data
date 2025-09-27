# Fetchers Architecture Documentation

## Overview

The fetcher system in china_stock_data follows a parameter delegation pattern where data entry classes (StockData, MarketData, IndexMarket) serve as parameter managers and sources, while individual fetchers handle the actual data retrieval logic.

## Architecture Pattern: Parameter Delegation

### Core Design Principle

**Entry classes are parameter builders and managers**, not direct data providers. They:
1. Accept user parameters during initialization
2. Store and manage these parameters as instance attributes
3. Pass themselves as parameter sources to fetchers
4. Provide unified access methods that delegate to appropriate fetchers

**Fetchers are data specialists** that:
1. Receive the entry class instance during initialization
2. Extract required parameters from the entry class when fetching data
3. Handle akshare method calls with properly formatted parameters
4. Implement data-specific logic and caching strategies

### Parameter Flow Architecture

```
User Input → Entry Class (Parameter Management) → Fetcher (Data Retrieval) → akshare API
           ↓                                    ↓
    [StockData]                        [Individual Fetcher]
    [MarketData]         →             [SSESummaryFetcher]
    [IndexMarket]                      [StockHistFetcher]
                                       [DividendFetcher]
                                       [...]
```

## Entry Classes Responsibilities

### 1. Parameter Construction and Validation
Entry classes handle all parameter logic:
- Accept parameters from users (dates, symbols, periods, etc.)
- Convert and normalize parameter formats (YYYY-MM-DD → YYYYMMDD)
- Set reasonable defaults for optional parameters
- Validate parameter combinations and ranges

### 2. Parameter Storage and Management
Store parameters as instance attributes for fetcher access:
```python
class MarketData:
    def __init__(self, date=None, symbol="当月"):
        self.date = date or datetime.now().strftime('%Y%m%d')
        self.symbol = symbol
        self.formatted_date_yyyymm = self.date[:6]  # For month-based APIs
        # ... other parameter derivatives
```

### 3. Fetcher Initialization and Registry
- Create fetcher instances and pass self as parameter source
- Maintain fetcher registry with multi-name support (pipe-separated names)
- Handle fetcher lifecycle and instance management

## Fetcher Implementation Requirements

### 1. Parameter Extraction Pattern
Fetchers must extract parameters from the entry class instance, not from method arguments:

```python
class SSESummaryFetcher(BaseFetcher):
    def __init__(self, market_data):
        self.market_data = market_data  # Store reference to parameter source
        # ... initialization logic
    
    def fetch_data(self, **kwargs) -> pd.DataFrame:
        # EXTRACT parameters from entry class, NOT from kwargs
        date = self.market_data.date
        symbol = self.market_data.symbol
        
        # Handle parameter format conversion if needed
        if len(date) == 10 and '-' in date:  # YYYY-MM-DD → YYYYMMDD
            date = date.replace('-', '')
        
        # Call akshare with extracted parameters
        return ak.stock_szse_summary(date=date)
```

### 2. Parameter Format Handling
Different akshare methods require different date formats:
- `stock_sse_summary()`: No parameters
- `stock_szse_summary(date='20240830')`: YYYYMMDD format
- `stock_szse_area_summary(date='202203')`: YYYYMM format
- `stock_szse_sector_summary(symbol='当月', date='202501')`: YYYYMM + symbol

Fetchers must handle format conversion:
```python
def fetch_data(self, **kwargs) -> pd.DataFrame:
    # Extract from entry class
    raw_date = self.market_data.date
    
    # Convert to required format
    if self.requires_yyyymm_format():
        date = raw_date[:6] if len(raw_date) == 8 else raw_date.replace('-', '')[:6]
    else:
        date = raw_date.replace('-', '') if '-' in raw_date else raw_date
    
    return ak.target_method(date=date)
```

### 3. Error Handling and Pre-formatted Parameters
Fetchers use pre-formatted parameters from entry class with graceful error handling:
```python
def fetch_data(self) -> pd.DataFrame:
    try:
        # Get pre-formatted parameters from entry class instance
        date = self.market_data.date_yyyymmdd  # For YYYYMMDD APIs
        # OR
        date = self.market_data.date_yyyymm   # For YYYYMM APIs
        symbol = self.market_data.symbol
        
        # Direct API call with pre-formatted parameters
        return ak.target_method(date=date, symbol=symbol)
        
    except Exception:
        return pd.DataFrame()  # Always return empty DataFrame on error
```

## Multi-Name Support Implementation

Fetchers support multiple access names via pipe-separated naming:
```python
class SSESummaryFetcher(BaseFetcher):
    name = "sse_summary|stock_sse_summary"  # business_name|akshare_method_name
```

Entry classes split names and create multiple dictionary entries:
```python
for fetcher in market_fetchers:
    fetcher_instance = fetcher(self)
    if "|" in fetcher.name:
        names = fetcher.name.split("|")
        for name in names:
            self.fetchers[name.strip()] = fetcher_instance
    else:
        self.fetchers[fetcher.name] = fetcher_instance
```

## Simplified Parameter Access

The system uses a simplified approach where fetchers get all parameters from the entry class instance:

```python
# Usage: parameters set during initialization
market = MarketData(date='2024-08-30', symbol='本月')
data = market.szse_summary  # Uses market.date_yyyymmdd
data = market.szse_sector_summary  # Uses market.date_yyyymm and market.symbol

# All access methods work the same way
data1 = market.sse_summary
data2 = market.get_data('sse_summary')  # Equivalent to above
```

## Implementation Checklist

### For Entry Classes:
- [x] Accept all relevant parameters in `__init__`
- [x] Store parameters as instance attributes with defaults
- [x] Provide parameter format derivatives (date_yyyymm, date_yyyymmdd, etc.)
- [x] Initialize fetchers with `self` as parameter source
- [x] Implement simplified `get_data()` method without parameter overrides

### For Fetchers:
- [x] Store entry class reference in `__init__`
- [x] Extract parameters from entry class in `fetch_data()`
- [x] Handle parameter format automatically using pre-formatted attributes
- [x] Provide graceful error handling with empty DataFrame fallback
- [x] Use multi-name pattern with pipe separator

### For BaseFetcher:
- [x] Simplified `fetch_and_cache_data()` without kwargs
- [x] Standard `fetch_data()` signature without parameters
- [x] Maintain full backward compatibility

## Benefits of This Architecture

1. **Separation of Concerns**: Entry classes manage parameters, fetchers handle data
2. **Flexibility**: Support both default parameters and runtime overrides  
3. **Consistency**: Unified parameter handling across all data types
4. **Maintainability**: Clear responsibility boundaries
5. **Extensibility**: Easy to add new parameters and fetchers
6. **User-Friendly**: Simple interface with sensible defaults

This architecture ensures that parameter management is centralized in entry classes while keeping data fetching logic specialized and focused in individual fetchers.
