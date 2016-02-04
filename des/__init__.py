from fiestel import fiestel
from keygen import *
from read_file import read_file
from utilities import bin_to_string

def process_des(filename, key, encryption):
	input_blocks = read_file(filename, encryption)
	keys = keygen(key)

	if encryption:
		# Convert each block to binary if operation is encryption.
		input_blocks = [string_to_bin(x) for x in input_blocks]

		# Pad zeroes to the end, if last block has less than 64 bits.
		if len(input_blocks[-1]) < 64:
			input_blocks[-1] += '0' * (64 - len(input_blocks[-1]))

	if not encryption:
		# Reverse the key schedule if operation is decryption.
		keys = list(reversed(keys))

	encoded_text = ''
	for block in input_blocks:
		encoded_text += fiestel(block, keys)

	if encryption:
		# Return cipher text as binary.
		return encoded_text
	else:
		# Remove padded zeroes if any.
		for i in range(64, 0, -8):
			if encoded_text[-8:] == '0' * 8:
				encoded_text = encoded_text[:-8]
			else:
				break

		# Convert binary to normal string.
		return bin_to_string(encoded_text)