# 基础用法示例

本章展示 China Stock Data 的基础使用方法和常见场景。

## 🎯 数据获取基础

### 获取单只股票数据

```python
from china_stock_data import StockData

# 创建股票实例
stock = StockData("000001", days=30)  # 平安银行最近30天

# 获取K线数据
kline = stock.get_data("kline")
print(f"获取到 {len(kline)} 天的数据")
print(f"价格范围: ¥{kline['最低'].min():.2f} - ¥{kline['最高'].max():.2f}")

# 计算基本统计信息
latest_price = kline['收盘'].iloc[-1]
price_change = ((latest_price / kline['收盘'].iloc[0]) - 1) * 100
print(f"最新价格: ¥{latest_price:.2f}")
print(f"期间涨跌: {price_change:+.2f}%")
```

### 批量获取多只股票

```python
# 银行股组合
bank_stocks = ["000001", "600036", "601988", "600000"]
portfolio_data = {}

for symbol in bank_stocks:
    try:
        stock = StockData(symbol, days=100)
        data = stock.get_data("kline")
        if not data.empty:
            portfolio_data[symbol] = data['收盘']
            print(f"✅ {symbol}: {len(data)} 天数据")
        else:
            print(f"❌ {symbol}: 无数据")
    except Exception as e:
        print(f"❌ {symbol}: {e}")

# 合并数据进行对比
import pandas as pd
portfolio_df = pd.DataFrame(portfolio_data)
print("\n投资组合数据:")
print(portfolio_df.head())
```

## 📊 数据分析示例

### 价格趋势分析

```python
import matplotlib.pyplot as plt

# 获取数据
stock = StockData("600519", days=200)  # 贵州茅台
data = stock.get_data("kline")

# 计算移动平均线
data['MA5'] = data['收盘'].rolling(5).mean()
data['MA20'] = data['收盘'].rolling(20).mean()
data['MA60'] = data['收盘'].rolling(60).mean()

# 绘制价格趋势图
plt.figure(figsize=(12, 8))
plt.plot(data.index, data['收盘'], label='收盘价', linewidth=2)
plt.plot(data.index, data['MA5'], label='5日均线', alpha=0.8)
plt.plot(data.index, data['MA20'], label='20日均线', alpha=0.8)
plt.plot(data.index, data['MA60'], label='60日均线', alpha=0.8)

plt.title('股价趋势分析', fontsize=16)
plt.xlabel('日期')
plt.ylabel('价格 (¥)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### 成交量分析

```python
# 成交量与价格关系分析
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# 价格图
ax1.plot(data.index, data['收盘'], label='收盘价')
ax1.set_ylabel('价格 (¥)')
ax1.set_title('价格与成交量分析')
ax1.legend()
ax1.grid(True, alpha=0.3)

# 成交量图
ax2.bar(data.index, data['成交量'], alpha=0.7, color='orange')
ax2.set_ylabel('成交量')
ax2.set_xlabel('日期')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 分析价量关系
volume_price_corr = data['成交量'].corr(data['收盘'])
print(f"成交量与价格相关系数: {volume_price_corr:.3f}")
```

## 🏢 市场数据分析

### 指数成分股分析

```python
from china_stock_data import StockMarket

# 分析沪深300指数
market = StockMarket("000300")
components = market.get_data("index_components")

print(f"沪深300指数包含 {len(components)} 只股票")
print("\n前10只权重股:")
if '权重' in components.columns:
    top_stocks = components.nlargest(10, '权重')
    print(top_stocks[['股票代码', '股票名称', '权重']])
else:
    print(components.head(10))
```

### 市场情绪监控

```python
# 获取市场情绪数据
market = StockMarket()
sentiment = market.get_data("sentiment")

print("当前市场情绪指标:")
if not sentiment.empty:
    print(sentiment)
    
    # 分析情绪变化
    if len(sentiment) > 1:
        numeric_cols = sentiment.select_dtypes(include=[float, int]).columns
        for col in numeric_cols:
            latest = sentiment[col].iloc[-1]
            previous = sentiment[col].iloc[-2] if len(sentiment) > 1 else latest
            change = ((latest / previous) - 1) * 100 if previous != 0 else 0
            print(f"{col}: {latest:.2f} ({change:+.1f}%)")
