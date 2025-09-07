# API 参考

本节提供完整的API文档，所有内容均从代码注释自动生成。

## 📚 模块概览

| 模块 | 描述 | 主要功能 |
|------|------|----------|
| [StockData](stock-data.md) | 个股数据获取 | K线、实时、基本信息 |
| [StockMarket](stock-market.md) | 市场整体数据 | 股票列表、交易状态 |
| [数据获取器](fetchers.md) | 底层数据获取 | 各类数据源适配 |
| [工具类](utils.md) | 辅助工具 | 缓存、时间、配置 |

## 🎯 快速导航

### 常用类

::: china_stock_data.StockData
    options:
      members: false
      show_root_heading: false
      show_source: false

::: china_stock_data.StockMarket
    options:
      members: false
      show_root_heading: false
      show_source: false

### 核心方法

#### StockData.get_data()
获取指定类型的股票数据。

**支持的数据类型:**
- `"kline"` - K线历史数据
- `"realtime"` - 实时行情数据  
- `"info"` - 公司基本信息
- `"chip"` - 筹码分布数据

#### StockMarket.get_data()
获取指定类型的市场数据。

**支持的数据类型:**
- `"index_components"` - 指数成分股
- `"index_list"` - 指数列表
- `"sentiment"` - 市场情绪
- `"us_index"` - 美股指数

## 🔧 配置选项

### 缓存配置

缓存系统会自动管理数据的存储和更新，你可以通过以下方式控制缓存行为：

```python
from china_stock_data import StockData

# 创建实例时会自动使用缓存
stock = StockData("000001")

# 强制刷新缓存 (通过重新获取数据)
data = stock.get_data("kline")  # 会检查缓存时效性
```

### 时间配置

系统会自动识别交易时间，在非交易时间优先使用缓存数据：

- **交易时间**: 工作日 9:30-11:30, 13:00-15:00
- **非交易时间**: 使用最近的缓存数据
- **数据更新**: 交易时间内定期检查数据时效性

## ⚠️ 重要说明

!!! warning "数据源限制"
    - 数据来源于第三方接口，可能存在延迟或不可用
    - 请合理控制请求频率，避免被限制访问
    - 生产环境建议加入适当的错误处理和重试机制

!!! tip "最佳实践"
    - 使用适当的日期范围避免获取过多数据
    - 利用缓存机制提高程序性能
    - 在批量处理时注意请求间隔

!!! info "版本兼容性"
    - 支持 Python 3.8+
    - 所有公开API保持向后兼容
    - 新增功能会在版本更新日志中说明
