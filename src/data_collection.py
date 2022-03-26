"""
This module contains a function that will convert
data to desired type in this project.
"""

def data_collection(user_input):
    """
    Assigns data type based on compatibility.
    Ex: 'm' will be assigned str. 2.3 or 2 
    will be assigned float.

    :param user_input: list containing strings
    from user input
    :return: variables with correct types for program
    """
    x_var = type_check(user_input[0])
    oper = user_input[1]
    y_var = type_check(user_input[2])
    return x_var, oper, y_var