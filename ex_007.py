# @saulpanders
# ex_7.py
# 
# Q: What is the 10 001st prime number?

# combine prime number theorem to get limit, then run sieve of erasthese?
import math

# its a little generous (multiply by a constant 2) but hey it works
def prime_upper_bound(n):
	return int(n*math.log(n) + n*math.log(n))

#input is a number n; output is list of primes <=n
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
	upper_bound = prime_upper_bound(10001)
	primes = sieve_of_Eratosthenes(upper_bound)
	
	print(primes[10000])

if __name__ == "__main__":
    main()