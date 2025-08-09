"""Convert a number to a human readable suffixed form.

Parameters:
    number (int | float): Numeric input.
    decimal_points (int): Number of decimal points for scaled numbers.
    currency (str | None): Optional currency prefix (e.g. '$').
    strip_trailing_zeros (bool): If True, trim unnecessary trailing zeros and dot.

Behavior:
    * For absolute values below 1000 returns the (possibly rounded) number, not a suffixed string.
    * Supports negative numbers (sign preserved before currency if provided: -$1.2K).
    * Uses shared suffix table up to 10^42.

Returns:
    int | float | str: For small numbers returns numeric type; otherwise a formatted string.
"""

from __future__ import annotations
from typing import Union
from ._suffixes import POWERS_TO_SUFFIX


def numerize(
    number: Union[int, float],
    decimal_points: int = 2,
    currency: str | None = None,
    strip_trailing_zeros: bool = False,
) -> Union[int, float, str]:
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number.")
    if not isinstance(decimal_points, int) or decimal_points < 0:
        raise ValueError("Decimal points must be a non-negative integer.")

    sign = "-" if number < 0 else ""
    abs_number = abs(number)

    for power, suffix in POWERS_TO_SUFFIX:
        if abs_number >= 10**power:
            scaled = abs_number / (10**power)
            rounded = round(scaled, decimal_points)
            text = f"{rounded}"
            if strip_trailing_zeros and decimal_points > 0:
                # Remove trailing zeros and optional trailing dot
                text = text.rstrip("0").rstrip(".")
            prefix = f"{sign}{currency}" if currency else f"{sign}"
            return f"{prefix}{text}{suffix}"

    # Below lowest suffix threshold
    rounded_small = round(abs_number, decimal_points)
    if rounded_small.is_integer():
        rounded_small = int(rounded_small)
    if number < 0:
        rounded_small = -rounded_small
    return rounded_small
