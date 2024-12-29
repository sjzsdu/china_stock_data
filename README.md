# A股市场数据服务项目

本项目主要是服务于A股市场，基于 [akshare](https://github.com/jindaxiang/akshare) 的封装，增加了缓存机制和数据持久化功能，提高数据获取的效率和可靠性。

## 主要特性

- **智能缓存**：
  - 自动判断交易时间，非交易时间优先使用缓存数据
  - 交易时间内控制请求频率，防止频繁访问
  - 支持数据时效性检查，确保数据及时更新

- **数据持久化**：
  - 自动创建数据存储目录
  - JSON格式存储配置和缓存信息
  - CSV格式存储行情数据

- **交易时间管理**：
  - 自动识别交易日
  - 智能判断当前是否为交易时间
  - 支持最近交易日比对

## 核心模块

### 1. StockData

用于获取个股相关数据：

```python
from china_stock_data import StockData

# 创建股票数据对象
stock = StockData('601688')

# 获取K线数据
kline_data = stock.kline

# 获取实时行情
realtime_data = stock.realtime

# 获取筹码分布
chip_data = stock.chip
```

### 2. StockMarket

用于获取市场整体数据：

```python
from china_stock_data import StockMarket

# 创建市场数据对象
market = StockMarket()

# 获取指数成分股
components = market.index_components('000001')  # 上证指数

# 获取指数列表
index_list = market.index_list

# 获取市场动态
market_motion = market.market_motion
```

## 安装方法

使用 pip 安装：

```bash
pip install china-stock-data
```

或者使用 poetry：

```bash
poetry add china-stock-data
```

## 项目结构

```
china_stock_data/
├── fetchers/           # 数据获取器
│   ├── base_fetcher.py
│   ├── stock_hist_fetcher.py
│   ├── stock_realtime_fetcher.py
│   └── ...
├── persistent_dict.py  # 数据持久化
├── trading_time_checker.py  # 交易时间管理
├── stock_data.py      # 个股数据类
└── stock_market.py    # 市场数据类
```

## 开发说明

### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_base_fetcher.py
```

### 代码风格

项目使用 Python 3.8+ 的类型注解，并遵循 PEP 8 规范。

## 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 版本历史

- 0.1.7: 当前版本
  - 增加数据持久化功能
  - 优化交易时间判断
  - 完善测试用例

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 联系方式

- 邮箱：122828837@qq.com
- Issues：[GitHub Issues](https://github.com/your-username/china-stock-data/issues)

## 致谢

感谢 [akshare](https://github.com/jindaxiang/akshare) 项目提供的数据接口支持。