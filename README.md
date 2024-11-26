<p align="center">
    <!--
    <a href="https://app.circleci.com/pipelines/github/jamesabel/tobool" alt="build">
        <img src="https://img.shields.io/circleci/build/gh/jamesabel/tobool" />
    </a>
    -->
    <a href="https://codecov.io/gh/jamesabel/tobool" alt="codecov">
        <img src="https://img.shields.io/codecov/c/github/jamesabel/tobool/master" />
    </a>
    <a href="https://pypi.org/project/tobool/" alt="pypi">
        <img src="https://img.shields.io/pypi/v/tobool" />
    </a>
    <a href="https://pypi.org/project/tobool/" alt="downloads">
        <img src="https://img.shields.io/pypi/dm/tobool" />
    </a>
    <!--
    <a alt="python">
        <img src="https://img.shields.io/pypi/pyversions/tobool" />
    </a>
    -->
    <a alt="license">
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
print(to_bool("None"))  # None
```

```python
from tobool import to_bool_strict

# to_bool_strict() will only return a bool
print(to_bool_strict("True"))  # True
print(to_bool_strict(None))  # False
```