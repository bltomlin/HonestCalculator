"""
This file contains the main entry point for the program that
dictates all logical flow.
"""
from src import call_functions, store_result


def honest_calculator():
    """
    Entry point for program.

    :return: void
    """
    memory = 0
    result = call_functions()
    store_result(result, memory)


if __name__ == '__main__':
    honest_calculator()
