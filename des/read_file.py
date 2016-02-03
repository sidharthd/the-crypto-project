from utilities import string_to_bin

def read_file(filename):
	file = open(filename, 'r')
	input_blocks = []
	while(True):
		block = file.read(8)
		if len(block) < 8:
			break
		input_blocks.append(block)
	input_blocks = [string_to_bin(x) for x in input_blocks]
	return input_blocks