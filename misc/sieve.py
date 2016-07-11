"""
Implementation of Sieve of Eratosthenes algorithm to find all prime numbers upto a value K.
"""

from math import sqrt, ceil
import unittest

def generate_primes(n):
	"""Returns a list of prime numbers upto n."""
	if n < 1:
		return None

	bool_array = [False, False] + [True] * n              
	for i in range(2, int(ceil(sqrt(n)))):                
		if bool_array[i]:                                 
			for j in range(i*i,n+1,i):                    
				bool_array[j] = False                     
	primes = [i for i in range(n+1) if bool_array[i]]
	return primes


class MyTest(unittest.TestCase):
	def test_prime(self):
		self.assertEqual(generate_primes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
		self.assertEqual(generate_primes(0), None)
		self.assertEqual(generate_primes(-19), None)
		self.assertEqual(generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
	unittest.main()
