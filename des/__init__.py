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
		# Convert binary to normal string.
		return bin_to_string(encoded_text)