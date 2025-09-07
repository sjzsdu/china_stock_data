# 数据获取器 API

数据获取器是系统的核心组件，负责从不同数据源获取和处理数据。

## 基础获取器

::: china_stock_data.fetchers.base_fetcher.BaseFetcher
    options:
      show_root_heading: true
      show_source: true

## 股票数据获取器

### 历史数据获取器

::: china_stock_data.fetchers.stock.hist_fetcher.StockHistFetcher
    options:
      show_root_heading: true
      show_source: true

### 实时数据获取器

::: china_stock_data.fetchers.stock.realtime_fetcher.StockRealtimeFetcher
    options:
      show_root_heading: true
      show_source: true

### 基本信息获取器

::: china_stock_data.fetchers.stock.info_fetcher.StockInfoFetcher
    options:
      show_root_heading: true
      show_source: true

### 筹码分布获取器

::: china_stock_data.fetchers.stock.chip_fetcher.StockChipFetcher
    options:
      show_root_heading: true
      show_source: true

## 指数数据获取器

### 指数成分股获取器

::: china_stock_data.fetchers.index.components_fetcher.IndexComponentsFetcher
    options:
      show_root_heading: true
      show_source: true

### 指数列表获取器

::: china_stock_data.fetchers.index.list_fetcher.IndexListFetcher
    options:
      show_root_heading: true
      show_source: true

### 美股指数获取器

::: china_stock_data.fetchers.index.us_index_fetcher.USIndexFetcher
    options:
      show_root_heading: true
      show_source: true

## 市场数据获取器

### 市场情绪获取器

::: china_stock_data.fetchers.market.sentiment_fetcher.MarketSentimentFetcher
    options:
      show_root_heading: true
      show_source: true
