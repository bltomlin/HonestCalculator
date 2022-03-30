def check(x_var, y_var, oper):
	msg = ""
	if 0 < x_var.is_integer() < 10 and 0 < y_var .is_integer() < 10:
		msg += " ... lazy"
	if (x_var == 1 or y_var == 1) and oper == '*':
		msg += " ... very lazy"
	if (x_var == 0 or y_var == 0) and oper in ['*', '+', '-']:
		msg += " ... very, very lazy"
	if msg != "":
		msg = "You are" + msg
		print(msg)