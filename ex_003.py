# @saulpanders
# ex_3.py
# 
# Q: Find the largest prime factor of 600851475143 

# sqrt(600851475143) = 775146
import math

#finds all factors (not necissarily prime) in input N; returns list of factors
def find_factors(n):
	factors = []
	upperbound = math.floor(math.sqrt(n))
	for i in range(2, upperbound):
		if(n % 2 == 0):
			continue
		if(n % i == 0):
			factors.append(i)
	return factors

totalfactors = find_factors(600851475143)

for x in totalfactors:
	print(x)
	print(find_factors(x))