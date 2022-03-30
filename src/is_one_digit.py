def is_one_digit(num):
	output = ''
	if num > -10 and num < 10 and num.is_integer():
		output = True
	else:
		output = False
	return output