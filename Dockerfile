# Multi-stage Dockerfile for MathLib testing

# Base stage with Python and dependencies
FROM python:3.11-slim as base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY requirements.txt requirements-dev.txt pyproject.toml ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy application code
COPY mathlib/ ./mathlib/
COPY tests/ ./tests/
COPY examples/ ./examples/
COPY scripts/ ./scripts/

# Install the package in editable mode
RUN pip install -e .

# Test stage - runs all tests
FROM base as test
CMD ["pytest", "-v", "--cov=mathlib", "--cov-report=term-missing", "--cov-report=html", "--cov-report=xml"]

# Coverage stage - generates and displays coverage
FROM base as coverage
CMD ["pytest", "--cov=mathlib", "--cov-report=html", "--cov-report=term", "--cov-fail-under=80"]

# Demo stage - runs the demo application
FROM base as demo
CMD ["python", "examples/demo.py"]

# Unit tests only
FROM base as test-unit
CMD ["pytest", "-m", "unit", "-v", "--cov=mathlib", "--cov-report=term"]

# Integration tests only
FROM base as test-integration
CMD ["pytest", "-m", "integration", "-v", "--cov=mathlib", "--cov-report=term"]

# Interactive shell for development
FROM base as dev
CMD ["/bin/bash"]
