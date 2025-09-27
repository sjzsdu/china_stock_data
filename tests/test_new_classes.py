#!/usr/bin/env python3
"""
Test script for the new IndexMarket and StockMarket classes
"""

from china_stock_data import IndexMarket, StockMarket

def test_index_market():
    """Test IndexMarket class functionality"""
    print("Testing IndexMarket...")
    
    # Test with index code
    index_market = IndexMarket(index="000300")
    print(f"IndexMarket key: {index_market.key()}")
    
    # List available fetchers
    print("Available index fetchers:")
    for name in index_market.fetchers:
        print(f"  - {name}")
    
    print()

def test_stock_market():
    """Test StockMarket class functionality"""
    print("Testing StockMarket...")
    
    # Create market instance
    market = StockMarket()
    print(f"StockMarket key: {market.key()}")
    
    # List available fetchers
    print("Available market fetchers:")
    for name in market.fetchers:
        print(f"  - {name}")
    
    print()

if __name__ == "__main__":
    test_index_market()
    test_stock_market()
    print("Tests completed successfully!")