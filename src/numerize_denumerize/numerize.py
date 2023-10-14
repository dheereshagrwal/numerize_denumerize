
def numerize(number, decimal_points=2,currency=None):
    if not isinstance(number, (int, float)):
        raise ValueError("Input must be a number.")
    if not isinstance(decimal_points, int) or decimal_points < 0:
        raise ValueError("Decimal points must be a non-negative integer.")
    suffixes = {
        42: 'D',
        39: 'N',
        36: 'O',
        33: 'S',
        30: 'F',
        27: 'U',
        24: 'Y',
        21: 'Z',
        18: 'E',
        15: 'P',
        12: 'T',
        9: 'B',
        6: 'M',
        3: 'K'
    }
    for suffix in suffixes:
        if number >= 10**suffix:
            number /= 10**suffix
            return f"{round(number, decimal_points)}{suffixes[suffix]}" if currency is None else f"{currency}{round(number, decimal_points)}{suffixes[suffix]}"
    return round(number, decimal_points)

