import pytest
from copy import deepcopy

from decimal import Decimal

from tobool import to_bool, to_bool_strict, ToBoolNoneValueException

test_values = {
    False: [False, "F", "false", "False", "FALSE", "F", "N", "no", 0, Decimal(0), Decimal(0.0), "off", " f"],
    True: [True, "T", "true", "yes", "Y", 1, Decimal(1), Decimal(1.0), "on", "   T   ", "  t "],
    None: [None, "None", "NONE", "NULL", "null", " None", "nil", "na", "NA"],
}


def test_type_conversion():
    for value, variants in test_values.items():
        for variant in variants:
            new_value = to_bool(variant)
            assert type(new_value) is bool or new_value is None
            assert value == new_value

    test_unsupported_values = {False: ["Nope", -1, "Nada", "fuggedaboutit", Decimal(-1)], True: ["Yup", "Si", 1.1, Decimal(100.0), Decimal(0.5)], None: ["huh?", "no idea", "nah", ""]}
    for value, variants in test_unsupported_values.items():
        for variant in variants:
            with pytest.raises(ValueError):
                to_bool(variant)


def test_strict():

    # modify the "regular" test set and make all the None values False
    strict_test_values = deepcopy(test_values)
    strict_test_values[False].extend(test_values[None])
    del strict_test_values[None]

    for value, variants in strict_test_values.items():
        for variant in variants:
            new_value = to_bool_strict(variant)
            assert type(new_value) is bool
            assert value == new_value


def test_strict_exception():

    # test that ToBoolNoneValueException is raises on any "None" value
    for value, variants in test_values.items():
        if value is None:
            with pytest.raises(ToBoolNoneValueException):
                to_bool_strict(value, True)
        else:
            result = to_bool_strict(value, True)
            assert isinstance(result, bool)
            assert type(result) == bool
