import akshare as ak
from ..base_fetcher import BaseFetcher
import pandas as pd
from datetime import datetime
from typing import Any
from china_stock_data.config import CACHE_PATH, CSV_EXT
from china_stock_data.utils import generate_stable_string

class StockHistFetcher(BaseFetcher):
    """
    获取股票的日线数据
    """
    name = "kline"
    def __init__(self, stock_data: Any):
        self.stock_data = stock_data
        original_file = f"{StockHistFetcher.name}_{stock_data.days_key}_{stock_data.period}_{stock_data.adjust}"
        file = generate_stable_string(original_file) + CSV_EXT
        path = f"{CACHE_PATH}/{stock_data.symbol}/{file}"
        
        super().__init__(path = path)
        self.factors = {}
        
    def fetch_data(self):
        start_date_formatted = datetime.strptime(self.stock_data.start_date, '%Y-%m-%d').strftime('%Y%m%d')
        end_date_formatted = datetime.strptime(self.stock_data.end_date, '%Y-%m-%d').strftime('%Y%m%d')
        # try:
        print("Fetching stock history data!", self.stock_data.symbol)
        data = ak.stock_zh_a_hist(
            symbol=self.stock_data.symbol,
            period=self.stock_data.period,
            start_date=start_date_formatted,
            end_date=end_date_formatted,
            adjust=self.stock_data.adjust
        )
        if data is None or data.empty:
            raise ValueError("No data returned from the API.")
        self.handle_data(data)
        return data
        # except Exception as e:
        #     print(f"Error fetching data: {e}")
        #     return pd.DataFrame()
        
    def handle_data(self, data: pd.DataFrame):
        # 计算最高、最低和平均值
        self.factors['最高'] = data['最高'].max()
        self.factors['最低'] = data['最低'].min()
        self.factors['平均'] = (self.factors['最高'] + self.factors['最低']) / 2
        data['平均'] = (data['最低'] + data['最高']) / 2  
        data['加权平均'] = data['成交额'] / data['成交量'] / 100     
        self.factors['加权平均'] = (data['平均'] * data['成交量']).sum() / data['成交量'].sum()
        
        first = data.iloc[0]
        last = data.iloc[-1]
        self.factors['涨跌额'] = last['收盘'] - first['收盘']
        self.factors['涨跌幅'] = (last['收盘'] - first['收盘']) * 100 / first['收盘']
        
        

        
    def __getitem__(self, key):
        if key in self.factors:
            return self.factors[key]
        else :
            raise KeyError(f"Key '{key}' not found in DataFrame")
        
