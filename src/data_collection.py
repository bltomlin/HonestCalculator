def data_collection(user_input):
    x_var = type_check(user_input[0])
    oper = user_input[1]
    y_var = type_check(user_input[2])
    return x_var, oper, y_var
    
def type_check(some_input):
    try: 
        some_input = float(some_input)
        return some_input
    except ValueError:
        some_input = str(some_input)
        return some_input
        

def test(x_var, oper, y_var):
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


def grab_input():
    user_input = input().split()
    return user_input

def main():
    print("Enter an equation")
    user_input = grab_input()
    x_var, oper, y_var = data_collection(user_input)
    test(x_var, oper, y_var)

main()