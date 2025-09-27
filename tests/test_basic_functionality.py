#!/usr/bin/env python3
"""
Simple functional test to ensure no import or basic usage errors
"""

def test_imports_and_basic_usage():
    """Test imports and basic usage without actual data fetching"""
    print("Testing imports and basic initialization...")
    
    # Test imports
    from china_stock_data import StockData, IndexMarket, StockMarket
    print("✅ All imports successful")
    
    # Test StockData initialization
    stock = StockData("000001")
    print(f"✅ StockData initialized: {len(stock.fetchers)} fetchers available")
    assert len(stock.fetchers) > 0, "StockData should have fetchers"
    
    # Test IndexMarket initialization  
    index = IndexMarket(index="000300")
    print(f"✅ IndexMarket initialized: {len(index.fetchers)} fetchers available")
    assert len(index.fetchers) > 0, "IndexMarket should have fetchers"
    
    # Test StockMarket initialization
    market = StockMarket()
    print(f"✅ StockMarket initialized: {len(market.fetchers)} fetchers available")
    assert len(market.fetchers) > 0, "StockMarket should have fetchers"
    
    # Test fetcher access (without actual data fetching)
    assert "dividend" in stock.fetchers, "dividend fetcher should be available"
    assert "stock_fhps_em" in stock.fetchers, "stock_fhps_em fetcher should be available"
    assert stock.fetchers["dividend"] is stock.fetchers["stock_fhps_em"], "Same fetcher should be referenced by different names"
    print("✅ Fetcher access works correctly")
    
    print("✅ All basic tests passed!")

if __name__ == "__main__":
    test_imports_and_basic_usage()
    print("\n🎉 All tests completed successfully! No errors found.")