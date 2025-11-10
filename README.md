# PyNapCat

一个现代化的 Python 异步框架包，专为 NapCat 设计。

## ⚡ 核心特性

- 🚀 **现代化架构**：使用 `pyproject.toml` 和 `src/` 布局
- 🔥 **Python 3.14+**：利用延迟注解求值（PEP 649/749）实现 TypeScript 级别的类型安全
- 📝 **严格类型检查**：配置 mypy 和 pyright 严格模式
- 🧪 **完整测试套件**：pytest + 代码覆盖率报告
- 🎨 **代码质量保证**：black、ruff 自动格式化和检查
- ⚡ **异步优先**：为异步编程设计的 API

## 📋 系统要求

- **Python 3.14 或更高版本** （必需）

> ⚠️ **为什么要求 Python 3.14？**
> 
> PyNapCat 利用 Python 3.14 引入的革命性类型系统改进（PEP 649/749）：
> - **延迟注解求值**：原生支持前向引用，无需手动字符串包裹
> - **`annotationlib` 标准库**：提供标准化的注解读取 API
> - **更低运行时开销**：注解按需计算，减少导入时性能损耗
> - **TypeScript 级别的类型体验**：更接近现代静态类型语言的开发体验
> 
> 详见：[Python 3.14 新特性 - 注解系统](https://docs.python.org/3.14/whatsnew/3.14.html)

## 📦 安装

### 前置条件

首先确保你已安装 Python 3.14+：

```bash
python --version  # 应显示 Python 3.14.0 或更高版本
```

如果需要安装 Python 3.14，请访问 [python.org/downloads](https://www.python.org/downloads/)

### 使用 pip 安装

```bash
pip install pynapcat
```

### 从源码安装

```bash
git clone https://github.com/yourusername/PyNapCat.git
cd PyNapCat
pip install -e .
```

## 开发环境设置

1. 克隆仓库：

```bash
git clone https://github.com/yourusername/PyNapCat.git
cd PyNapCat
```

2. 安装开发依赖：

```bash
pip install -e ".[dev]"
```

3. 运行测试：

```bash
pytest
```

4. 代码格式化：

```bash
black src tests
ruff check src tests
```

5. 类型检查：

```bash
mypy src
```

## 使用方法

```python
import pynapcat

# 你的代码
```

## 项目结构

```
PyNapCat/
├── src/
│   └── pynapcat/
│       └── __init__.py
├── tests/
│   └── __init__.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

## 贡献

欢迎贡献！请查看[贡献指南](CONTRIBUTING.md)。

## 许可证

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

## 联系方式

- 作者：Your Name
- 邮箱：your.email@example.com
- 项目主页：https://github.com/yourusername/PyNapCat

## 📝 类型安全示例

PyNapCat 充分利用 Python 3.14 的类型系统特性：

```python
from pynapcat import AsyncHandler
from annotationlib import get_annotations, Format

class MyHandler(AsyncHandler):
    async def handle(self, request: Request) -> Response:
        # 前向引用无需字符串包裹
        next_handler: MyHandler | None = None
        ...

# 运行时安全地读取注解
annotations = get_annotations(MyHandler.handle, format=Format.FORWARDREF)
```

## 📚 更新日志

### 0.1.0 (2025-11-11)

- 🎉 初始版本发布
- ✨ 基于 Python 3.14 延迟注解求值
- 🔧 配置严格类型检查（mypy + pyright）
- 📦 现代化包结构
