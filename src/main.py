def honest_calculator():
    print("Enter an equation")
    user_input = grab_input()
    x_var, oper, y_var = data_collection(user_input)
    test_equation(x_var, oper, y_var)

if __name__ == '__main__':
    honest_calculator()
