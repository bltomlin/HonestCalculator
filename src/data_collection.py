def data_colection():
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

    print(msg_0)
    calc = input().split()
    num_x = float(calc[0])
    num_y = float(calc[2])
    oper = str(calc[1])

    while type(num_x) != 'float' or type(num_y) != 'float':
        print(msg_1)
        calc = input().split()
        num_x = float(calc[0])
        num_y = float(calc[2])
        oper = str(calc[1])

    while '+-*/' not in oper:
        print(msg_2)
        calc = input().split()
        num_x = float(calc[0])
        num_y = float(calc[2])
        oper = str(calc[1])
        while type(num_x) != 'float' or type(num_y) != 'float':
            print(msg_1)
            calc = input().split()
            num_x = float(calc[0])
            num_y = float(calc[2])
            oper = str(calc[1])

data_colection()