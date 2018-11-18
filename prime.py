#!/usr/local/bin/python3.6

import math
import functools

def is_prime(value: 'int') -> 'bool':
	if (value < 0):
		value = -value
	if (value == 1):
		return False
	i = 2
	while i <= math.sqrt(value):
		if (value % i == 0):
			return False
		i += 1
	return True

@functools.lru_cache()
def is_prime_cached(value: 'int') -> 'bool':
	if (value < 0):
		value = -value
	if (value == 1):
		return False
	i = 2
	while i <= math.sqrt(value):
		if (value % i == 0):
			return False
		i += 1
	return True

for n in range(1, 300):
	if (is_prime_cached(n)):
		print(n)
