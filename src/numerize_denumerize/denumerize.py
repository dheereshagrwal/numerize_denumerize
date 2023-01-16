import re
def denumerize(number_string):
    if not isinstance(number_string, str):
        raise ValueError("Input must be a string.")
    number_string = number_string.strip()
    suffixes = {
        'K': 3,
        'M': 6,
        'B': 9,
        'T': 12,
        'P': 15,
        'E': 18,
        'Z': 21,
        'Y': 24,
        'U': 27,
        'F': 30,
        'S': 33,
        'O': 36,
        'N': 39,
        'D': 42
    }
    suffix = re.search(r'[A-Za-z]', number_string[-1])
    if suffix:
        suffix = suffix.group()
        if suffix in suffixes:
            number = float(
                re.search(r'[0-9]+\.?[0-9]*', number_string).group())
            return number * 10**suffixes[suffix]
    else:
        return float(number_string)
