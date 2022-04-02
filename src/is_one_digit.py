"""
This file contains a function used to validate how many digits are in the number.
"""
from src import is_integer

def is_one_digit(num):
	"""
    Check's if number is single digit.
    :param num: value of integer being checked
    """
	output = ''
	if num > -10 and num < 10 and num.is_integer():
		output = True
	else:
		output = False
	return output