<p align="center">
    <a href="https://github.com/jamesabel/tobool/actions/workflows/python-package.yml" alt="build">
        <img src="https://img.shields.io/github/actions/workflow/status/jamesabel/tobool/python-package.yml?branch=main" />
    </a>
    <a href="https://pypi.org/project/tobool/" alt="pypi">
        <img src="https://img.shields.io/pypi/v/tobool" />
    </a>
    <a href="https://pypi.org/project/tobool/" alt="downloads">
        <img src="https://img.shields.io/pypi/dm/tobool" />
    </a>
    <a href="https://github.com/jamesabel/tobool/blob/main/LICENSE" alt="license">
        <img src="https://img.shields.io/github/license/jamesabel/tobool" />
    </a>
</p>

# tobool

Convert many different representations of a bool to an actual bool or a None

# Usage

```
pip install tobool
```

```python
from tobool import to_bool

# Examples:
print(to_bool("True"))  # True
print(to_bool("False"))  # False
print(to_bool("Yes"))  # True
print(to_bool("T"))  # True
print(to_bool(1))  # True
print(to_bool(1.0))  # True
print(to_bool("1.0"))  # True
print(to_bool("enabled"))  # True
print(to_bool(b"true"))  # True
print(to_bool("None"))  # None
print(to_bool("n/a"))  # None
print(to_bool(float("nan")))  # None
```

```python
from tobool import to_bool_strict

# to_bool_strict() will only return a bool
print(to_bool_strict("True"))  # True
print(to_bool_strict(None))  # False
print(to_bool_strict(None, True))  # tobool.tobool.ToBoolNoneValueException: None
```