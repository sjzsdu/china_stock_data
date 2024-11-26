# A股市场数据服务项目

本项目主要是服务于A股市场，基于 [akshare](https://github.com/jindaxiang/akshare) 的封装，增加了一些功能以提高数据获取的效率和可靠性。

## 项目功能

- **缓存机制**：通过增加缓存功能以控制 akshare 的访问频率，防止频繁请求导致 IP 被封禁。
- **数据对象**：
  - `StockData`: 代表个股数据。通过封装 akshare 的个股接口，提供多个 fetcher 来获取特定股票的数据。
  - `StockMarket`: 代表整个股票市场。用于获取与个股无关的市场数据。

## 主要模块

### 1. StockData

`StockData` 模块用于处理单个股票的数据请求。它封装了 akshare 提供的个股数据接口，确保数据获取简单、高效。该模块提供的功能包括但不限于：

- 股票历史数据获取
- 实时行情数据获取
等等，还在更新....

### 2. StockMarket

`StockMarket` 模块处理整个市场的数据查询。通过这一模块，用户可以获取诸如指数数据、板块数据以及市场动态等信息。该模块帮助用户了解市场的整体情况，并可能为投资决策提供支持。

## 使用说明
### 安装
```python
from china_stock_data import StockData, StockMarket

# 个股数据示例
stock_data = StockData('601688')
historical_data = stock_data.kline

# 市场数据示例
market = StockMarket('000001')
index_data = market.index_components
```

## 贡献
欢迎对本项目的改进提出建议或提交PR！请先 Fork 该项目，然后在本地进行修改，最后提交相关 PR。

## 许可证
本项目采用 MIT 许可证开源。有关更多详细信息，请参阅 LICENSE 文件。

有问题请联系: 122828837@qq.com