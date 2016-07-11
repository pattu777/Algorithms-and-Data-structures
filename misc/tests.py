import unittest

from sieve import generate_primes

class MyTest(unittest.TestCase):
	def test_prime(self):
		"""Unit tests for primality checking."""
		self.assertEqual(generate_primes(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
		self.assertEqual(generate_primes(0), None)
		self.assertEqual(generate_primes(-19), None)
		self.assertEqual(generate_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
	unittest.main()
