def xor(a, b):
	'''Performs XOR operation on two binary strings.
	Binary strings here refer to strings of 0s and 1s.
	The two strings should be of equal length.
	Returns the result as a string.

	Samples:
	>>>xor('0', '1')
	'1'
	>>>xor('1011', '0010')
	'1001'
	'''

	length = len(a)
	output = ''
	for i in range(length):
		# Take a single character (of same index number) from each string and perform XOR operation 
		output += '0' if a[i]==b[i] else '1'
	return output