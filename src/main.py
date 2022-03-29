"""
This file contains the main entry point for the program that
dictates all logical flow.
"""
from src import data_collection, grab_input, test_equation


def honest_calculator():
    """
    Entry point for program.

    :return: void
    """
    memory = 0
    print("Enter an equation")
    user_input = grab_input()
    x_var, oper, y_var = data_collection(user_input, memory)
    x_var, oper, y_var = test(x_var, oper, y_var)
    result = operator_check(x_var, oper, y_var, memory)
    store_result(result, memory)


if __name__ == '__main__':
    honest_calculator()
