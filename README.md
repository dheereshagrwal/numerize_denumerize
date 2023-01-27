numerize_denumerize

A python package to numerize and denumerize numbers.
Installation

Use pip to install the package:

pip3 install numerize_denumerize

Usage

from numerize_denumerize import numerize, denumerize

# Numerize
print(numerize.numerize(10000000, decimal_points=2))  # '10.00M'

# Denumerize
print(denumerize.denumerize('10.00M'))  # 10000000
Methods
numerize(number, decimal_points=2)

This method takes a number and returns a string in the format of x.xxM or x.xxK or x.xxB based on the number.
denumerize(number_string)

This method takes a string in the format of x.xxM or x.xxK or x.xxB and returns the actual number.
Note

Please make sure you provide correct format while calling denumerize method.
License

This project is licensed under the MIT License - see the LICENSE file for details.
