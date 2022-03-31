"""
This file contains a function used to validate the operator in equation.
"""
from src import data_collection, grab_input, test_equation


def operator_check(x_var, oper, y_var, memory):
    """
    Check's the operator of the entered equation.
    :param x_var: the float x variable of the equation 
    :param oper: the str operator of the equation
    :param y_var: the float y variable of the equation
    :param memory: user answer stored for future use
    """
    response = ''
    while response != 'exit':
        if oper == '+':
            print(x_var + y_var)
            return(x_var + y_var)
            response = 'exit'
        elif oper == '-':
            print(x_var - y_var)
            return(x_var - y_var)
            response = 'exit'
        elif oper == '*':
            print(x_var * y_var)
            return(x_var * y_var)
            response = 'exit'
        else:
            if oper == '/' and y_var != 0:
                print(x_var / y_var)
                return(x_var / y_var)
                response = 'exit'
            else:
                print("Yeah... division by zero. Smart move...")
                print("Enter an equation")
                x_var, oper, y_var = data_collection(grab_input(), memory)
                test(x_var, oper, y_var)
                check(x_var, y_var, oper)