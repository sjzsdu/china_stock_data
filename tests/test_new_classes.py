"""
Test script for the new IndexData and MarketData classes
"""

from china_stock_data import IndexData, MarketData

def test_index_market():
    """Test IndexData class functionality"""
    print("Testing IndexData...")
    
    # Test with index parameter
    index_market = IndexData(index="000300")
    print(f"IndexData key: {index_market.key()}")
    
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