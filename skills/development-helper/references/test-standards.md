# Testing Standards

## Coverage Requirements

- **Minimum coverage**: 80%
- **Critical paths**: 100%
- **New code**: 90%

## Test Organization

```
tests/
├── unit/           # Unit tests for individual functions
├── integration/    # Integration tests for components
├── e2e/           # End-to-end tests
└── fixtures/      # Test data and mocks
```

## Naming Conventions

- Test files: `test_<module>.py` or `<module>.test.ts`
- Test functions: `test_<functionality>_<scenario>`
- Example: `test_user_login_with_valid_credentials`

## Best Practices

1. **Arrange-Act-Assert** pattern
2. **One assertion per test** (when possible)
3. **Descriptive test names**
4. **Isolated tests** (no dependencies between tests)
5. **Fast execution** (unit tests < 100ms)

## Running Tests

```bash
# Run all tests
npm test              # Node.js
pytest               # Python

# Run with coverage
npm run test:coverage
pytest --cov

# Run specific test file
npm test -- path/to/test.test.ts
pytest tests/unit/test_auth.py
```
