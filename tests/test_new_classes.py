#!/usr/bin/env python3
"""
Test script for the new IndexMarket and MarketData classes
"""

from china_stock_data import IndexMarket, MarketData

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

def test_market_data():
    """Test MarketData class functionality"""
    print("Testing MarketData...")
    
    # Create market instance
    market = MarketData()
    print(f"StockMarket key: {market.key()}")
    
    # List available fetchers
    print("Available market fetchers:")
    for name in market.fetchers:
        print(f"  - {name}")
    
    print()

if __name__ == "__main__":
    test_index_market()
    test_market_data()
    print("Tests completed successfully!")