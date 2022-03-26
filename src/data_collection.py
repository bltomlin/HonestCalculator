def data_collection(user_input):
    x_var = type_check(user_input[0])
    oper = user_input[1]
    y_var = type_check(user_input[2])
    return x_var, oper, y_var