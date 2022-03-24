def data_collection():
    response = ''
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    while response != 'exit':
        print(msg_0)
        user_input = input().split()
        x_var = float(user_input[0])
        oper = str(user_input[1])
        y_var = float(user_input[2])

        if type(x_var) == 'int' and type(y_var) == 'int':
            if '+-*/' in oper:
                response = 'exit'
            else:
                print(msg_2)
        else:
            print(msg_1)
data_collection()