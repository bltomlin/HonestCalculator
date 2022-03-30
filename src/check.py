def check(x_var, y_var, oper):
	msg = ""
	if is_one_digit(x_var) and is_one_digit(y_var):
		msg += " ... lazy"
	if (x_var == 1 or y_var == 1) and oper == '*':
		msg += " ... very lazy"
	if (x_var == 0 or y_var == 0) and oper in ['*', '+', '-']:
		msg += " ... very, very lazy"
	if msg != "":
		msg = "You are" + msg
		print(msg)