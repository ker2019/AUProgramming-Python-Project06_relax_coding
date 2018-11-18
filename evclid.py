#!/usr/local/bin/python3.6

def gcd(a: 'int', b: 'int') -> 'int':
	if (a < 0):
		a = -a
	if (b < 0):
		b = -b
	while (a != 0 and b != 0):
		if (a > b):
			a = a % b
		else:
			b = b % a
	if (a == 0):
		return b
	if (b == 0):
		return a

print(gcd(14659*13, -86678*13))
	
		
