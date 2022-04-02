"""
This file contains a function used to call most of the main program.
"""
def call_functions(memory):
	"""
    Method for calling main functions in the program.
    :param memory: double value user saves for future use
    """
	print("Enter an equation")
	user_input = grab_input()
	x_var, oper, y_var = data_collection(user_input, memory)
	x_var, oper, y_var = test(x_var, oper, y_var)
	check(x_var, y_var, oper)
	result = operator_check(x_var, oper, y_var, memory)
	return result