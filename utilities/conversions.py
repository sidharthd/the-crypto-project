def string_to_bin(string):
	return ''.join('{0:08b}'.format(ord(x), 'b') for x in string)

def bin_to_string(binary):
	return ''.join(chr(int(binary[i:i+8], 2)) for i in xrange(0, len(binary), 8))