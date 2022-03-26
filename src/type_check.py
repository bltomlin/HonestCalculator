"""
This file contains a function used to assign the correct type
on a user entered equation.
"""


def type_check(some_input):
    """
    Assign the correct type on a user entered equation to avoid
    accomodate a failure to input numbers in an equation.

    :param some_input: an element from the user input list.
    """
    try: 
        some_input = float(some_input)
        return some_input
    except ValueError:
        some_input = str(some_input)
        return some_input
