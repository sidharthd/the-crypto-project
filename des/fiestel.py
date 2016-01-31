from utilities import xor

def fiestel(input_block, round_keys):
	rounds = 16
	length = len(input_block)
	left_half = input_block[:length/2]
	right_half = input_block[length/2:]
	
	for round in range(rounds):	
		next_left_half = right_half

		# Expand the right half from 32 bits to 48 bits.
		expanded_right_half = ''
		for i in range(4, (length/2)+1, 4):
			try:
				expanded_right_half += right_half[i-4:i]
				expanded_right_half += right_half[i] + right_half[i-1]
			except IndexError:
				pass
		expanded_right_half = right_half[length/2-1] + expanded_right_half + right_half[0]
		right_half = expanded_right_half

		# XOR the expanded right half with round key.
		right_half = xor(right_half, round_keys[round])

		return right_half