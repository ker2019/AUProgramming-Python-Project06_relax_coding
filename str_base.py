#!/usr/local/bin/python3.6

class DigitError(Exception):
	pass
	
#Return digit (or latter) by number
def digit(num: 'int') -> 'char':
	if (num < 0):
		raise DigitError("Can,t find digit")
	if (num < 10):
		return chr(ord('0') + num)
	if (num <= 36):
		return chr(ord('A') + num - 10)
	raise DigitError("Can,t find digit")

def str_base(value: 'int', base: 'int') -> 'str':
	string = "" 
	if (value < 0):
		value = -value
		string += '-'
	digits = []
	while (value != 0):
		digits.append(digit(value % base))
		value = value // base
	digits.reverse()
	for c in digits:
		string += c
	return string

print(str_base(321, 4))
