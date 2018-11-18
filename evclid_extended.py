#!/usr/local/bin/python3.6

import numpy

def egcd(a: 'int', b: 'int') -> 'int, int':
	p0 = 1
	q0 = 0
	p1 = 0
	q1 = 1
	while (b != 0):
		tmp = p1
		p1 = p0 - p1*(a // b)
		p0 = tmp  

		tmp = q1
		q1 = q0 - q1*(a // b)
		q0 = tmp

		tmp = b
		b = a % b
		a = tmp

	return p0, q0

print(egcd(146, 68))
