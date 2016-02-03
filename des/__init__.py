from fiestel import fiestel
from keygen import *
from read_file import read_file
from utilities import bin_to_string

def process_des(filename, key, encryption):
	input_blocks = read_file(filename, encryption)
	keys = keygen(key)
	if encryption:
		input_blocks = [string_to_bin(x) for x in input_blocks]
	if not encryption:
		keys = list(reversed(keys))
	encoded_text = ''
	for block in input_blocks:
		encoded_text += fiestel(block, keys)
	if encryption:
		return encoded_text
	else:
		return bin_to_string(encoded_text)