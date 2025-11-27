# Conftest file for pytest configuration and shared fixtures

import pytest


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "slow: Slow running tests")


@pytest.fixture(scope="session")
def sample_data():
    """Provide sample data for tests."""
    return {
        "integers": [1, 2, 3, 4, 5],
        "floats": [1.5, 2.5, 3.5, 4.5, 5.5],
        "mixed": [1, 2.5, 3, 4.5, 5],
    }
