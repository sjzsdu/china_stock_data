#!/usr/bin/env python3
"""
Quick test to verify fundamentals fetchers are available in StockData
"""

from china_stock_data import StockData

def test_fundamentals_availability():
    """Test if fundamentals fetchers are available in StockData"""
    print("Testing fundamentals fetchers availability in StockData...")
    
    # Create a stock data instance
    stock = StockData("000001")
    
    # List of expected fundamentals fetchers
    expected_fundamentals = [
        # Short names
        "block_trade", "dividend", "earnings", "financial_statements",
        "repurchase", "restricted_release", "share_change", "top_shareholders",
        # AkShare method names
        "stock_block_trade_big_em", "stock_fhps_em", "stock_yjbb_em", "stock_yjyg_em",
        "stock_lrb_em", "stock_zcfz_em", "stock_xjll_em", "stock_repurchase_em",
        "stock_restricted_release_queue_em", "stock_share_change_em", "stock_gdfx_free_top_10_em"
    ]
    
    print("\nChecking available fetchers:")
    all_fetchers = sorted(stock.fetchers.keys())
    print(f"Total fetchers available: {len(all_fetchers)}")
    
    # Group fetchers by type
    stock_basic = [f for f in all_fetchers if f in ["kline", "stock_zh_a_hist", "info", "bid_ask", "chip"]]
    fundamentals = [f for f in all_fetchers if any(keyword in f for keyword in ["dividend", "earnings", "financial", "repurchase", "share_change", "top_shareholders", "block_trade", "restricted"])]
    akshare_methods = [f for f in all_fetchers if f.startswith("stock_")]
    
    print(f"\nStock basic fetchers: {stock_basic}")
    print(f"Fundamentals fetchers: {fundamentals}")
    print(f"AkShare method names: {len(akshare_methods)} total")
    
    # Test specific fundamentals fetchers
    print("\n--- Testing Fundamentals Fetchers ---")
    fundamentals_tests = [
        ("dividend", "stock_fhps_em"),
        ("earnings", "stock_yjbb_em"),
        ("financial_statements", "stock_lrb_em"),
        ("top_shareholders", "stock_gdfx_free_top_10_em"),
        ("block_trade", "stock_block_trade_big_em")
    ]
    
    for short_name, ak_name in fundamentals_tests:
        short_available = short_name in stock.fetchers
        ak_available = ak_name in stock.fetchers
        same_instance = short_available and ak_available and (stock.fetchers[short_name] is stock.fetchers[ak_name])
        
        print(f"{short_name:20} | {ak_name:30} | Short: {'✅' if short_available else '❌'} | AK: {'✅' if ak_available else '❌'} | Same: {'✅' if same_instance else '❌'}")

if __name__ == "__main__":
    test_fundamentals_availability()
    print("\nTest completed!")