# Contributing to TrustByDesign

Thank you for your interest in improving TrustByDesign! This framework is part of the MirrorDNA-Reflection-Protocol ecosystem and serves as the trust layer for reflective AI systems.

---

## Contribution Philosophy

TrustByDesign contributions should:

✅ **Strengthen safety** without adding bureaucracy
✅ **Make governance transparent**, not burdensome
✅ **Keep trust verification simple** and robust
✅ **Maintain backward compatibility** whenever possible
✅ **Provide working code** not just documentation

❌ **Avoid** speculative architecture
❌ **Avoid** heavy symbolic references
❌ **Avoid** breaking existing templates or schemas

---

## Ways to Contribute

### 1. Report Issues
- **Bugs**: Safety violations, validation errors, broken examples
- **Gaps**: Missing templates, unclear documentation, incomplete coverage
- **Improvements**: Better validation rules, clearer error messages

**How**: Open a GitHub Issue with clear reproduction steps

### 2. Improve Documentation
- Fix typos or unclear explanations
- Add real-world examples
- Expand FAQ with common questions
- Create visual diagrams

**How**: Submit a Pull Request with documentation changes

### 3. Add Templates
- New compliance templates for specific use cases
- Industry-specific checklists (healthcare, finance, education)
- Audit trail formats for different logging systems

**Requirements**:
- Must align with TrustByDesign principles
- Must include validation example
- Must be copy-paste ready

### 4. Enhance Tools
- Improve validation logic in `scripts/`
- Add new library functions in `lib/`
- Create new CLI tools for common tasks

**Requirements**:
- Must include tests in `tests/`
- Must update `requirements.txt` if adding dependencies
- Must document usage in tool's docstring

### 5. Contribute Code Examples
- Integration patterns with other frameworks
- Real-world implementation examples
- Educational demonstrations

**Requirements**:
- Must be fully functional (not pseudocode)
- Must include inline comments explaining safety patterns
- Must demonstrate at least one TrustByDesign principle

---

## Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/MirrorDNA-Reflection-Protocol/TrustByDesign.git
cd TrustByDesign
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Tests
```bash
pytest tests/ -v
```

All tests should pass before you start making changes.

---

## Contribution Workflow

### For Small Changes (Documentation, Templates)
1. Fork the repository
2. Create a branch: `git checkout -b fix/improve-faq`
3. Make your changes
4. Test locally (run examples, validate templates)
5. Commit: `git commit -m "Improve FAQ clarity on Level 2 consent"`
6. Push: `git push origin fix/improve-faq`
7. Open a Pull Request

### For Code Changes (Tools, Library, Scripts)
1. Fork the repository
2. Create a branch: `git checkout -b feature/add-validation-tool`
3. Make your changes
4. **Write tests** in `tests/`
5. **Run test suite**: `pytest tests/ -v`
6. **Update documentation** if adding new functionality
7. Commit with clear message
8. Push and open Pull Request

### For New Features
1. **Open an issue first** to discuss the feature
2. Wait for feedback from maintainers
3. Once approved, follow the code contribution workflow above

---

## Code Standards

### Python Code
- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings to all public functions
- Keep functions focused and testable

**Example**:
```python
def validate_compliance(config: dict, level: int) -> tuple[bool, list[str]]:
    """
    Validate a system configuration against a compliance level.

    Args:
        config: System configuration dictionary
        level: Compliance level (1, 2, or 3)

    Returns:
        Tuple of (is_valid, list of error messages)
    """
    errors = []
    # Validation logic here
    return len(errors) == 0, errors
```

### Templates & Schemas
- Use consistent YAML formatting (2-space indent)
- Include inline comments explaining requirements
- Provide example values
- Reference relevant framework documents

### Documentation
- Use clear, concise language
- Avoid jargon unless defined
- Include code examples where helpful
- Link to related documents

---

## Testing Requirements

All code contributions must include tests:

### Unit Tests
```python
# tests/test_my_feature.py
import pytest
from lib.my_module import my_function

def test_my_function_valid_input():
    result = my_function("valid")
    assert result is True

def test_my_function_invalid_input():
    with pytest.raises(ValueError):
        my_function("invalid")
```

### Integration Tests
For tools and scripts, include integration tests that verify end-to-end functionality.

### Test Coverage
- Aim for >80% code coverage on new code
- Run: `pytest tests/ --cov=lib --cov=scripts`

---

## Pull Request Guidelines

### PR Title Format
```
<type>: <short description>

Examples:
fix: Correct validation error in Level 2 checklist
feat: Add industry-specific compliance templates
docs: Improve integration guide clarity
test: Add coverage for policy_checker edge cases
```

### PR Description Template
```markdown
## Summary
Brief description of what this PR does

## Motivation
Why is this change needed?

## Changes
- List of specific changes made
- Include file paths if helpful

## Testing
- How did you test this?
- What test coverage was added?

## Documentation
- What documentation was updated?
- Are examples still valid?

## Checklist
- [ ] Tests added and passing
- [ ] Documentation updated
- [ ] No breaking changes (or migration guide provided)
- [ ] Follows code standards
```

---

## Maintainer Response Time

- **Issue acknowledgment**: Within 3 days
- **PR review**: Within 1 week
- **Security issues**: Within 24 hours

Please be patient. TrustByDesign is maintained by volunteers.

---

## Code of Conduct

### Our Standards
- **Respectful**: Treat all contributors with respect
- **Constructive**: Provide helpful feedback, not just criticism
- **Collaborative**: Work together toward better safety and governance
- **Professional**: Keep discussions focused on the work

### Unacceptable Behavior
- Harassment, discrimination, or personal attacks
- Trolling or inflammatory comments
- Publishing others' private information
- Malicious code contributions

**Violations**: Report to repository maintainers. Serious violations may result in bans.

---

## Questions?

- **General questions**: Open a GitHub Discussion
- **Bugs or issues**: Open a GitHub Issue
- **Security concerns**: Use private vulnerability reporting
- **Feature proposals**: Open an issue with `[Feature Request]` prefix

---

## License

By contributing to TrustByDesign, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for helping make AI systems safer and more trustworthy!**
