import numbers
from decimal import Decimal
from typing import Union
from functools import lru_cache


@lru_cache()
def strtobool(value: str) -> bool:
    """
    Convert a string representation of truth to True or False.
    True values are 'y', 'yes', 'on', 'true', 't', '1', 'enable', 'enabled', and 'active'.
    False values are 'n', 'no', 'off', 'false', 'f', '0', 'disable', 'disabled', and 'inactive'.
    Raises ValueError if 'value' is anything else.

    Derived from the Python 3.5 version of distutils.util.strtobool(), with additional vocabulary.

    :param value: string value to convert
    :return: bool value of original value
    """
    value = value.lower()
    if value in ("y", "yes", "on", "true", "t", "1", "enable", "enabled", "active"):
        return True
    elif value in ("n", "no", "off", "false", "f", "0", "disable", "disabled", "inactive"):
        return False
    else:
        raise ValueError("invalid truth value %r" % (value,))


class ToBoolNoneValueException(Exception):
    """raised by to_bool_strict() with fault_on_none=True when given any of the "None" values"""


@lru_cache()
def to_bool(value: Union[str, bytes, bool, int, float, Decimal, None]) -> Union[bool, None]:
    """
    performs a casting of a multitude of values to bool.
    i.e. "true", "TRUE", "y", "Yes", "on", "enabled", "1", "1.0", 1, 1.0, "false", "FALSE", "n", "No", "off", "disabled", "0", 0, 0.0, etc.
    Any numeric type (int, float, Decimal, Fraction, etc.) equal to 0 or 1 converts, NaN converts to None, and bytes are decoded and treated as strings.
    :param value: input value
    :return: boolean value of original value (None for the "missing value" representations such as None, "none", "null", "n/a", "", NaN, etc.)
    """

    new_bool: Union[bool, None]  # for mypy
    if isinstance(value, bool):
        # bool has to come first since bools are also ints (i.e., isinstance(True, int) == True)
        new_bool = value
    elif value is None:
        new_bool = None
    elif isinstance(value, numbers.Number):
        if value != value:
            # NaN is the only value not equal to itself and represents a missing value
            new_bool = None
        elif value == 0 or value == 1:
            new_bool = bool(value)
        else:
            raise ValueError(value)
    elif isinstance(value, (str, bytes)):
        if isinstance(value, bytes):
            value = value.decode()  # a non-decodable input raises UnicodeDecodeError, which is a ValueError
        value = value.strip().lower()
        if value in ("", "none", "null", "nil", "na", "nan", "n/a", "undefined"):
            new_bool = None
        else:
            try:
                new_bool = bool(strtobool(value))
            except ValueError:
                # numeric strings such as "0.0" and "1.0"
                try:
                    number = float(value)
                except ValueError:
                    raise ValueError(value) from None
                new_bool = to_bool(number)
    else:
        raise ValueError(value)

    return new_bool


@lru_cache()
def to_bool_strict(value: Union[str, bytes, bool, int, float, Decimal, None], fault_on_none: bool = False) -> bool:
    """
    Like to_bool(), except the return is strictly only a bool (the "strict" is on the output). A None return becomes a False.
    Good for strict return typing and not having to worry about Python's "truthiness" on a None.
    If `fault_on_none` is set to True the input is also strict (any of the "None" values will raise a ToBoolNoneValueException).
    :param value: input value
    :param fault_on_none: set to True to fault if any of the "None" values are passed (False to convert a None to False, which is the default), i.e. be strict on input
    :return: boolean value of original value
    """
    new_bool = to_bool(value)
    if new_bool is None:
        if fault_on_none:
            raise ToBoolNoneValueException(value)
        else:
            new_bool = False
    return new_bool
