# aicommits

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Type Checked](https://img.shields.io/badge/type%20checked-mypy-blue)](http://mypy-lang.org/)

A modern Python CLI tool that generates meaningful git commit messages using AI.

## 🚀 Features

- **AI-Powered**: Generate commit messages using OpenAI's GPT models
- **Multi-Provider Support**: Support for OpenAI, Anthropic, and local models
- **Git Integration**: Seamless integration with git workflows and hooks
- **Conventional Commits**: Support for conventional commit message format
- **Secure Configuration**: Encrypted storage of API keys and settings
- **Modern Python**: Built with Python 3.8+ using modern best practices

## 📦 Installation

```bash
pip install aicommits
```

## 🛠️ Development Setup

1. Clone the repository:
```bash
git clone git@github.com:garethdaine/commit.git
cd commit
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

4. Install pre-commit hooks:
```bash
pre-commit install
```

5. Run tests:
```bash
pytest
```

## 🏗️ Project Status

This project is currently in **Phase 1** development. See [TASKS.md](TASKS.md) for detailed development roadmap.

### Current Phase: Project Foundation
- ✅ Git repository setup with Git Flow
- ✅ Modern Python packaging with pyproject.toml
- ✅ Comprehensive testing framework
- ✅ Code quality tools (Black, isort, flake8, mypy)
- 🔄 Core architecture implementation

## 🤝 Contributing

This project follows strict development practices:

- **Test-Driven Development (TDD)**: All code must have tests written first
- **Git Flow**: Feature branches for all development
- **Code Quality**: 90%+ test coverage, type hints, and linting
- **Security First**: Secure handling of API keys and credentials

See our [development workflow rules](.cursor/rules/) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [Repository](https://github.com/garethdaine/commit)
- [Issues](https://github.com/garethdaine/commit/issues)
- [Changelog](CHANGELOG.md)

---

**Note**: This is a Python reimplementation of [aicommits](https://github.com/Nutlope/aicommits) with additional features and improvements.
