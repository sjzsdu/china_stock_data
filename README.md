<div align="center">

# 🇨🇳 China Stock Data

**一个现代化的中国股市数据获取库**

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/china_stock_data.svg)](https://pypi.org/project/china_stock_data/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://github.com/sjzsdu/china_stock_data/workflows/CI/badge.svg)](https://github.com/sjzsdu/china_stock_data/actions)
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)](#)

[🚀 快速开始](#-快速开始) • [📖 文档](#-功能特性) • [💡 示例](#-使用示例) • [🤝 贡献](#-贡献)

</div>

---

## ✨ 功能特性

🎯 **智能数据获取** - 基于 [AkShare](https://github.com/jindaxiang/akshare) 的现代化封装  
⚡ **智能缓存机制** - 交易时间感知的数据缓存，提升访问效率  
🔄 **数据持久化** - 自动数据存储与管理，减少重复请求  
📊 **多维度分析** - 支持个股、指数、市场情绪等多角度数据  
🛡️ **类型安全** - 完整的类型提示，IDE友好的开发体验  
🧪 **测试覆盖** - 95%+ 测试覆盖率，可靠稳定  

## 🚀 快速开始

### 安装

```bash
pip install china_stock_data
```

### 30秒快速体验

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

## 💡 使用示例

### 📈 个股分析

```python
# 技术分析
stock = StockData("600519")  # 贵州茅台
kline = stock.get_data("kline")
realtime = stock.get_data("realtime")

# 计算移动平均线
kline['MA20'] = kline['收盘'].rolling(20).mean()

# 获取公司信息
info = stock.get_data("info")
```

### 🏢 市场分析

```python
# 市场情绪分析
market = StockMarket()
sentiment = market.get_data("sentiment")
index_list = market.get_data("index_list")

# 指数成分股分析
csi300 = StockMarket("000300")
components = csi300.get_data("index_components")
```

### 📊 批量分析

```python
# 投资组合分析
symbols = ["000001", "000002", "600519"]
portfolio = {}

for symbol in symbols:
    stock = StockData(symbol, days=252)
    data = stock.get_data("kline")
    portfolio[symbol] = data['收盘']

# 计算相关性、收益率等...
```

## 📁 项目结构

```
china_stock_data/
├── 📦 fetchers/              # 数据获取器 (按类别组织)
│   ├── 📈 stock/            # 个股数据获取器
│   ├── 📊 index/            # 指数数据获取器
│   ├── 🏢 market/           # 市场数据获取器
│   └── 🔧 base_fetcher.py   # 基础获取器
├── 💾 persistent_dict.py     # 数据持久化
├── ⏰ trading_time_checker.py # 交易时间管理
├── 📈 stock_data.py         # 个股数据类
├── 🏢 stock_market.py       # 市场数据类
└── 📝 examples/             # 使用示例
    ├── quick_start.ipynb    # 5分钟快速入门
    ├── professional_analysis.ipynb  # 专业技术分析
    └── portfolio_analysis.ipynb     # 投资组合管理
```

## 🎓 学习资源

📚 **[完整示例教程](examples/)**
- [🚀 5分钟快速入门](examples/quick_start.ipynb) - 基础功能学习
- [📊 专业技术分析](examples/professional_analysis.ipynb) - 技术指标与图表
- [💼 投资组合管理](examples/portfolio_analysis.ipynb) - 量化分析与风险管理

## 🛠️ 开发

### 环境设置

```bash
# 克隆仓库
git clone https://github.com/sjzsdu/china_stock_data.git
cd china_stock_data

# 安装依赖 (推荐使用 Poetry)
poetry install

# 运行测试
poetry run pytest
```

### API 参考

#### StockData

| 方法 | 说明 | 示例 |
|------|------|------|
| `get_data("kline")` | 获取K线数据 | 历史价格、成交量 |
| `get_data("realtime")` | 获取实时数据 | 当前价格、买卖盘 |
| `get_data("info")` | 获取基本信息 | 公司概况、财务指标 |
| `get_data("chip")` | 获取筹码分布 | 持仓成本分布 |

#### StockMarket

| 方法 | 说明 | 示例 |
|------|------|------|
| `get_data("index_components")` | 指数成分股 | 沪深300成分股列表 |
| `get_data("index_list")` | 指数列表 | 所有可用指数 |
| `get_data("sentiment")` | 市场情绪 | 情绪指标数据 |
| `get_data("us_index")` | 美股指数 | 道琼斯、纳斯达克 |

## 🤝 贡献

我们欢迎各种形式的贡献！

🐛 **发现了问题?** [提交 Issue](https://github.com/sjzsdu/china_stock_data/issues)  
💡 **有好想法?** [发起讨论](https://github.com/sjzsdu/china_stock_data/discussions)  
🔧 **想要改进?** [提交 Pull Request](https://github.com/sjzsdu/china_stock_data/pulls)  

### 贡献步骤

1. 🍴 Fork 本仓库
2. 🌟 创建特性分支: `git checkout -b feature/amazing-feature`
3. 💻 编写代码并添加测试
4. ✅ 确保测试通过: `poetry run pytest`
5. 📝 提交更改: `git commit -m 'Add amazing feature'`
6. 🚀 推送分支: `git push origin feature/amazing-feature`
7. 🔄 创建 Pull Request

## 📞 支持

- 📧 邮箱: 122828837@qq.com
- 🐛 问题反馈: [GitHub Issues](https://github.com/sjzsdu/china_stock_data/issues)
- 💬 讨论交流: [GitHub Discussions](https://github.com/sjzsdu/china_stock_data/discussions)

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 🙏 致谢

- 感谢 [AkShare](https://github.com/jindaxiang/akshare) 提供的数据接口
- 感谢所有贡献者的支持与帮助

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个星标！**

[⭐ Star](https://github.com/sjzsdu/china_stock_data/stargazers) • [👀 Watch](https://github.com/sjzsdu/china_stock_data/watchers) • [🍴 Fork](https://github.com/sjzsdu/china_stock_data/network/members)

</div>
