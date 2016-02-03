from utilities import string_to_bin

def read_file(filename, encryption):
	print encryption
	if encryption:
		block_length = 8
	else:
		block_length = 64
	file = open(filename, 'r')
	input_blocks = []
	while(True):
		block = file.read(block_length)
		print block
		if len(block) < block_length:
			break
		input_blocks.append(block)
	return input_blocks