else:
    print("暂无情绪数据")
```

## 🔍 实时数据监控

### 实时价格监控

```python
import time

def monitor_stock(symbol, duration_minutes=10):
    """监控股票实时价格"""
    stock = StockData(symbol)
    start_time = time.time()
    end_time = start_time + duration_minutes * 60
    
    print(f"开始监控 {symbol} (持续 {duration_minutes} 分钟)...")
    
    while time.time() < end_time:
        try:
            realtime = stock.get_data("realtime")
            if not realtime.empty:
                current_time = time.strftime("%H:%M:%S")
                print(f"[{current_time}] 实时数据更新:")
                print(realtime.head())
            else:
                print(f"[{time.strftime('%H:%M:%S')}] 非交易时间或无实时数据")
            
            time.sleep(30)  # 30秒更新一次
            
        except Exception as e:
            print(f"获取实时数据失败: {e}")
            time.sleep(30)

# 使用示例 (注释掉避免在文档中实际运行)
# monitor_stock("000001", duration_minutes=5)
```

## 📈 技术指标计算

### RSI 指标

```python
def calculate_rsi(prices, period=14):
    """计算RSI指标"""
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

# 应用RSI计算
stock = StockData("000001", days=100)
data = stock.get_data("kline")
data['RSI'] = calculate_rsi(data['收盘'])

# 分析RSI信号
latest_rsi = data['RSI'].iloc[-1]
print(f"当前RSI: {latest_rsi:.2f}")

if latest_rsi > 70:
    print("信号: 超买，考虑卖出")
elif latest_rsi < 30:
    print("信号: 超卖，考虑买入")
else:
    print("信号: 中性")
```

### MACD 指标

```python
def calculate_macd(prices, fast=12, slow=26, signal=9):
    """计算MACD指标"""
    exp1 = prices.ewm(span=fast).mean()
    exp2 = prices.ewm(span=slow).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram

# 应用MACD计算
macd, signal_line, histogram = calculate_macd(data['收盘'])
data['MACD'] = macd
data['MACD_Signal'] = signal_line
data['MACD_Histogram'] = histogram

# 分析MACD信号
latest_macd = data['MACD'].iloc[-1]
latest_signal = data['MACD_Signal'].iloc[-1]

print(f"MACD: {latest_macd:.4f}")
print(f"信号线: {latest_signal:.4f}")

if latest_macd > latest_signal:
    print("MACD信号: 看涨")
else:
    print("MACD信号: 看跌")
```

## 💡 最佳实践

### 错误处理

```python
def safe_get_stock_data(symbol, data_type="kline", max_retries=3):
    """安全获取股票数据，包含重试机制"""
    for attempt in range(max_retries):
        try:
            stock = StockData(symbol)
            data = stock.get_data(data_type)
            
            if data.empty:
                print(f"警告: {symbol} 的 {data_type} 数据为空")
                return None
            
            print(f"成功获取 {symbol} 的 {data_type} 数据")
            return data
            
        except Exception as e:
            print(f"尝试 {attempt + 1}/{max_retries} 失败: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # 等待2秒后重试
            else:
                print(f"获取 {symbol} 数据最终失败")
                return None

# 使用示例
data = safe_get_stock_data("000001", "kline")
if data is not None:
    print(f"成功获取数据，形状: {data.shape}")
```

### 数据缓存利用

```python
# 利用缓存提高效率
symbols = ["000001", "600519", "000002"]

# 第一次获取会从网络加载
print("首次获取数据...")
start_time = time.time()
for symbol in symbols:
    stock = StockData(symbol, days=30)
    data = stock.get_data("kline")
    print(f"{symbol}: {len(data)} 条数据")
first_duration = time.time() - start_time

# 第二次获取会使用缓存
print("\n再次获取数据...")
start_time = time.time()
for symbol in symbols:
    stock = StockData(symbol, days=30)
    data = stock.get_data("kline")
    print(f"{symbol}: {len(data)} 条数据")
second_duration = time.time() - start_time

print(f"\n首次耗时: {first_duration:.2f}秒")
print(f"缓存耗时: {second_duration:.2f}秒")
print(f"提速比: {first_duration/second_duration:.1f}x")
```

这些示例涵盖了库的主要功能和最佳实践，帮助用户快速上手并有效使用。
