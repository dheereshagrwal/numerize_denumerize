"""Shared suffix mappings between numerize and denumerize.

POWERS_TO_SUFFIX: list of (power_of_ten, suffix) in descending order.
SUFFIX_TO_POWER: reverse lookup dict.
"""

POWERS_TO_SUFFIX = [
    (42, "D"),
    (39, "N"),
    (36, "O"),
    (33, "S"),
    (30, "F"),
    (27, "U"),
    (24, "Y"),
    (21, "Z"),
    (18, "E"),
    (15, "P"),
    (12, "T"),
    (9, "B"),
    (6, "M"),
    (3, "K"),
]

SUFFIX_TO_POWER = {s: p for p, s in POWERS_TO_SUFFIX}
