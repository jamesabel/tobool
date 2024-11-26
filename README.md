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