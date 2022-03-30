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
				result = call_functions(memory)
			else:
				return(memory)
				_exit = 'exit'
		else:
			if answer == 'n':
				print("Do you want to continue calculations? (y / n):")
				answer = input()
				if answer == 'y':
					result = call_functions(memory)
				else:
					return(memory)
					_exit = 'exit'
			else:
				continue