#!/usr/bin/env python3
"""
Test script for new market summary fetchers
"""

from china_stock_data import MarketData

def test_new_market_fetchers():
    """Test the new market summary fetchers"""
    print("Testing new market summary fetchers...")
    
    # Create a market instance
    market = MarketData()
    
    print(f"Total market fetchers available: {len(market.fetchers)}")
    
    # List all available fetchers
    print("\nAll available market data fetchers:")
    for name in sorted(market.fetchers.keys()):
        print(f"  - {name}")
    
    # Test specific new fetchers
    new_fetchers = [
        ("sse_summary", "stock_sse_summary", "上海证券交易所股票数据总貌"),
        ("szse_summary", "stock_szse_summary", "深圳证券交易所市场总貌"),
        ("szse_area_summary", "stock_szse_area_summary", "深圳证券交易所地区交易排序"),
        ("szse_sector_summary", "stock_szse_sector_summary", "深圳证券交易所股票行业成交"),
        ("sse_deal_daily", "stock_sse_deal_daily", "上海证券交易所每日成交概况")
    ]
    
    print("\n--- Testing New Market Summary Fetchers ---")
    for short_name, ak_name, description in new_fetchers:
        short_available = short_name in market.fetchers
        ak_available = ak_name in market.fetchers
        same_instance = short_available and ak_available and (market.fetchers[short_name] is market.fetchers[ak_name])
        
        print(f"{short_name:20} | {ak_name:25} | Short: {'✅' if short_available else '❌'} | AK: {'✅' if ak_available else '❌'} | Same: {'✅' if same_instance else '❌'}")
        print(f"{'':20} | {description}")
        print()

def demo_usage():
    """Demonstrate usage of new fetchers"""
    print("\n--- Usage Examples ---")
    print("# 获取上海证券交易所股票数据总貌")
    print("market = MarketData()")
    print("sse_summary = market.sse_summary")
    print("# 或者使用 AkShare 方法名")
    print("sse_summary = market.stock_sse_summary")
    print()
    
    print("# 获取深圳证券交易所市场总貌")
    print("szse_summary = market.szse_summary")
    print("szse_summary = market.stock_szse_summary")
    print()
    
    print("# 获取地区交易排序")
    print("area_summary = market.szse_area_summary")
    print("area_summary = market.stock_szse_area_summary")
    print()
    
    print("# 获取股票行业成交数据")
    print("sector_summary = market.szse_sector_summary")
    print("sector_summary = market.stock_szse_sector_summary")
    print()
    
    print("# 获取上海证券交易所每日成交概况")
    print("daily_deal = market.sse_deal_daily")
    print("daily_deal = market.stock_sse_deal_daily")

if __name__ == "__main__":
    test_new_market_fetchers()
    demo_usage()
    print("\nTest completed!")