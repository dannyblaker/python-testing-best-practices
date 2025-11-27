# Quick Start Guide

This guide will help you get started with the MathLib testing repository.

## Quick Start with Docker (Recommended) 🐳

The easiest way to get started is with Docker:

1. **Navigate to the repository**:
   ```bash
   cd /home/d/Documents/test_suite
   ```

2. **Run tests**:
   ```bash
   docker compose up
   ```

That's it! Docker will automatically:
- Build the container with Python and all dependencies
- Run the complete test suite
- Generate coverage reports
- Display results

### Other Docker Commands

```bash
# Run the demo application
docker compose up demo

# Run only unit tests
docker compose up test-unit

# Run only integration tests
docker compose up test-integration

# Generate coverage report
docker compose up coverage

# Interactive development shell
docker compose run --rm dev

# Using Makefile shortcuts
make test          # Run all tests
make demo          # Run demo
make shell         # Interactive shell
make help          # Show all commands
```

## Alternative: Manual Installation

If you prefer not to use Docker:

1. **Clone the repository** (or navigate to it):
   ```bash
   cd /home/d/Documents/test_suite
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -e .
   pip install -r requirements-dev.txt
   ```

## Running Tests

### With Docker

```bash
# Run all tests
docker compose up test

# Run with verbose output (already included)
docker compose up test

# Run different test suites
docker compose up test-unit         # Unit tests only
docker compose up test-integration  # Integration tests only

# Use Makefile for convenience
make test                           # All tests
make test-unit                      # Unit tests
make test-integration               # Integration tests
```

### Without Docker (Manual)

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with detailed output
pytest -vv
```

### Running Specific Test Categories

```bash
# Run only unit tests
pytest -m unit -v

# Run only integration tests
pytest -m integration -v

# Run only slow tests
pytest -m slow -v

# Exclude slow tests
pytest -m "not slow" -v
```

### Test Coverage

```bash
# Run tests with coverage report
pytest --cov=mathlib --cov-report=term-missing

# Generate HTML coverage report
pytest --cov=mathlib --cov-report=html
open htmlcov/index.html  # View in browser

# Check minimum coverage threshold
pytest --cov=mathlib --cov-fail-under=80
```

### Parallel Test Execution

```bash
# Run tests in parallel (auto-detect CPU cores)
pytest -n auto

# Run tests on 4 cores
pytest -n 4
```

### Running Specific Tests

```bash
# Run a specific test file
pytest tests/test_calculator.py -v

# Run a specific test class
pytest tests/test_calculator.py::TestCalculator -v

# Run a specific test function
pytest tests/test_calculator.py::TestCalculator::test_add -v

# Run tests matching a pattern
pytest -k "circle" -v
pytest -k "test_add or test_subtract" -v
```

## Test Output Examples

### Example 1: Running Unit Tests

```bash
pytest -m unit -v
```

Expected output:
- All unit tests run
- Detailed pass/fail for each test
- Coverage report

### Example 2: Running Integration Tests

```bash
pytest -m integration -v
```

Expected output:
- Integration tests showing module interactions
- Tests demonstrating complex workflows

### Example 3: Coverage Report

```bash
pytest --cov=mathlib --cov-report=term-missing
```

Expected output:
```
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
mathlib/__init__.py         1      0   100%
mathlib/calculator.py      39      0   100%
mathlib/geometry.py        51      0   100%
mathlib/statistics.py      60      0   100%
-----------------------------------------------------
TOTAL                     151      0   100%
```

## Demo Application

Run the demo to see the library in action:

```bash
python examples/demo.py
```

## Helper Scripts

Use the command script for common tasks:

```bash
# Run all tests
python scripts/commands.py test

# Run unit tests
python scripts/commands.py test-unit

# Run integration tests
python scripts/commands.py test-integration

# Generate coverage report
python scripts/commands.py coverage

# Run tests in parallel
python scripts/commands.py test-parallel

# Clean generated files
python scripts/commands.py clean
```

## Understanding Test Output

### Passed Test
```
tests/test_calculator.py::TestCalculator::test_add[2-3-5] PASSED [0%]
```
- ✅ Test passed successfully

### Failed Test
```
tests/test_calculator.py::TestCalculator::test_add[2-3-6] FAILED [0%]
```
- ❌ Test failed
- Shows expected vs actual values
- Includes traceback

### Skipped Test
```
tests/test_calculator.py::TestCalculator::test_future SKIPPED [0%]
```
- ⏭️ Test was skipped (e.g., not applicable)

## CI/CD Pipeline

The GitHub Actions workflows automatically run:

1. **On push/pull request**:
   - Tests on multiple OS (Ubuntu, Windows, macOS)
   - Tests on Python 3.8-3.12
   - Code coverage analysis
   - Code quality checks

2. **Workflow files**:
   - `.github/workflows/tests.yml` - Main test workflow
   - `.github/workflows/coverage.yml` - Coverage reporting

## Common Issues

### Issue: Import errors
**Solution**: Make sure you installed the package with `pip install -e .`

### Issue: pytest not found
**Solution**: Activate virtual environment and install dev dependencies

### Issue: Coverage not showing
**Solution**: Run with `--cov=mathlib` flag

## Next Steps

1. **Explore the code**: Review the implementation in `mathlib/`
2. **Study the tests**: Examine test patterns in `tests/`
3. **Try modifying tests**: Make a test fail to see the output
4. **Add new features**: Practice TDD by writing tests first
5. **Check coverage**: Identify untested code paths

## Resources

- **pytest docs**: https://docs.pytest.org/
- **Coverage docs**: https://coverage.readthedocs.io/
- **Testing best practices**: See README.md

## Testing Checklist

- [ ] All tests pass locally
- [ ] Coverage above 80%
- [ ] New features have tests
- [ ] Edge cases covered
- [ ] Error conditions tested
- [ ] Documentation updated
- [ ] CI pipeline passes

---

**Happy Testing! 🧪**
