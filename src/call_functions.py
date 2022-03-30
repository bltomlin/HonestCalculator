def call_functions(memory):
	print("Enter an equation")
	user_input = grab_input()
	x_var, oper, y_var = data_collection(user_input, memory)
	x_var, oper, y_var = test(x_var, oper, y_var)
	check(x_var, y_var, oper)
	result = operator_check(x_var, oper, y_var, memory)
	return result