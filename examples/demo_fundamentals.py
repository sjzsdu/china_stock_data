#!/usr/bin/env python3
"""
Demo script showing how to use fundamentals data in StockData
"""

from china_stock_data import StockData

def demo_fundamentals_usage():
    """Demonstrate fundamentals data usage"""
    print("=== StockData Fundamentals Demo ===")
    
    # Create stock data instance
    stock = StockData("000001")  # 平安银行
    
    print(f"Stock: {stock.symbol}")
    print(f"Data period: {stock.start_date} to {stock.end_date}")
    
    # Show all available fetchers
    print(f"\nTotal fetchers available: {len(stock.fetchers)}")
    
    # Categorize fetchers
    basic_fetchers = []
    fundamentals_fetchers = []
    akshare_methods = []
    
    for name in sorted(stock.fetchers.keys()):
        if name in ["kline", "stock_zh_a_hist", "info", "bid_ask", "chip"]:
            basic_fetchers.append(name)
        elif any(keyword in name for keyword in ["dividend", "earnings", "financial", "repurchase", "share_change", "top_shareholders", "block_trade", "restricted"]):
            fundamentals_fetchers.append(name)
        elif name.startswith("stock_"):
            akshare_methods.append(name)
    
    print(f"\n--- Basic Data Fetchers ({len(basic_fetchers)}) ---")
    for name in basic_fetchers:
        print(f"  - {name}")
    
    print(f"\n--- Fundamentals Data Fetchers ({len(fundamentals_fetchers)}) ---")
    for name in fundamentals_fetchers:
        print(f"  - {name}")
    
    print(f"\n--- Available AkShare Methods ({len(akshare_methods)}) ---")
    print("  (First 10 methods)")
    for name in akshare_methods[:10]:
        print(f"  - {name}")
    if len(akshare_methods) > 10:
        print(f"  ... and {len(akshare_methods) - 10} more")
    
    # Usage examples
    print(f"\n--- Usage Examples ---")
    print("# Basic data access:")
    print("stock.kline                    # Historical price data")
    print("stock.info                     # Stock information")
    print("stock.chip                     # Chip distribution")
    
    print("\n# Fundamentals data access (using business names):")
    print("stock.dividend                 # Dividend information")
    print("stock.earnings                 # Earnings reports")
    print("stock.financial_statements     # Financial statements")
    print("stock.top_shareholders         # Top shareholders")
    print("stock.block_trade             # Block trades")
    
    print("\n# Fundamentals data access (using AkShare method names):")
    print("stock.stock_fhps_em           # Same as dividend")
    print("stock.stock_yjbb_em           # Same as earnings")
    print("stock.stock_lrb_em            # Same as financial_statements")
    print("stock.stock_gdfx_free_top_10_em # Same as top_shareholders")
    
    print("\n# Using get_data method:")
    print('stock.get_data("dividend")')
    print('stock.get_data("stock_fhps_em")')

if __name__ == "__main__":
    demo_fundamentals_usage()
    print("\nDemo completed!")