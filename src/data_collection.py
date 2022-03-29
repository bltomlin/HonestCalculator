"""
This module contains a function that will convert
data to desired type in this project.
"""
from src import type_check


def data_collection(user_input, memory):
    """
    Assigns data type based on compatibility.
    Ex: 'm' will be assigned str. 2.3 or 2 will be assigned float.

    :param user_input: list containing strings from user input
    :param memory: user answer stored for future use
    :return: variables with correct types for program
    """
    x_var = type_check(user_input[0], memory)
    oper = user_input[1]
    y_var = type_check(user_input[2], memory)
    return x_var, oper, y_var