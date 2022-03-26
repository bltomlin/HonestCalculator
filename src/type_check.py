def type_check(some_input):
    try: 
        some_input = float(some_input)
        return some_input
    except ValueError:
        some_input = str(some_input)
        return some_input
