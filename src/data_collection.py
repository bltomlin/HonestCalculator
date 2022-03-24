def data_collection(user_input):
    x_var = int(user_input[0])
    oper = str(user_input[1])
    y_var = int(user_input[2])
    return x_var, oper, y_var

def test(x_var, oper, y_var):
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    response = ''
    while response != 'exit':
        if type(x_var) is int and type(y_var) is int:
            if oper in ['+', '-', '*', '/']:
                response = 'exit'
            else:
                print(msg_2)
                quit()
        else:
            print(msg_1)
            quit()


def grab_input(msg_0):
    print(msg_0)
    user_input = input().split()
    return user_input

def main():
    msg_0 = "Enter an equation"
    user_input = grab_input(msg_0)
    data_collection(user_input)
    x_var, oper, y_var = data_collection(user_input)
    test(x_var, oper, y_var)

main()