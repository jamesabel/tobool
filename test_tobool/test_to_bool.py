import pytest
from copy import deepcopy

from decimal import Decimal
from fractions import Fraction

from tobool import to_bool, to_bool_strict, ToBoolNoneValueException

test_values = {
    False: [False, "F", "false", "False", "FALSE", "N", "no", 0, 0.0, Decimal(0), Fraction(0), "off", " f", "0", "0.0", b"false", b"0", "disable", "disabled", "inactive"],
    True: [True, "T", "true", "yes", "Y", 1, 1.0, Decimal(1), Fraction(1), "on", "   T   ", "  t ", "1", "1.0", b"true", b"1", "enable", "enabled", "active"],
    None: [None, "None", "NONE", "NULL", "null", " None", "nil", "na", "NA", "nan", "NaN", "n/a", "N/A", "undefined", "", float("nan"), Decimal("NaN")],
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

    # "Si" stays unsupported: internationalization is out of scope
    test_unsupported_values = {
        False: ["Nope", -1, "Nada", "fuggedaboutit", Decimal(-1), -1.0, Fraction(-1), b"nope"],
        True: ["Yup", "Si", 1.1, Decimal(100.0), Decimal(0.5), float("inf"), "2.0", "1e6", b"\xfftrue"],
        None: ["huh?", "no idea", "nah", object()],
    }
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
