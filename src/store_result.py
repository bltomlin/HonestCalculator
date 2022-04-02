"""
This file contains a function used to store the users result.
"""
from src import is_one_digit, call_functions,


def store_result(result, memory):
    """
    Check's the operator of the entered equation.
    :param result: answer from equation
    :param memory: double value user saves for future use
    """
	msg = ["Are you sure? It is only one digit! (y / n)",
	"Don't be silly! It's just one number! Add to the memory? (y / n)",
	"Last chance! Do you really want to embarrass yourself? (y / n)"]
	_exit = ''
	while _exit != 'exit':
		msg_index = 0
		print("Do you want to store the result? (y / n):")
		answer = input()
		if answer == "y":
			if is_one_digit(result) == True and answer == "y":
				while is_one_digit(result) == True and answer == "y" and msg_index <= 2:
					print(msg[msg_index])
					answer = input()                
					if answer == "y":
						msg_index += 1
						if msg_index == 2:
							memory = result
					else:
						if answer == "n":
							break
						else:
							pass
			else:
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