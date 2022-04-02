"""
This file contains a function used to evaluate the difficulty of a user entered equation
"""
def check(x_var, y_var, oper):
	"""
    Evaluates the students bravery when entering equations.
    :param x_var: the float x variable of the equation 
    :param oper: the str operator of the equation
    :param y_var: the float y variable of the equation
    """
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

