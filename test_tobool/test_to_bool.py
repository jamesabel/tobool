import pytest

from decimal import Decimal

from tobool import to_bool


def test_type_conversion():
    test_values = {
        False: [False, "F", "false", "False", "FALSE", "F", "N", "no", 0, Decimal(0), Decimal(0.0), "off", " f"],
        True: [True, "T", "true", "yes", "Y", 1, Decimal(1), Decimal(1.0), "on", "   T   ", "  t "],
        None: [None, "None", "NULL", "null", " None", "nil", "na", "NA"],
    }
    for value, variants in test_values.items():
        for variant in variants:
            assert value == to_bool(variant)

    test_unsupported_values = {False: ["Nope", -1, "Nada", "fuggedaboutit", Decimal(-1)], True: ["Yup", "Si", 1.1, Decimal(100.0), Decimal(0.5)], None: ["huh?", "no idea", "nah"]}
    for value, variants in test_unsupported_values.items():
        for variant in variants:
            with pytest.raises(ValueError):
                to_bool(variant)
