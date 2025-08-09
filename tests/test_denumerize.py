import pytest

from numerize_denumerize.denumerize import denumerize


def test_denumerize_no_suffix():
    assert denumerize("42") == 42


def test_denumerize_k():
    assert denumerize("1.5K") == 1500


def test_denumerize_currency():
    assert denumerize("$2.5K") == 2500


def test_denumerize_large_suffix():
    assert denumerize("1P") == 10**15


def test_denumerize_invalid_type():
    with pytest.raises(ValueError):
        denumerize(1234)  # type: ignore[arg-type]


def test_denumerize_bad_suffix():
    with pytest.raises(ValueError):
        denumerize("1.2Q")


def test_denumerize_invalid_format():
    with pytest.raises(ValueError):
        denumerize("abc")


def test_denumerize_lowercase_suffix():
    assert denumerize("1.5k") == 1500


def test_denumerize_spaces():
    assert denumerize(" 1.5K ") == 1500


def test_denumerize_negative():
    assert denumerize("-1.2K") == -1200


def test_denumerize_positive_sign():
    assert denumerize("+1.2K") == 1200


def test_denumerize_currency_pound():
    assert denumerize("£1.0M") == 1_000_000


def test_denumerize_very_large():
    assert denumerize("1D") == 10**42


def test_denumerize_int_normalization():
    # Should return int not float when whole
    assert isinstance(denumerize("1.0K"), int)
    assert denumerize("1.0K") == 1000


def test_denumerize_multiple_suffix_invalid():
    with pytest.raises(ValueError):
        denumerize("1KK")


def test_denumerize_internal_space_invalid():
    with pytest.raises(ValueError):
        denumerize("1 000K")
