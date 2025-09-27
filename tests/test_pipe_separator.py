#!/usr/bin/env python3
"""
Test script for the improved fetcher name handling with "|" separator
"""

from china_stock_data import StockData

def test_pipe_separator():
    """Test the pipe separator functionality"""
    print("Testing pipe separator functionality...")
    
    # Create a stock data instance
    stock = StockData("000001")
    
    print("Available fetchers:")
    for name in sorted(stock.fetchers.keys()):
        print(f"  - {name}")
    
    # Test if both "kline" and "stock_zh_a_hist" work
    if "kline" in stock.fetchers:
        print("\n✅ 'kline' key is available")
    else:
        print("\n❌ 'kline' key is missing")
        
    if "stock_zh_a_hist" in stock.fetchers:
        print("✅ 'stock_zh_a_hist' key is available")
    else:
        print("❌ 'stock_zh_a_hist' key is missing")
    
    # Check if they reference the same instance
    if "kline" in stock.fetchers and "stock_zh_a_hist" in stock.fetchers:
        if stock.fetchers["kline"] is stock.fetchers["stock_zh_a_hist"]:
            print("✅ Both keys reference the same fetcher instance")
        else:
            print("❌ Keys reference different instances")

if __name__ == "__main__":
    test_pipe_separator()
    print("\nTest completed!")