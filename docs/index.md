# China Stock Data

<div align="center">

**🇨🇳 一个现代化的中国股市数据获取库**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/china_stock_data.svg)](https://pypi.org/project/china_stock_data/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://github.com/sjzsdu/china_stock_data/workflows/CI/badge.svg)](https://github.com/sjzsdu/china_stock_data/actions)

</div>

## 🌟 特性亮点

🎯 **智能数据获取** - 基于 AkShare 的现代化封装  
⚡ **智能缓存机制** - 交易时间感知的数据缓存  
🔄 **数据持久化** - 自动数据存储与管理  
📊 **多维度分析** - 支持个股、指数、市场情绪等多角度数据  
🛡️ **类型安全** - 完整的类型提示，IDE友好  
🧪 **高测试覆盖** - 95%+ 测试覆盖率，可靠稳定  

## 🚀 快速体验

### 安装

```bash
pip install china_stock_data
```

### 30秒上手

```python
from china_stock_data import StockData, StockMarket

# 获取股票数据
stock = StockData("000001", days=30)  # 平安银行最近30天
price_data = stock.get_data("kline")
print(f"最新价格: ¥{price_data['收盘'].iloc[-1]:.2f}")

# 获取市场数据
market = StockMarket("000300")  # 沪深300指数
components = market.get_data("index_components")
print(f"成分股数量: {len(components)}")
```

## 📖 核心概念

### StockData - 个股数据
用于获取单只股票的各类数据，包括历史价格、实时行情、公司信息等。

### StockMarket - 市场数据
用于获取市场层面的数据，包括指数信息、市场情绪、成分股等。

### 智能缓存
- 🕐 **交易时间感知** - 非交易时间优先使用缓存
- ⚡ **频率控制** - 防止过度请求
- 🔄 **自动更新** - 数据时效性检查

## 🎯 使用场景

- 📈 **量化投资** - 历史数据回测、策略开发
- 🔍 **投资研究** - 基本面分析、技术分析
- 📊 **数据分析** - 市场研究、学术研究
- 🤖 **自动化交易** - 实时数据获取、信号生成

## 🔗 快速导航

- [📚 快速开始](getting-started.md) - 5分钟学会基础用法
- [📖 API 参考](api/index.md) - 完整的API文档
- [💡 示例教程](examples/basic.md) - 实战案例和最佳实践
- [🤝 贡献指南](contributing.md) - 参与项目开发

## 🙏 致谢

感谢 [AkShare](https://github.com/jindaxiang/akshare) 提供优秀的数据接口。
