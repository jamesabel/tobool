from decimal import Decimal
import distutils.util
from typing import Union


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
            new_bool = bool(distutils.util.strtobool(value))
    else:
        raise ValueError(value)

    return new_bool


def to_bool_strict(value: Union[str, bool, int, Decimal, None]) -> bool:
    """
    Like to_bool(), except the return is strictly only a bool. A None return becomes a False. Good for strict typing and not having to worry about Python's "truthiness".
    :param value: input value
    :return: boolean value of original value
    """
    new_bool = to_bool(value)
    if new_bool is None:
        new_bool = False
    return new_bool
