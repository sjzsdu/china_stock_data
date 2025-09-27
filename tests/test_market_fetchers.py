#!/usr/bin/env python3
"""
Test script for market fetchers with improved name handling
"""

from china_stock_data import StockMarket

def test_market_fetchers():
    """Test the market fetchers with pipe separator names"""
    print("Testing market fetchers with pipe separator functionality...")
    
    # Create a market instance
    market = StockMarket()
    
    print("Available market fetchers:")
    for name in sorted(market.fetchers.keys()):
        print(f"  - {name}")
    
    # Test LHB fetcher
    print("\n=== Testing LHB Fetcher ===")
    if "lhb" in market.fetchers:
        print("✅ 'lhb' key is available")
    if "stock_lhb_detail_em" in market.fetchers:
        print("✅ 'stock_lhb_detail_em' key is available")
    if "lhb" in market.fetchers and "stock_lhb_detail_em" in market.fetchers:
        if market.fetchers["lhb"] is market.fetchers["stock_lhb_detail_em"]:
            print("✅ Both LHB keys reference the same instance")
    
    # Test Margin Financing fetcher
    print("\n=== Testing Margin Financing Fetcher ===")
    margin_keys = ["margin_financing", "stock_margin_sse", "stock_margin_szse"]
    available_keys = []
    for key in margin_keys:
        if key in market.fetchers:
            available_keys.append(key)
            print(f"✅ '{key}' key is available")
    
    if len(available_keys) > 1:
        if all(market.fetchers[available_keys[0]] is market.fetchers[key] for key in available_keys[1:]):
            print("✅ All margin financing keys reference the same instance")
    
    # Test Northbound Holdings fetcher
    print("\n=== Testing Northbound Holdings Fetcher ===")
    if "northbound_holdings" in market.fetchers:
        print("✅ 'northbound_holdings' key is available")
    if "stock_hsgt_hold_stock_em" in market.fetchers:
        print("✅ 'stock_hsgt_hold_stock_em' key is available")
    if "northbound_holdings" in market.fetchers and "stock_hsgt_hold_stock_em" in market.fetchers:
        if market.fetchers["northbound_holdings"] is market.fetchers["stock_hsgt_hold_stock_em"]:
            print("✅ Both northbound keys reference the same instance")
    
    # Test Market Sentiment fetcher
    print("\n=== Testing Market Sentiment Fetcher ===")
    if "market_sentiment" in market.fetchers:
        print("✅ 'market_sentiment' key is available")
    if "index_news_sentiment_scope" in market.fetchers:
        print("✅ 'index_news_sentiment_scope' key is available")
    if "market_sentiment" in market.fetchers and "index_news_sentiment_scope" in market.fetchers:
        if market.fetchers["market_sentiment"] is market.fetchers["index_news_sentiment_scope"]:
            print("✅ Both sentiment keys reference the same instance")

if __name__ == "__main__":
    test_market_fetchers()
    print("\nTest completed!")