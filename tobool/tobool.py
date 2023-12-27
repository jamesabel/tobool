from decimal import Decimal
from typing import Union


def strtobool(value: str) -> bool:
    """
    Convert a string representation of truth to true (1) or false (0).
    True values are 'y', 'yes', 'on', 'true', 't', '1', and any string
    starting with 'y', 'Y', 't', 'T', or '1'. False values are 'n', 'no',
    'off', 'false', 'f', '0', and any string starting with 'n', 'N', 'f',
    'F', or '0'. Raises ValueError if 'value' is anything else.

    This is a copy of the Python 3.5 version of distutils.util.strtobool()

    :param value: string value to convert
    :return: bool value of original value
    """
    value = value.lower()
    if value in ("y", "yes", "on", "true", "t", "1"):
        return True
    elif value in ("n", "no", "off", "false", "f", "0"):
        return False
    else:
        raise ValueError("invalid truth value %r" % (value,))


class ToBoolNoneValueException(Exception):
    ...


def to_bool(value: Union[str, bool, int, Decimal, None]) -> Union[bool, None]:
    """
    performs a casting of a multitude of values to bool.
    i.e. "true", "TRUE", "y", "Yes", "on", "1", 1, "false", "FALSE", "n", "No", "off", "0", 0, etc.
    :param value: input value
    :return: boolean value of original value
    """

    new_bool: Union[bool, None]  # for mypy
    if isinstance(value, bool):
        # bool has to come first since bools are also ints (i.e., isinstance(True, int) == True)
        new_bool = value
    elif value is None:
        new_bool = None
    elif isinstance(value, int) and 0 <= value <= 1:
        new_bool = bool(value)
    elif isinstance(value, Decimal) and (value == Decimal(0) or value == Decimal(1)):
        new_bool = bool(value)
    elif isinstance(value, str):
        value = value.strip().lower()
        if value == "none" or value == "null" or value == "nil" or value == "na":
            new_bool = None
        else:
            # strtobool actually returns an int
            new_bool = bool(strtobool(value))
    else:
        raise ValueError(value)

    return new_bool


def to_bool_strict(value: Union[str, bool, int, Decimal, None], fault_on_none: bool = False) -> bool:
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
