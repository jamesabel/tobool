import pytest
from copy import deepcopy

from decimal import Decimal

from tobool import to_bool, to_bool_strict, ToBoolNoneValueException

test_values = {
    False: [False, "F", "false", "False", "FALSE", "N", "no", 0, Decimal(0), "off", " f", "0"],
    True: [True, "T", "true", "yes", "Y", 1, Decimal(1), "on", "   T   ", "  t ", "1"],
    None: [None, "None", "NONE", "NULL", "null", " None", "nil", "na", "NA"],
}


def clear_caches():
    # to_bool() and to_bool_strict() are lru_cache'd, and equal-hashing inputs (e.g. Decimal(0) and False)
    # share a cache entry, so the caches must be cleared before each call to ensure the code actually runs
    to_bool.cache_clear()
    to_bool_strict.cache_clear()


def test_type_conversion():
    for value, variants in test_values.items():
        for variant in variants:
            clear_caches()
            new_value = to_bool(variant)
            assert type(new_value) is bool or new_value is None
            assert value == new_value

    test_unsupported_values = {False: ["Nope", -1, "Nada", "fuggedaboutit", Decimal(-1)], True: ["Yup", "Si", 1.1, Decimal(100.0), Decimal(0.5)], None: ["huh?", "no idea", "nah", ""]}
    for value, variants in test_unsupported_values.items():
        for variant in variants:
            clear_caches()
            with pytest.raises(ValueError):
                to_bool(variant)


def test_strict():

    # modify the "regular" test set and make all the None values False
    strict_test_values = deepcopy(test_values)
    strict_test_values[False].extend(test_values[None])
    del strict_test_values[None]

    for value, variants in strict_test_values.items():
        for variant in variants:
            clear_caches()
            new_value = to_bool_strict(variant)
            assert type(new_value) is bool
            assert value == new_value


def test_strict_exception():

    # test that ToBoolNoneValueException is raised on any "None" value
    for value, variants in test_values.items():
        for variant in variants:
            clear_caches()
            if value is None:
                with pytest.raises(ToBoolNoneValueException):
                    to_bool_strict(variant, True)
            else:
                result = to_bool_strict(variant, True)
                assert type(result) is bool
                assert value == result
