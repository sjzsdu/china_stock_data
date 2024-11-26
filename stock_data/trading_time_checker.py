import akshare as ak
from datetime import datetime
from .persistent_dict import app_dict

class TradingTimeChecker:

    @classmethod
    def load_trade_dates(cls):
        current_year = datetime.now().year
        cached_year = app_dict.get('year')
        trade_dates = app_dict.get('trade_dates')

        if cached_year != current_year or trade_dates is None:
            trade_dates_df = ak.tool_trade_date_hist_sina()
            trade_dates = trade_dates_df['trade_date'].astype(str).values.tolist()
            app_dict.set('year', current_year)
            app_dict.set('trade_dates', trade_dates)

        return trade_dates

    @classmethod
    def is_trading_time(cls, time_str=None):
        if time_str is not None:
            current_time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        else:
            current_time = datetime.now()
        
        today = current_time.strftime('%Y-%m-%d')
        trade_dates = cls.load_trade_dates()
        
        if today not in trade_dates:
            return False
        
        current_hour = current_time.hour
        current_minute = current_time.minute
        trading_hours = (9 <= current_hour < 11) or (current_hour == 11 and current_minute <= 30) or (13 <= current_hour < 15)
        
        return trading_hours

    @classmethod
    def get_nearest_trade_date(cls, date_str=None):
        if date_str is not None:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        else:
            date = datetime.now()
        
        trade_dates = cls.load_trade_dates()
        trade_date_objs = [datetime.strptime(d, '%Y-%m-%d') for d in trade_dates]
        valid_trade_dates = [d for d in trade_date_objs if d <= date]
        
        if not valid_trade_dates:
            raise ValueError("No trading dates found before the given date.")
        
        nearest_trade_date = max(valid_trade_dates)
        return nearest_trade_date.strftime('%Y-%m-%d') 
    
    @classmethod
    def compare_with_nearest_trade_date(cls, compare_date_str, date_str=None):
        nearest_trade_date_str = cls.get_nearest_trade_date(date_str)
        nearest_trade_date = datetime.strptime(nearest_trade_date_str, '%Y-%m-%d')
        compare_date = datetime.strptime(compare_date_str, '%Y-%m-%d')
        return compare_date >= nearest_trade_date