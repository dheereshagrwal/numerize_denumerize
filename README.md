# numerize_denumerize

Human-friendly number abbreviator and parser supporting large powers up to 10^42.

```
1234567   -> 1.23M
$2.5K     -> 2500
1D        -> 1000000000000000000000000000000000000000000 (10^42)
```

## Features

- Abbreviates numbers with suffixes: K M B T P E Z Y U F S O N D (up to 10^42)
- Reverses abbreviations back to precise integers (no float precision loss)
- Optional currency prefix handling (e.g. $ £ €)
- Negative number support (e.g. -$1.5K)
- Configurable decimal points and optional trailing zero stripping
- Typed (PEP 561) and tested

## Install

```
pip install numerize_denumerize
```

## Quick Start

```python
from numerize_denumerize import numerize, denumerize

print(numerize(1_234_567))                 # '1.23M'
print(numerize(1_234_567, decimal_points=1))  # '1.2M'
print(numerize(1500, currency="$"))       # '$1.5K'
print(numerize(-1500))                     # '-1.5K'
print(numerize(1_000_000, strip_trailing_zeros=True))  # '1M'

print(denumerize("1.23M"))  # 1230000
print(denumerize("$1.5K"))  # 1500
print(denumerize("1D"))     # 10**42
```

## API

```python
numerize(number: int | float, decimal_points: int = 2, currency: str | None = None, strip_trailing_zeros: bool = False) -> int | float | str
denumerize(number_string: str) -> int | float
```

## Suffix Table

| Suffix | Power | Example                  |
| ------ | ----- | ------------------------ |
| K      | 10^3  | 1.2K = 1_200             |
| M      | 10^6  | 3.4M = 3_400_000         |
| B      | 10^9  | 1.0B = 1_000_000_000     |
| T      | 10^12 | 1.0T = 1_000_000_000_000 |
| P      | 10^15 | 1.0P = 10\*\*15          |
| E      | 10^18 | 1.0E = 10\*\*18          |
| Z      | 10^21 | 1.0Z = 10\*\*21          |
| Y      | 10^24 | 1.0Y = 10\*\*24          |
| U      | 10^27 | 1.0U = 10\*\*27          |
| F      | 10^30 | 1.0F = 10\*\*30          |
| S      | 10^33 | 1.0S = 10\*\*33          |
| O      | 10^36 | 1.0O = 10\*\*36          |
| N      | 10^39 | 1.0N = 10\*\*39          |
| D      | 10^42 | 1.0D = 10\*\*42          |

## Why this package?

Most alternatives stop at trillions or lose precision when parsing very large numbers. This library:

- Preserves integer precision using `Decimal` / int parsing
- Round-trips formatting + parsing reliably
- Offers optional formatting niceties (currency, trailing zero stripping)

## Testing

```
pip install numerize_denumerize[tests]
pytest -q
```

## Contributing

Issues and PRs welcome. Please add tests for new functionality.

## License

MIT – see `LICENSE`.
