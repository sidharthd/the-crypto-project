from hashlib import sha256
from utilities import string_to_bin, left_shift

def keygen(key):
	key_hash = sha256(key).hexdigest()
	key = string_to_bin(key_hash[:8])
	pc1 = [
		57, 49, 41, 33, 25, 17, 9,
		1, 58, 50, 42, 34, 26, 18,
		10, 2, 59, 51, 43, 35, 27,
		19, 11, 3, 60, 52, 44, 36,
		63, 55, 47, 39, 31, 23, 15,
		7, 62, 54, 46, 38, 30, 22,
		14, 6, 61, 53, 45, 37, 29,
		21, 13, 5, 28, 20, 12, 4
	]

	pc2 = [
		14, 17, 11, 24, 1, 5, 3, 28,
		15, 6, 21, 10, 23, 19, 12, 4,
		26, 8, 16, 7, 27, 20, 13, 2,
		41, 52, 31, 37, 47, 55, 30, 40,
		51, 45, 33, 48, 44, 49, 39, 56,
		34, 53, 46, 42, 50, 36, 29, 32
	]

	key_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

	rounds = 16

	permuted_key = ''
	for i in range(56):
		permuted_key += key[pc1[i]-1]
	key = permuted_key

	keys = []

	for i in range(rounds):

		left_half = left_shift(key[:28], key_schedule[i])
		right_half = left_shift(key[28:], key_schedule[i])

		next_key = left_half + right_half

		key = next_key

		permuted_key = ''
		for i in range(48):
			permuted_key += key[pc2[i]-1]

		keys.append(permuted_key)

	return keys



