# 📘 Assignment: Testing Python Programs with unittest

## 🎯 Objective

Learn how to verify Python programs with the standard-library `unittest` framework by writing assertions, covering edge cases, and using failing tests to find and fix a defect.

## 📝 Tasks

### 🛠️ Write Basic Unit Tests

#### Description

Complete the test class in the starter code so that each provided function has a clear test for its expected behavior.

#### Requirements

Completed program should:

- Use `unittest.TestCase` and test methods whose names begin with `test_`.
- Test `is_even()` with both an even number and an odd number.
- Test `format_name()` with a representative first name and last name.
- Use appropriate assertions such as `assertTrue`, `assertFalse`, and `assertEqual`.

### 🛠️ Cover Edge Cases

#### Description

Expand the test suite to check inputs that are easy to overlook or that could expose an incorrect implementation.

#### Requirements

Completed program should:

- Test `is_even()` with zero and at least one negative number.
- Test `calculate_discount()` with a zero-percent discount and a nonzero discount.
- Test `format_name()` with names that include surrounding whitespace.
- Include at least six meaningful test methods in total.

Example command:

```text
python3 starter-code.py
```

### 🛠️ Find and Fix a Defect

#### Description

Use the completed tests to identify a defect in the provided code, correct the implementation, and add a regression test that prevents the defect from returning.

#### Requirements

Completed program should:

- Run the full test suite and interpret a failing assertion.
- Correct the defect in `calculate_discount()` without weakening or deleting the failing test.
- Add a regression test that checks the corrected discount calculation.
- Finish with all tests passing when run with `python3 starter-code.py`.
