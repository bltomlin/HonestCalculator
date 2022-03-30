"""
This file contains a function used to store the users result.
"""
def store_result(result, memory):
    """
    Check's the operator of the entered equation.
    :param result: answer from equation
    :param memory: double value user saves for future use
    """
	_exit = ''
	while _exit != 'exit':
		print("Do you want to store the result? (y / n):")
		answer = input()
		if answer == 'y':
			memory = result
			print("Do you want to continue calculations? (y / n):")
			answer = input()
			if answer == 'y':
				print("Enter an equation")
				user_input = grab_input()
				x_var, oper, y_var = data_collection(user_input, memory)
				x_var, oper, y_var = test(x_var, oper, y_var)
				check(x_var, y_var, oper)
				result = operator_check(x_var, oper, y_var, memory)
			else:
				return(memory)
				_exit = 'exit'
		else:
			if answer == 'n':
				print("Do you want to continue calculations? (y / n):")
				answer = input()
				if answer == 'y':
					print("Enter an equation")
					user_input = grab_input()
					x_var, oper, y_var = data_collection(user_input, memory)
					x_var, oper, y_var = test(x_var, oper, y_var)
					check(x_var, y_var, oper)
					result = operator_check(x_var, oper, y_var, memory)
				else:
					return(memory)
					_exit = 'exit'
			else:
				continue