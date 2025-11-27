# MathLib - Testing Best Practices Demo

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://github.com/yourusername/test_suite)
[![Python Versions](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10%20|%203.11%20|%203.12-blue)](https://www.python.org/)

A comprehensive demonstration of Python testing best practices using **pytest**, featuring a mathematics library with unit tests, integration tests, and CI/CD automation.

[![A Danny Blaker project badge](https://github.com/dannyblaker/dannyblaker.github.io/blob/main/danny_blaker_project_badge.svg)](https://github.com/dannyblaker/)

## 🎯 Project Overview

This repository showcases professional testing practices for Python projects, including:

- ✅ **Unit Tests**: Isolated tests for individual functions with edge cases
- ✅ **Integration Tests**: Tests for interactions between modules
- ✅ **Parameterized Tests**: Testing multiple scenarios efficiently
- ✅ **Fixtures**: Reusable test components
- ✅ **Test Markers**: Organizing and filtering tests
- ✅ **Code Coverage**: Measuring test effectiveness
- ✅ **CI/CD Pipeline**: Automated testing with GitHub Actions
- ✅ **Cross-Platform Testing**: Linux, Windows, and macOS
- ✅ **Multiple Python Versions**: 3.8 through 3.12

## 📚 Project Structure

```
test_suite/
├── mathlib/                 # Main application package
│   ├── __init__.py
│   ├── calculator.py       # Calculator operations
│   ├── statistics.py       # Statistical functions
│   └── geometry.py         # Geometric calculations
├── tests/                   # Test suite
│   ├── __init__.py
│   ├── test_calculator.py  # Unit tests for calculator
│   ├── test_statistics.py  # Unit tests for statistics
│   ├── test_geometry.py    # Unit tests for geometry
│   └── test_integration.py # Integration tests
├── .github/
│   └── workflows/
│       ├── tests.yml       # Main CI/CD workflow
│       └── coverage.yml    # Coverage reporting workflow
├── pyproject.toml          # Project configuration
├── requirements.txt        # Production dependencies
├── requirements-dev.txt    # Development dependencies
└── README.md              # This file
```

## 🚀 Getting Started

### Quick Start with Docker (Recommended)

The fastest way to run the project is using Docker Compose:

```bash
# Run all tests with coverage
docker compose up

# Or run the demo application
docker compose up demo

# Or run specific test suites
docker compose up test-unit
docker compose up test-integration
```

That's it! No Python installation or virtual environment needed.

### Alternative: Manual Installation

#### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

#### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/test_suite.git
   cd test_suite
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the package in development mode**:
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

## 🧪 Running Tests

### With Docker (Recommended)

```bash
# Run all tests
docker compose up test

# Run demo application
docker compose up demo

# Run unit tests only
docker compose up test-unit

# Run integration tests only
docker compose up test-integration

# Generate coverage report
docker compose up coverage

# Interactive development shell
docker compose run --rm dev

# Or use the Makefile for convenience
make test          # Run all tests
make demo          # Run demo
make test-unit     # Unit tests only
make coverage      # Coverage report
make shell         # Interactive shell
```

### Without Docker (Manual)

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run unit tests only
pytest -m unit

# Run integration tests only
pytest -m integration

# Run tests with coverage report
pytest --cov=mathlib --cov-report=html --cov-report=term-missing

# Run tests in parallel
pytest -n auto

# Run specific test file
pytest tests/test_calculator.py -v

# Run specific test function
pytest tests/test_calculator.py::TestCalculator::test_add -v
```

## 📊 Testing Best Practices Demonstrated

### 1. **Test Organization**

Tests are organized into logical groups:
- **Unit tests**: Test individual functions in isolation
- **Integration tests**: Test interactions between modules
- **Test classes**: Group related tests together
- **Test markers**: Categorize tests for selective execution

### 2. **Fixtures**

Fixtures provide reusable test setup:

```python
@pytest.fixture
def calc(self):
    """Fixture to provide a Calculator instance."""
    return Calculator()
```

### 3. **Parametrized Tests**

Test multiple scenarios efficiently:

```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(self, calc, a, b, expected):
    assert calc.add(a, b) == expected
```

### 4. **Exception Testing**

Verify error handling:

```python
def test_divide_by_zero(self, calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)
```

### 5. **Floating Point Comparisons**

Use `pytest.approx` for floating point comparisons:

```python
assert result == pytest.approx(expected)
```

### 6. **Test Markers**

Organize tests with custom markers:

```python
@pytest.mark.unit
@pytest.mark.slow
def test_something():
    pass
```

### 7. **Code Coverage**

Measure test coverage and enforce minimum thresholds:
- Coverage reports in multiple formats (HTML, XML, terminal)
- Integration with CI/CD for automated coverage checks
- Target: >80% coverage

### 8. **Continuous Integration**

GitHub Actions workflows that:
- Run tests on multiple OS (Linux, Windows, macOS)
- Test against multiple Python versions (3.8-3.12)
- Generate and upload coverage reports
- Run code quality checks
- Test parallel execution

## 🔍 Code Coverage

Generate a coverage report:

```bash
pytest --cov=mathlib --cov-report=html
```

View the HTML report:
```bash
open htmlcov/index.html  # On macOS
xdg-open htmlcov/index.html  # On Linux
start htmlcov/index.html  # On Windows
```

## 📈 CI/CD Pipeline

The project includes two GitHub Actions workflows:

### 1. **Main Test Workflow** (`.github/workflows/tests.yml`)
- Runs on push and pull requests
- Tests across multiple OS and Python versions
- Includes parallel test execution
- Performs code quality checks

### 2. **Coverage Workflow** (`.github/workflows/coverage.yml`)
- Generates detailed coverage reports
- Creates coverage badges
- Fails if coverage drops below 80%
- Comments coverage on pull requests

## 🛠️ Development Workflow

### With Docker
1. **Write tests first** (TDD approach)
2. **Implement functionality** to pass tests
3. **Run tests locally**: `docker compose up test`
4. **Check coverage**: `docker compose up coverage`
5. **Test in dev shell**: `make shell` or `docker compose run --rm dev`
6. **Commit changes** and push
7. **CI pipeline** runs automatically

### Without Docker
1. **Write tests first** (TDD approach)
2. **Implement functionality** to pass tests
3. **Run tests locally**: `pytest -v`
4. **Check coverage**: `pytest --cov=mathlib`
5. **Commit changes** and push
6. **CI pipeline** runs automatically
7. **Review coverage reports** and results

## 📝 Test Writing Guidelines

### Unit Tests
- Test one thing at a time
- Use descriptive test names
- Include edge cases and boundary conditions
- Test error conditions
- Use parametrized tests for multiple inputs
- Aim for high code coverage

### Integration Tests
- Test interactions between modules
- Verify data flow across components
- Test realistic usage scenarios
- Check error propagation
- Test complex workflows

### General Principles
- **Arrange-Act-Assert** pattern
- Tests should be **independent**
- Tests should be **repeatable**
- Tests should be **fast**
- Use **meaningful assertions**
- Keep tests **simple and readable**

## 🎓 Learning Resources

This project demonstrates:

1. **Test-Driven Development (TDD)**
2. **pytest framework features**
3. **Test organization and structure**
4. **CI/CD best practices**
5. **Code coverage analysis**
6. **Cross-platform testing**
7. **Multi-version Python support**

## 📦 Dependencies

### Docker (Recommended)
- Docker Engine 20.10+
- Docker Compose 2.0+

### Production
None (pure Python implementation)

### Development (if not using Docker)
- `pytest>=7.4.0` - Testing framework
- `pytest-cov>=4.1.0` - Coverage plugin
- `pytest-xdist>=3.3.0` - Parallel execution
- `pytest-mock>=3.11.0` - Mocking utilities

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Test with Docker: `docker compose up test`
5. Ensure all tests pass
6. Maintain >80% coverage
7. Submit a pull request

## 📄 License

This project is for educational purposes. Feel free to use it as a template for your own projects.

## 🔗 Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [Python Testing Best Practices](https://docs.python-guide.org/writing/tests/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 💡 Tips for Using This Template

1. **Use Docker for consistency** - `docker compose up` runs everywhere
2. **Start with unit tests** - Test individual functions first
3. **Add integration tests** - Test module interactions
4. **Monitor coverage** - Aim for >80% coverage
5. **Use test markers** - Organize tests by type and speed
6. **Run tests frequently** - Catch issues early
7. **Keep tests maintainable** - Use fixtures and parametrization
8. **Document test intent** - Use descriptive names and docstrings
9. **Automate with CI/CD** - Let GitHub Actions handle testing

## 🐳 Docker Commands Reference

```bash
# Quick commands
docker compose up              # Run all tests (default)
docker compose up demo         # Run demo application
make test                      # Run tests (using Makefile)
make demo                      # Run demo (using Makefile)
make shell                     # Interactive development shell

# All available commands
make help                      # Show all available commands
make build                     # Build Docker images
make test-unit                 # Run unit tests only
make test-integration          # Run integration tests only
make coverage                  # Generate coverage report
make logs                      # View container logs
make clean                     # Clean up containers and artifacts
```

---

**Happy Testing!**
