from utilities import string_to_bin

def read_file(filename, encryption):
	if encryption:
		block_length = 8
	else:
		block_length = 64

	file = open(filename, 'r')

	input_blocks = []

	while(True):
		block = file.read(block_length)

		if not block:
			break

		# Check if the file can be decrypted.
		if (encryption == 0) and (len(block) != 64):
			print 'not encryption'
			return 'not_encrypted_file'

		input_blocks.append(block)

		if len(block) < block_length:
			break

	return input_blocks