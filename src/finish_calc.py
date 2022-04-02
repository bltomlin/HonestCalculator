def finish_calc(memory):
	print("Do you want to continue calculations? (y / n):")
	answer = input()
	if answer == 'y':
		result = call_functions(memory)
		return result
	else:
		return(memory)
		_exit = 'exit'