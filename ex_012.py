# @saulpanders
# ex_012.py
# 
# Q: What is the value of the first triangle number to have over five hundred divisors?

# Use 1 + 2 .. + n = n(n+1)/2 to get value of triangluar number
# use divisor counting function for final solution

import math

def find_triangular_number(n):
	return (n*(n+1))/2


#counts all factors (not necissarily prime) in input N
def count_divisors(n):
	divisors = 0
	upper_bound = int(math.sqrt(n) + 1)
	for i in range(1, upper_bound):
		if(n % i == 0):
			if n / i == i:
				divisors +=1
			else:
				divisors +=2
	return divisors

def main():
	divisors = 1 
	n= 1
	#guesstimate the answer
	for i in range(100000):
		n = int(find_triangular_number(i))
		divisors = count_divisors(n)
		if (divisors >= 500):
			print(n)
	


if __name__ == "__main__":
    main()