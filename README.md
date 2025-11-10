# PyNapCat

一个现代化的 Python 包，用于 NapCat。

## 特性

- 🚀 现代化的包结构（使用 `pyproject.toml`）
- 📦 采用 `src/` 布局
- 🧪 集成测试框架（pytest）
- 🎨 代码格式化和检查（black、ruff）
- 📝 类型检查（mypy）
- 📊 代码覆盖率报告

## 安装

使用 pip 安装：

```bash
pip install pynapcat
```

从源码安装：

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

## 更新日志

### 0.1.0 (2024-11-11)

- 初始版本发布
