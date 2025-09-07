# 快速开始

本指南将帮助你在5分钟内掌握 China Stock Data 的基础用法。

## 📦 安装

=== "pip"
    ```bash
    pip install china_stock_data
    ```

=== "poetry"
    ```bash
    poetry add china_stock_data
    ```

=== "conda"
    ```bash
    conda install -c conda-forge china_stock_data
    ```

## 🎯 核心概念

### StockData - 个股数据类

用于获取单只股票的各类数据：

- **历史数据** - K线、价格、成交量
- **实时数据** - 当前价格、买卖盘
- **基本信息** - 公司概况、财务指标
- **技术指标** - 筹码分布等

### StockMarket - 市场数据类

用于获取市场整体数据：

- **指数数据** - 指数列表、成分股
- **市场情绪** - 情绪指标、热点板块
- **国际市场** - 美股指数等

## 💡 基础用法

### 1. 获取股票历史数据

```python
from china_stock_data import StockData

# 创建股票实例
stock = StockData("000001", days=100)  # 平安银行最近100天

# 获取K线数据
kline = stock.get_data("kline")
print(f"数据范围: {kline.index.min()} 到 {kline.index.max()}")
print(f"最新收盘价: ¥{kline['收盘'].iloc[-1]:.2f}")

# 查看数据结构
print(kline.head())
```

### 2. 获取实时数据

```python
# 获取实时行情
realtime = stock.get_data("realtime")
if not realtime.empty:
    print("实时行情:")
    print(realtime)
else:
    print("非交易时间，无实时数据")
```

### 3. 获取公司信息

```python
# 获取公司基本信息
info = stock.get_data("info")
print("公司信息:")
print(info)
```

### 4. 市场数据获取

```python
from china_stock_data import StockMarket

# 创建市场实例
market = StockMarket("000300")  # 沪深300指数

# 获取指数成分股
components = market.get_data("index_components")
print(f"沪深300成分股数量: {len(components)}")
print("前5只成分股:")
print(components.head())

# 获取所有指数列表
index_list = market.get_data("index_list")
print(f"可用指数数量: {len(index_list)}")
```

### 5. 市场情绪分析

```python
# 获取市场情绪数据
market = StockMarket()
sentiment = market.get_data("sentiment")
print("市场情绪指标:")
print(sentiment)
```

## 🔧 常用参数

### StockData 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | 必填 | 股票代码 (如: "000001") |
| `days` | int | 100 | 获取的交易日天数 |
| `start_date` | str | None | 开始日期 (格式: "2023-01-01") |
| `end_date` | str | None | 结束日期 |
| `period` | str | "daily" | 数据周期 |
| `adjust` | str | "qfq" | 复权方式 |

### StockMarket 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `index` | str | None | 指数代码 (如: "000300") |
| `symbol` | str | None | 股票代码 (兼容参数) |

## ⚠️ 注意事项

!!! warning "数据可用性"
    - 部分数据仅在交易时间可用
    - 不同股票的数据完整性可能不同
    - 网络问题可能导致数据获取失败

!!! tip "性能优化"
    - 使用合理的 `days` 参数避免获取过多数据
    - 利用缓存机制减少重复请求
    - 批量处理时考虑请求频率限制

!!! info "错误处理"
    ```python
    try:
        data = stock.get_data("kline")
        if data.empty:
            print("数据为空")
        else:
            print(f"获取到 {len(data)} 条数据")
    except Exception as e:
        print(f"数据获取失败: {e}")
    ```

## 🎯 下一步

现在你已经掌握了基础用法，可以继续学习：

- [📊 基础使用示例](examples/basic.md) - 学习基本数据获取方法
- [📖 完整API参考](api/index.md) - 深入了解所有功能
