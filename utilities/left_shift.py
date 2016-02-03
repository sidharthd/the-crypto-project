def left_shift(input, shifts):
	output = ''
	for i in range(shifts):
		output = input[shifts:] + input[:shifts]
	return output