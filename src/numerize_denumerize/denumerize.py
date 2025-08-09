"""Convert a suffixed human-readable number back to its numeric value.

Supported suffixes (powers of 10):
    K=10^3, M=10^6, B=10^9, T=10^12, P=10^15, E=10^18, Z=10^21,
    Y=10^24, U=10^27, F=10^30, S=10^33, O=10^36, N=10^39, D=10^42

Also tolerates an optional single leading currency symbol (e.g. $ or £)
added by the companion numerize() function.

Examples:
    denumerize("1.5K") -> 1500
    denumerize("$2.5K") -> 2500
    denumerize("42") -> 42

Raises:
    ValueError: on invalid input type or format.
"""

import re
from typing import Union
from decimal import Decimal, InvalidOperation
from ._suffixes import SUFFIX_TO_POWER

_SUFFIXES = SUFFIX_TO_POWER

_NUMBER_PATTERN = re.compile(
    r"^\s*([^0-9A-Za-z\-+]?)([-+]?\d+(?:\.\d+)?)([A-Za-z]?)\s*$"
)


def denumerize(number_string: str) -> Union[int, float]:
    if not isinstance(number_string, str):
        raise ValueError("Input must be a string.")

    match = _NUMBER_PATTERN.match(number_string)
    if not match:
        raise ValueError("Invalid formatted number string.")

    currency, numeric_part, suffix = match.groups()
    # currency part is ignored intentionally; presence is allowed but not required
    # Choose precise numeric base (int if whole, otherwise Decimal for precision)
    if "." in numeric_part:
        try:
            base: Union[int, Decimal] = Decimal(numeric_part)
        except InvalidOperation:
            raise ValueError("Invalid numeric component.")
    else:
        # handles signs automatically
        base = int(numeric_part)

    if suffix:
        suffix = suffix.upper()
        if suffix not in _SUFFIXES:
            raise ValueError(f"Unknown suffix '{suffix}'.")
        power = 10 ** _SUFFIXES[suffix]
        base = base * (power if isinstance(base, int) else Decimal(power))

    # Normalize to int if integral
    if isinstance(base, Decimal):
        if base == base.to_integral():
            return int(base)
        return float(base)  # safe; precision only matters when integral comparison used
    return base
