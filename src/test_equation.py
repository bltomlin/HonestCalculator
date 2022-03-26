def test_equation(x_var, oper, y_var):
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    response = ''
    while response != 'exit':
        if type(x_var) is float and type(y_var) is float:
            if oper in ['+', '-', '*', '/']:
                response = 'exit'
            else:
                print(msg_2)
                print("Enter an equation")
                x_var, oper, y_var = data_collection(grab_input())
        else:
            print(msg_1)
            print("Enter an equation")
            x_var, oper, y_var = data_collection(grab_input())

