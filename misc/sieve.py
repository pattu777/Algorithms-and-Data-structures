"""
Implementation of Sieve of Eratosthenes algorithm to find all prime numbers upto a value K.
"""

from math import sqrt, ceil

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
