import pytest

from numerize_denumerize.numerize import numerize


def test_numerize_small_number_returns_number():
    # For numbers < 1000 it should return the rounded number (not a suffixed string)
    assert numerize(42) == 42
    assert isinstance(numerize(42), (int, float))


def test_numerize_thousand_to_k():
    assert numerize(1500) == "1.5K"


def test_numerize_million_rounding_default():
    # 1_234_567 / 1e6 = 1.234567 -> rounds to 1.23 with default 2 decimal points
    assert numerize(1_234_567) == "1.23M"


def test_numerize_million_custom_decimal_points():
    # 1 decimal point
    assert numerize(1_234_567, decimal_points=1) == "1.2M"


def test_numerize_large_peta():
    assert numerize(10**15) == "1.0P"


def test_numerize_currency_prefix():
    assert numerize(2500, currency="$") == "$2.5K"


def test_numerize_invalid_number_type():
    with pytest.raises(ValueError):
        numerize("1234")  # type: ignore[arg-type]


def test_numerize_invalid_decimal_points_type():
    with pytest.raises(ValueError):
        numerize(1000, decimal_points="2")  # type: ignore[arg-type]


def test_numerize_invalid_decimal_points_negative():
    with pytest.raises(ValueError):
        numerize(1000, decimal_points=-1)


def test_numerize_exact_1000():
    assert numerize(1000) == "1.0K"


def test_numerize_zero():
    assert numerize(0) == 0


def test_numerize_boundary_before_million():
    # Ensure rounding does not incorrectly carry to next suffix
    assert numerize(999_950) == "999.95K"  # not 1.0M


def test_numerize_exact_large_power():
    assert numerize(10**42) == "1.0D"


def test_numerize_decimal_points_zero():
    # Current behavior: Python round(1.53, 0) -> 2.0
    assert numerize(1530, decimal_points=0) == "2.0K"


def test_numerize_negative_number():
    assert numerize(-1500) == "-1.5K"


def test_numerize_negative_with_currency():
    assert numerize(-1500, currency="$") == "-$1.5K"


def test_numerize_strip_trailing_zeros():
    assert numerize(1500, decimal_points=2, strip_trailing_zeros=True) == "1.5K"
    assert numerize(1_000_000, decimal_points=2, strip_trailing_zeros=True) == "1M"
