# TrustByDesign Test Suite

This directory contains tests for validating TrustByDesign compliance.

## Test Files

### test_safety_protocols.py

Comprehensive test suite for safety protocol compliance. Includes tests for:

- **Level 1 (Observational)**:
  - Capability boundary enforcement
  - Prohibited action refusal

- **Level 2 (Interactive)**:
  - Memory safety (view, delete, consent)
  - Transparency (confidence levels)
  - Consent mechanisms (grant, revoke)
  - Audit logging

- **Level 3 (Autonomous)**:
  - (To be added based on specific autonomous requirements)

## Running Tests

### Prerequisites

```bash
pip install pytest pyyaml
```

### Run All Tests

```bash
# From repository root
pytest tests/ -v

# Or from tests directory
cd tests
pytest -v
```

### Run Specific Test File

```bash
pytest tests/test_safety_protocols.py -v
```

### Run Specific Test

```bash
pytest tests/test_safety_protocols.py::test_memory_requires_consent -v
```

### Run with Coverage

```bash
pip install pytest-cov
pytest tests/ --cov=your_module --cov-report=html
```

## Adapting Tests to Your System

The test suite includes a `MockLevel2Agent` class that demonstrates the required interfaces. To adapt for your system:

1. **Replace the mock agent** with your actual implementation
2. **Update fixtures** to initialize your agent
3. **Add system-specific tests** for unique features
4. **Keep all compliance tests** to ensure TrustByDesign requirements are met

### Example Adaptation

```python
# In your conftest.py or test file
import pytest
from my_system import MyAgent

@pytest.fixture
def agent():
    """Create your actual agent for testing."""
    return MyAgent(config="test_config.yaml")

# Run the existing compliance tests against your agent
# They should pass if your implementation is compliant
```

## Test Coverage Targets

- **Level 1 Systems**: All capability boundary tests must pass
- **Level 2 Systems**: All Level 1 + memory, consent, transparency, and audit tests must pass
- **Level 3 Systems**: All Level 2 + governance and autonomous action tests must pass

## CI/CD Integration

### GitHub Actions Example

```yaml
name: TrustByDesign Compliance Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          pip install pytest pyyaml
          pip install -e .
      - name: Run compliance tests
        run: pytest tests/ -v
```

## Adding New Tests

When adding new safety requirements:

1. Add test to appropriate level section
2. Document what's being tested
3. Ensure test is deterministic
4. Add to compliance summary test

## Test Naming Convention

- `test_[feature]_[expected_behavior]`
- Examples:
  - `test_memory_requires_consent`
  - `test_prohibited_action_refused`
  - `test_audit_log_exists`

## Troubleshooting

### Tests Fail with Import Errors

Make sure your system module is in the Python path:
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/your/system"
```

### Mock Agent vs Real Agent

The mock agent demonstrates the *interface* your agent should implement. Your real agent may have additional features, but must support at minimum the operations shown in the mock.

## Additional Resources

- See `docs/safety-protocols.md` for detailed requirement specifications
- See `docs/integration-guide.md` for implementation guidance
- See `examples/` for configuration templates
