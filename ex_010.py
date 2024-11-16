# @saulpanders
# ex_010.py
# 
# Q: Find the sum of all the primes below two million.

import math

#input is a number n; output is list of primes <=n (r) (reused from ex 7)
def sieve_of_Eratosthenes(n):
	#initialize array of size n for 1 (true)
	prime_table = [1] * (n)

	#0 and 1 are not prime
	prime_table[0] = 0
	prime_table[1] = 0
 
	primes = []
	upper_bound = int(math.sqrt(n))
	for i in range(2, upper_bound+1):
		if prime_table[i] == 1:
			for j in range(i*i,n,i):
				prime_table[j] = 0 
		
	#theres gotta be a faster way but ehh
	for i in range(len(prime_table)):
		if prime_table[i] == 1:
			primes.append(i)

	return primes

	


def main():
	primes = sieve_of_Eratosthenes(2000000)
	print(sum(primes))

if __name__ == "__main__":
    main()