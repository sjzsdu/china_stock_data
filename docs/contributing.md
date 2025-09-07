# 贡献指南

感谢你对 China Stock Data 项目的关注！我们欢迎各种形式的贡献。

## 🎯 贡献方式

### 🐛 报告问题
- [提交 Bug 报告](https://github.com/sjzsdu/china_stock_data/issues/new?template=bug_report.md)
- [请求新功能](https://github.com/sjzsdu/china_stock_data/issues/new?template=feature_request.md)
- [文档改进建议](https://github.com/sjzsdu/china_stock_data/issues/new)

### 💻 代码贡献
- 修复 Bug
- 新增功能
- 性能优化
- 代码重构

### 📖 文档贡献
- 改进文档内容
- 添加使用示例
- 翻译文档
- 修正错别字

## 🛠️ 开发环境设置

### 1. 克隆仓库

```bash
git clone https://github.com/sjzsdu/china_stock_data.git
cd china_stock_data
```

### 2. 安装依赖

推荐使用 Poetry 管理依赖：

```bash
# 安装 Poetry (如果尚未安装)
curl -sSL https://install.python-poetry.org | python -

# 安装项目依赖
poetry install

# 安装文档依赖
poetry install --with docs

# 激活虚拟环境
poetry shell
```

### 3. 验证安装

```bash
# 运行测试
poetry run pytest

# 检查代码导入
poetry run python -c "from china_stock_data import StockData; print('✅ 安装成功')"
```

## 🧪 开发工作流

### 1. 创建功能分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/bug-description
```

### 2. 编写代码

- 遵循现有代码风格
- 添加适当的类型注解
- 编写清晰的 docstring
- 保持函数简洁，单一职责

### 3. 编写测试

```bash
# 为新功能编写测试
# 测试文件位于 tests/ 目录

# 运行测试确保通过
poetry run pytest tests/

# 检查测试覆盖率
poetry run pytest --cov=china_stock_data tests/
```

### 4. 更新文档

如果你的更改影响了 API：

```bash
# 构建文档预览
poetry run mkdocs serve

# 在浏览器中查看: http://127.0.0.1:8000
```

### 5. 提交更改

```bash
git add .
git commit -m "feat: 简洁描述你的更改"

# 推送到远程分支
git push origin feature/your-feature-name
```

### 6. 创建 Pull Request

- 访问 GitHub 仓库页面
- 点击 "New Pull Request"
- 选择你的功能分支
- 填写 PR 描述模板

## 📝 代码规范

### Python 代码风格

```python
from typing import Optional, Dict, Any
import pandas as pd

class ExampleClass:
    """
    Example class demonstrating coding standards.
    
    This class serves as a template for consistent code style
    across the project.
    """
    
    def __init__(self, symbol: str, days: Optional[int] = None) -> None:
        """
        Initialize the example class.
        
        Args:
            symbol: Stock symbol code
            days: Number of days, defaults to None
            
        Raises:
            ValueError: If symbol is empty
        """
        if not symbol:
            raise ValueError("Symbol cannot be empty")
            
        self.symbol: str = symbol
        self.days: Optional[int] = days
    
    def get_data(self, data_type: str) -> pd.DataFrame:
        """
        Get data of specified type.
        
        Args:
            data_type: Type of data to retrieve
            
        Returns:
            DataFrame containing the requested data
            
        Raises:
            NotImplementedError: If data_type is not supported
        """
        raise NotImplementedError(f"Data type '{data_type}' not supported")
```

### 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
feat: 添加新功能
fix: 修复问题
docs: 文档更新
style: 代码格式调整
refactor: 代码重构
test: 测试相关
chore: 构建工具或辅助工具的变动
```

示例：
```
feat: 新增美股指数数据获取功能
fix: 修复交易时间判断的边界条件问题
docs: 更新 API 文档中的示例代码
test: 增加市场情绪数据的单元测试
```

## 🧪 测试指南

### 编写测试

```python
import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from china_stock_data import StockData

class TestStockData:
    """Test StockData functionality."""
    
    def setup_method(self):
        """Setup test data before each test method."""
        self.symbol = "000001"
        self.stock = StockData(self.symbol, days=30)
    
    def test_init(self):
        """Test StockData initialization."""
        assert self.stock.symbol == self.symbol
        assert self.stock.days == 30
    
    @patch('china_stock_data.fetchers.stock.hist_fetcher.ak.stock_zh_a_hist')
    def test_get_kline_data(self, mock_ak):
        """Test K-line data retrieval."""
        # Mock返回数据
        mock_data = pd.DataFrame({
            '日期': pd.date_range('2023-01-01', periods=5),
            '开盘': [100, 101, 102, 103, 104],
            '收盘': [101, 102, 103, 104, 105],
            '最高': [102, 103, 104, 105, 106],
            '最低': [99, 100, 101, 102, 103],
            '成交量': [1000000] * 5
        })
        mock_ak.return_value = mock_data
        
        # 执行测试
        result = self.stock.get_data("kline")
        
        # 验证结果
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 5
        assert '收盘' in result.columns
        mock_ak.assert_called_once()
```

### 运行测试

```bash
# 运行所有测试
poetry run pytest

# 运行特定测试文件
poetry run pytest tests/test_stock_data.py

# 运行特定测试方法
poetry run pytest tests/test_stock_data.py::TestStockData::test_get_kline_data

# 显示详细输出
poetry run pytest -v

# 生成覆盖率报告
poetry run pytest --cov=china_stock_data --cov-report=html tests/
```

## 📖 文档贡献

### 文档结构

```
docs/
├── index.md              # 首页
├── getting-started.md    # 快速开始
├── api/                  # API 文档 (自动生成)
├── examples/            # 示例教程
└── contributing.md      # 贡献指南
```

### 本地预览文档

```bash
# 启动文档服务器
poetry run mkdocs serve

# 访问 http://127.0.0.1:8000 预览
```

### 文档写作规范

- 使用清晰的标题层次
- 提供可运行的代码示例
- 包含必要的警告和提示
- 保持内容更新与代码同步

## 🔍 代码审查

### PR 审查清单

**功能性**
- [ ] 功能按预期工作
- [ ] 处理了边界条件
- [ ] 错误处理恰当
- [ ] 性能考虑合理

**代码质量**
- [ ] 代码风格一致
- [ ] 变量命名清晰
- [ ] 函数职责单一
- [ ] 注释和文档充分

**测试**
- [ ] 包含相应测试
- [ ] 测试覆盖核心功能
- [ ] 测试用例设计合理
- [ ] 所有测试通过

**文档**
- [ ] API 文档更新
- [ ] 使用示例清晰
- [ ] 变更日志记录

## 🚀 发布流程

### 版本管理

项目使用[语义化版本](https://semver.org/lang/zh-CN/)：

- `MAJOR.MINOR.PATCH`
- 主版本号：不兼容的 API 修改
- 次版本号：向下兼容的功能性新增
- 修订号：向下兼容的问题修正

### 发布清单

1. **更新版本号**
   ```bash
   # pyproject.toml 中更新版本
   version = "0.3.0"
   ```

2. **更新变更日志**
   ```markdown
   ## [0.3.0] - 2024-01-15
   
   ### Added
   - 新增美股指数数据获取功能
   
   ### Fixed
   - 修复缓存失效问题
   
   ### Changed
   - 优化数据获取性能
   ```

3. **运行完整测试**
   ```bash
   poetry run pytest
   ```

4. **创建发布标签**
   ```bash
   git tag -a v0.3.0 -m "Release version 0.3.0"
   git push origin v0.3.0
   ```

## 💬 社区

### 获取帮助

- 📚 [查看文档](https://sjzsdu.github.io/china_stock_data/)
- 🐛 [报告问题](https://github.com/sjzsdu/china_stock_data/issues)
- 💬 [参与讨论](https://github.com/sjzsdu/china_stock_data/discussions)
- 📧 发送邮件：122828837@qq.com

### 行为准则

我们致力于营造一个开放、友好的社区环境：

- 🤝 尊重不同观点和经验
- 💬 使用友好和包容的语言
- 🎯 专注于对社区最有利的事情
- 🙏 对其他社区成员表示同理心

## 🙏 致谢

感谢所有贡献者的支持！你的每一份贡献都让这个项目变得更好。

[![Contributors](https://contrib.rocks/image?repo=sjzsdu/china_stock_data)](https://github.com/sjzsdu/china_stock_data/graphs/contributors)
