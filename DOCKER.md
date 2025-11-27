# Docker Guide for MathLib

This guide explains how to use Docker to run, test, and develop the MathLib project.

## Why Docker?

Using Docker provides several benefits:

- ✅ **No Python installation required** - Docker containers include everything
- ✅ **Consistent environment** - Works the same on any machine
- ✅ **Isolated dependencies** - No conflicts with your system Python
- ✅ **Quick setup** - Single command to run tests
- ✅ **Clean workspace** - Easy to remove and start fresh

## Prerequisites

- [Docker Engine](https://docs.docker.com/engine/install/) 20.10+
- [Docker Compose](https://docs.docker.com/compose/install/) 2.0+

Verify installation:
```bash
docker --version
docker compose version
```

## Quick Start

Run all tests with a single command:

```bash
docker compose up
```

This will:
1. Build the Docker image with Python 3.11 and all dependencies
2. Run the complete test suite (181 tests)
3. Generate coverage reports
4. Display results in your terminal

## Available Commands

### Using Docker Compose

```bash
# Run all tests with coverage (default)
docker compose up

# Run specific services
docker compose up test              # All tests
docker compose up demo              # Demo application
docker compose up test-unit         # Unit tests only
docker compose up test-integration  # Integration tests only
docker compose up coverage          # Coverage report

# Interactive development shell
docker compose run --rm dev

# View logs
docker compose logs

# Stop and remove containers
docker compose down

# Clean everything (images, volumes, containers)
docker compose down -v --rmi all
```

### Using the Makefile (Recommended)

The Makefile provides convenient shortcuts:

```bash
# Show all available commands
make help

# Common commands
make test              # Run all tests
make demo              # Run demo application
make test-unit         # Run unit tests only
make test-integration  # Run integration tests only
make coverage          # Generate coverage report
make shell             # Open development shell

# Build and cleanup
make build             # Build Docker images
make rebuild           # Rebuild from scratch
make clean             # Remove containers and artifacts

# View logs
make logs              # View container logs
```

## Detailed Usage

### Running Tests

#### All Tests
```bash
docker compose up test
# or
make test
```

Output includes:
- Test results for all 181 tests
- Code coverage percentage (100%)
- Coverage report in terminal
- HTML coverage report in `htmlcov/`
- XML coverage report in `coverage.xml`

#### Unit Tests Only
```bash
docker compose up test-unit
# or
make test-unit
```

Runs 169 unit tests focusing on individual module functionality.

#### Integration Tests Only
```bash
docker compose up test-integration
# or
make test-integration
```

Runs 12 integration tests focusing on module interactions.

### Running the Demo

```bash
docker compose up demo
# or
make demo
```

This runs the example application showcasing the mathematics library in action.

### Development Shell

For interactive development and debugging:

```bash
docker compose run --rm dev
# or
make shell
```

Inside the shell you can:
```bash
# Run tests manually
pytest -v

# Run specific tests
pytest tests/test_calculator.py -v

# Run Python interactively
python

# Use the library
python examples/demo.py

# Install additional packages
pip install <package>

# Exit the shell
exit
```

## Docker Architecture

### Multi-Stage Dockerfile

The project uses a multi-stage Dockerfile with several targets:

1. **base** - Base image with Python, dependencies, and application code
2. **test** - Runs all tests with coverage
3. **coverage** - Generates coverage reports
4. **demo** - Runs the demo application
5. **test-unit** - Runs unit tests only
6. **test-integration** - Runs integration tests only
7. **dev** - Interactive development environment

### Services

The `docker-compose.yml` defines these services:

| Service | Description | Command |
|---------|-------------|---------|
| `test` | Run all tests | `docker compose up test` |
| `demo` | Run demo app | `docker compose up demo` |
| `test-unit` | Run unit tests | `docker compose up test-unit` |
| `test-integration` | Run integration tests | `docker compose up test-integration` |
| `coverage` | Generate coverage | `docker compose up coverage` |
| `dev` | Development shell | `docker compose run --rm dev` |

## Volumes and Artifacts

### Generated Files

When you run tests, Docker generates these files on your host machine:

```
test_suite/
├── htmlcov/           # HTML coverage report
│   └── index.html    # Open in browser
└── coverage.xml       # XML coverage report (for CI/CD)
```

These are mounted as volumes so you can access them after the container stops.

### Viewing Coverage Report

After running tests:

```bash
# Generate coverage
docker compose up coverage

# View HTML report in browser
open htmlcov/index.html         # macOS
xdg-open htmlcov/index.html     # Linux
start htmlcov/index.html        # Windows
```

## Dockerfile Details

### Base Image
```dockerfile
FROM python:3.11-slim as base
```
Uses official Python 3.11 slim image for smaller size.

### Dependencies
- Git (for version control)
- pytest and plugins (from requirements-dev.txt)
- Application code (mathlib, tests, examples, scripts)

### Working Directory
All commands run in `/app` inside the container.

## Tips and Best Practices

### 1. Cache Optimization

Docker caches layers to speed up builds. The Dockerfile is organized to maximize cache hits:
- Dependencies are installed before copying code
- Code changes don't invalidate dependency layers

### 2. Volume Mounts

The dev service can mount your local directory for live development:

```yaml
dev:
  volumes:
    - .:/app  # Mount current directory
```

This allows you to edit code locally and see changes immediately.

### 3. Parallel Execution

Run multiple services simultaneously:

```bash
# Run tests and demo together
docker compose up test demo

# Run in background
docker compose up -d test
```

### 4. Resource Management

Clean up regularly to free disk space:

```bash
# Remove unused containers, networks, images
docker system prune

# Remove project containers and images
make clean
```

### 5. Debugging Failed Tests

If tests fail:

```bash
# Run with verbose output
docker compose run --rm dev pytest -vv

# Run specific failing test
docker compose run --rm dev pytest tests/test_calculator.py::test_add -v

# Interactive debugging
docker compose run --rm dev bash
```

## Troubleshooting

### Issue: Docker daemon not running
**Solution**: Start Docker Desktop or Docker daemon
```bash
# Check status
docker info
```

### Issue: Port conflicts
**Solution**: Stop containers using the same ports
```bash
docker compose down
```

### Issue: Build fails
**Solution**: Rebuild without cache
```bash
make rebuild
# or
docker compose build --no-cache
```

### Issue: Permission errors
**Solution**: Ensure Docker has permissions
```bash
# Add user to docker group (Linux)
sudo usermod -aG docker $USER
# Log out and back in
```

### Issue: Slow build
**Solution**: Docker may need more resources
- Increase Docker Desktop memory/CPU allocation
- Clean up unused images: `docker system prune -a`

### Issue: Coverage file busy error
**Solution**: Don't mount `.coverage` file as volume
```yaml
# Correct - mount directory only
volumes:
  - ./htmlcov:/app/htmlcov
```

## Comparison: Docker vs Local

| Aspect | Docker | Local Install |
|--------|--------|---------------|
| Setup time | ~1 minute | ~5 minutes |
| Prerequisites | Docker only | Python + pip |
| Consistency | ✅ Same everywhere | ❌ May vary |
| Isolation | ✅ Completely isolated | ❌ System-wide |
| Cleanup | ✅ `docker compose down` | ❌ Manual uninstall |
| Speed | Slightly slower (first run) | Slightly faster |

## Advanced Usage

### Custom Python Version

Edit `Dockerfile` to use different Python version:

```dockerfile
FROM python:3.12-slim as base  # Change version
```

Then rebuild:
```bash
make rebuild
```

### Add Dependencies

Edit `requirements-dev.txt` and rebuild:

```bash
echo "new-package>=1.0.0" >> requirements-dev.txt
make rebuild
```

### Run Custom Commands

```bash
# Run any command in the container
docker compose run --rm test pytest --help

# Run with environment variables
docker compose run --rm -e DEBUG=1 test pytest -v
```

### CI/CD Integration

Use in GitHub Actions or GitLab CI:

```yaml
# .github/workflows/docker-test.yml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run tests
        run: docker compose up test
```

## Next Steps

1. **Try it out**: Run `docker compose up` or `make test`
2. **Explore**: Run `make demo` to see the application
3. **Develop**: Use `make shell` for interactive development
4. **Learn**: Check the [README.md](README.md) for testing practices

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Python Docker Images](https://hub.docker.com/_/python)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

---

**Happy Testing with Docker! 🐳**
