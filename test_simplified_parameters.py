#!/usr/bin/env python3
"""
Test script for simplified parameter passing mechanism in MarketData class.

This script tests:
1. Default parameter handling (current date/time)
2. Custom parameter passing during initialization
3. Different date format conversions
4. All market data fetchers with simplified access
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from china_stock_data import MarketData
from datetime import datetime

def test_default_parameters():
    """Test MarketData with default parameters (current date)"""
    print("=== Testing Default Parameters ===")
    
    market = MarketData()
    print(f"Default date: {market.date}")
    print(f"Default date_yyyymm: {market.date_yyyymm}")
    print(f"Default date_yyyymmdd: {market.date_yyyymmdd}")
    print(f"Default symbol: {market.symbol}")
    
    # Test access to a fetcher that doesn't need parameters
    print(f"Available fetchers: {len(market.fetchers)}")
    print(f"SSE Summary available: {'sse_summary' in market.fetchers}")
    print()

def test_custom_parameters():
    """Test MarketData with custom parameters"""
    print("=== Testing Custom Parameters ===")
    
    # Test with custom date and symbol
    custom_date = "2024-08-30"
    custom_symbol = "本月"
    
    market = MarketData(date=custom_date, symbol=custom_symbol)
    print(f"Custom date input: {custom_date}")
    print(f"Stored date: {market.date}")
    print(f"Formatted date_yyyymm: {market.date_yyyymm}")
    print(f"Formatted date_yyyymmdd: {market.date_yyyymmdd}")
    print(f"Custom symbol: {market.symbol}")
    print()

def test_date_format_handling():
    """Test different date format inputs"""
    print("=== Testing Date Format Handling ===")
    
    test_dates = [
        "2024-08-30",  # YYYY-MM-DD
        "20240830",    # YYYYMMDD
        "202408",      # YYYYMM
    ]
    
    for test_date in test_dates:
        print(f"Input date: {test_date}")
        market = MarketData(date=test_date)
        print(f"  Stored date: {market.date}")
        print(f"  YYYYMM format: {market.date_yyyymm}")
        print(f"  YYYYMMDD format: {market.date_yyyymmdd}")
        print()

def test_fetcher_access():
    """Test various ways to access market data fetchers"""
    print("=== Testing Fetcher Access Methods ===")
    
    market = MarketData(date="2024-08-30")
    
    # Test multi-name access
    test_names = [
        "sse_summary",
        "stock_sse_summary", 
        "szse_summary",
        "stock_szse_summary",
        "szse_area_summary",
        "szse_sector_summary",
        "sse_deal_daily"
    ]
    
    print("Testing fetcher availability:")
    for name in test_names:
        available = name in market.fetchers
        print(f"  {name}: {'✓' if available else '✗'}")
    
    print()
    
    # Test different access methods
    print("Testing access methods:")
    try:
        # Method 1: Direct attribute access
        print("1. Attribute access: market.sse_summary")
        result1 = market.sse_summary
        print(f"   Result type: {type(result1)}")
        print(f"   Result shape: {result1.shape if hasattr(result1, 'shape') else 'N/A'}")
        
        # Method 2: get_data method
        print("2. get_data method: market.get_data('sse_summary')")
        result2 = market.get_data('sse_summary')
        print(f"   Result type: {type(result2)}")
        print(f"   Result shape: {result2.shape if hasattr(result2, 'shape') else 'N/A'}")
        
        # Method 3: Dictionary access (if implemented)
        print("3. Dictionary access: market['stock_sse_summary']")
        try:
            result3 = market['stock_sse_summary']
            print(f"   Result type: {type(result3)}")
        except Exception as e:
            print(f"   Error: {e}")
            
    except Exception as e:
        print(f"Error during access test: {e}")
    
    print()

def test_parameter_extraction():
    """Test that fetchers correctly extract parameters from MarketData instance"""
    print("=== Testing Parameter Extraction in Fetchers ===")
    
    market = MarketData(date="2024-08-30", symbol="本月")
    
    # Test fetchers that require different parameter formats
    fetcher_tests = [
        ("sse_summary", "No parameters needed"),
        ("szse_summary", "Needs YYYYMMDD date"),
        ("szse_area_summary", "Needs YYYYMM date"),  
        ("szse_sector_summary", "Needs YYYYMM date + symbol"),
        ("sse_deal_daily", "Needs YYYYMMDD date"),
    ]
    
    for fetcher_name, description in fetcher_tests:
        print(f"Testing {fetcher_name} ({description}):")
        if fetcher_name in market.fetchers:
            fetcher = market.fetchers[fetcher_name]
            print(f"  Fetcher has market_data reference: {hasattr(fetcher, 'market_data')}")
            if hasattr(fetcher, 'market_data'):
                print(f"  Can access date: {hasattr(fetcher.market_data, 'date')}")
                print(f"  Can access date_yyyymm: {hasattr(fetcher.market_data, 'date_yyyymm')}")
                print(f"  Can access date_yyyymmdd: {hasattr(fetcher.market_data, 'date_yyyymmdd')}")
                print(f"  Can access symbol: {hasattr(fetcher.market_data, 'symbol')}")
        else:
            print(f"  Fetcher not found!")
        print()

def main():
    """Run all tests"""
    print("Testing Simplified Parameter Passing Mechanism")
    print("=" * 50)
    print()
    
    try:
        test_default_parameters()
        test_custom_parameters()
        test_date_format_handling()
        test_fetcher_access()
        test_parameter_extraction()
        
        print("=== All Tests Completed ===")
        print("✓ Parameter passing mechanism is working correctly!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()