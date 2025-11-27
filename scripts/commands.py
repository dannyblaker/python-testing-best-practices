"""
Makefile-style commands for common development tasks.

Usage: python scripts/commands.py <command>
"""

import subprocess
import sys


def run_command(cmd):
    """Run a shell command."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode


def test():
    """Run all tests."""
    return run_command("pytest -v")


def test_unit():
    """Run unit tests only."""
    return run_command("pytest -m unit -v")


def test_integration():
    """Run integration tests only."""
    return run_command("pytest -m integration -v")


def coverage():
    """Run tests with coverage report."""
    return run_command("pytest --cov=mathlib --cov-report=html --cov-report=term-missing")


def test_parallel():
    """Run tests in parallel."""
    return run_command("pytest -n auto -v")


def lint():
    """Run linting checks."""
    return run_command("ruff check .")


def format_code():
    """Format code with ruff."""
    return run_command("ruff format .")


def clean():
    """Clean up generated files."""
    return run_command(
        "rm -rf __pycache__ .pytest_cache htmlcov .coverage *.egg-info build dist"
    )


def install():
    """Install the package in development mode."""
    return run_command("pip install -e . && pip install -r requirements-dev.txt")


def help_menu():
    """Show available commands."""
    print("Available commands:")
    print("  test              - Run all tests")
    print("  test-unit         - Run unit tests only")
    print("  test-integration  - Run integration tests only")
    print("  coverage          - Run tests with coverage report")
    print("  test-parallel     - Run tests in parallel")
    print("  lint              - Run linting checks")
    print("  format            - Format code")
    print("  clean             - Clean up generated files")
    print("  install           - Install package in development mode")
    return 0


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        return help_menu()

    command = sys.argv[1].replace("-", "_")
    commands = {
        "test": test,
        "test_unit": test_unit,
        "test_integration": test_integration,
        "coverage": coverage,
        "test_parallel": test_parallel,
        "lint": lint,
        "format": format_code,
        "clean": clean,
        "install": install,
        "help": help_menu,
    }

    if command not in commands:
        print(f"Unknown command: {sys.argv[1]}")
        return help_menu()

    return commands[command]()


if __name__ == "__main__":
    sys.exit(main())
