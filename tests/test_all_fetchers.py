#!/usr/bin/env python3
"""
Test script for all fetchers with improved name handling
"""

from china_stock_data import StockData, IndexData, MarketData

def test_stock_fetchers():
    """Test stock data fetchers with pipe separator names"""
    print("=== Testing Stock Data Fetchers ===")
    
    stock = StockData("000001")
    
    print("Available stock fetchers:")
    for name in sorted(stock.fetchers.keys()):
        print(f"  - {name}")
    
    # Test some key fetchers
    print("\n--- Testing Stock History Fetcher ---")
    if "kline" in stock.fetchers and "stock_zh_a_hist" in stock.fetchers:
        if stock.fetchers["kline"] is stock.fetchers["stock_zh_a_hist"]:
            print("✅ kline and stock_zh_a_hist reference the same instance")
    
    # Test fundamentals fetchers
    print("\n--- Testing Fundamentals Fetchers ---")
    fundamentals_tests = [
        ("dividend", "stock_fhps_em"),
        ("earnings", "stock_yjbb_em"),
        ("financial_statements", "stock_lrb_em"),
        ("repurchase", "stock_repurchase_em"),
        ("top_shareholders", "stock_gdfx_free_top_10_em")
    ]
    
    for short_name, ak_name in fundamentals_tests:
        if short_name in stock.fetchers and ak_name in stock.fetchers:
            if stock.fetchers[short_name] is stock.fetchers[ak_name]:
                print(f"✅ {short_name} and {ak_name} reference the same instance")
        elif short_name in stock.fetchers:
            print(f"✅ {short_name} is available")

def test_index_fetchers():
    """Test index market fetchers with pipe separator names"""
    print("\n=== Testing Index Market Fetchers ===")
    
    index_market = IndexData(index="000300")
    
    print("Available index fetchers:")
    for name in sorted(index_market.fetchers.keys()):
        print(f"  - {name}")
    
    # Test index fetchers
    index_tests = [
        ("index_components", "index_stock_cons_csindex"),
        ("index_list", "index_stock_info"),
        ("us_index", "index_us_stock_sina")
    ]
    
    for short_name, ak_name in index_tests:
        if short_name in index_market.fetchers and ak_name in index_market.fetchers:
            if index_market.fetchers[short_name] is index_market.fetchers[ak_name]:
                print(f"✅ {short_name} and {ak_name} reference the same instance")
        elif short_name in index_market.fetchers:
            print(f"✅ {short_name} is available")

def test_market_fetchers():
    """Test market fetchers with pipe separator names"""
    print("\n=== Testing Market Fetchers ===")
    
    market = MarketData()
    
    print("Available market fetchers:")
    for name in sorted(market.fetchers.keys()):
        print(f"  - {name}")
    
    # Test market fetchers
    market_tests = [
        ("lhb", "stock_lhb_detail_em"),
        ("margin_financing", "stock_margin_sse"),
        ("northbound_holdings", "stock_hsgt_hold_stock_em"),
        ("market_sentiment", "index_news_sentiment_scope")
    ]
    
    for short_name, ak_name in market_tests:
        if short_name in market.fetchers and ak_name in market.fetchers:
            if market.fetchers[short_name] is market.fetchers[ak_name]:
                print(f"✅ {short_name} and {ak_name} reference the same instance")
        elif short_name in market.fetchers:
            print(f"✅ {short_name} is available")

if __name__ == "__main__":
    test_stock_fetchers()
    test_index_fetchers()
    test_market_fetchers()
    print("\nAll tests completed!")