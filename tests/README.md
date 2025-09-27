# Tests Directory

This directory contains all test files for the china_stock_data project.

## Running Tests

### Individual Test Files

To run individual test files, use one of the following methods:

```bash
# From project root directory
cd /path/to/china_stock_data

# Method 1: Using PYTHONPATH
PYTHONPATH=. python tests/test_basic_functionality.py
PYTHONPATH=. python tests/test_fundamentals_availability.py
PYTHONPATH=. python tests/test_all_fetchers.py

# Method 2: Using pytest (recommended)
python -m pytest tests/test_basic_functionality.py -v
python -m pytest tests/ -v  # Run all tests
```

### All Tests

```bash
# Run all tests with pytest
python -m pytest tests/ -v

# Run specific test patterns
python -m pytest tests/test_*functionality*.py -v
```

## Test Files

- `test_basic_functionality.py` - Basic imports and initialization tests
- `test_fundamentals_availability.py` - Fundamentals fetchers availability tests  
- `test_all_fetchers.py` - Comprehensive test for all fetcher types
- `test_market_fetchers.py` - Market-specific fetcher tests
- `test_pipe_separator.py` - Pipe separator functionality tests
- `test_new_classes.py` - Tests for IndexMarket and StockMarket classes

## Note

When running tests from the project root, make sure to set `PYTHONPATH=.` to ensure proper module imports.