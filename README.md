# Unit Test Failure Validation

A GitHub Action that validates unit tests are properly written by ensuring they fail without code changes before passing with them.

> **Read more**: [New Unit Tests Need to Fail Running the Old Code](https://alex.kirk.at/2023/10/09/new-unit-tests-need-to-fail-running-the-old-code/)

## Why?

When fixing bugs or adding new features with tests, it's critical to verify that the new tests actually expose the problem they claim to solve. A test that passes with both the old (buggy) and new (fixed) code validates nothing.

**The principle**: Keep the new unit test, undo the other code changes. The unit test now needs to fail.

This action helps prevent inadequate test coverage by:

- Ensuring new tests for bug fixes actually expose the original bug
- Validating that tests aren't just checking trivial assertions
- Catching tests that pass due to mocking/stubbing issues
- Supporting Test-Driven Development (TDD) workflows

## How It Works

When a PR is opened or updated, this action:

1. Runs your tests with the PR changes (normal test run)
2. Reverts implementation code changes (keeping test modifications)
3. Runs the tests again
4. Expects the tests to **fail** without the implementation changes
5. If tests still pass, the validation fails (the tests don't properly test the bug fix or new feature)

## Usage

### Quick Start

Add this to your existing test workflow (e.g., `.github/workflows/test.yml`):

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Install dependencies
        run: # your dependency installation here

      - name: Validate tests fail without code changes
        uses: akirk/unit-test-failure@main
        with:
          test-command: composer test

      - name: Run test suite
        run: composer test
```

The validation step should run **before** your actual test suite to ensure new tests properly fail without the implementation changes.

### Skipping Validation for Test Coverage PRs

When adding tests to existing working code (not bug fixes), the tests should pass even with the old code. In these cases, you can skip validation using a PR label:

```yaml
- name: Validate tests fail without code changes
  uses: akirk/unit-test-failure@main
  with:
    test-command: composer test
  if: ${{ !contains(github.event.pull_request.labels.*.name, 'test-coverage') }}
```

Now when you add the `test-coverage` label to a PR, the validation will be skipped.

### Examples

#### Python (unittest)
```yaml
- uses: akirk/unit-test-failure@main
  with:
    test-command: python -m unittest discover -s tests
```

#### Python (pytest)
```yaml
- uses: akirk/unit-test-failure@main
  with:
    test-command: pytest
```

#### PHP (PHPUnit)
```yaml
- uses: akirk/unit-test-failure@main
  with:
    test-command: composer test
```

#### JavaScript/Node (npm)
```yaml
- uses: akirk/unit-test-failure@main
  with:
    test-command: npm test
```

#### JavaScript/Node (Jest with custom test directory)
```yaml
- uses: akirk/unit-test-failure@main
  with:
    test-command: jest
    test-directory: __tests__/
```

### Inputs

| Input | Required | Default | Description |
|-------|----------|---------|-------------|
| `test-command` | Yes | - | Command to run your tests |
| `test-directory` | No | `tests/` | Directory containing your tests |
| `base-ref` | No | PR base branch | Base branch to compare against |

### Outputs

| Output | Description |
|--------|-------------|
| `tests-changed` | Whether tests were modified (1 or 0) |
| `validation-passed` | Result: '1' (passed), '0' (failed), or 'skipped' |

## License

MIT
