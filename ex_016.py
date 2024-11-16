# @saulpanders
# ex_012.py
# 
# Q: What is the sum of the digits of the number 2^1000?

import math

#raises x to the power n naively, O(n) time
def power(x,n):
	product = 1
	for i in range(n):
		product = product * x
	return product

# uses insight that you can stack exponentiation to do it faster O(logn)
def fast_power(x,n):
	product = 1
	while n > 0:
		if n % 2 == 0:
			#divide power by 2, multiply base to itself
			n = n/2
			x = x*x
		else:
			#odd case, decrement power and do the multiply manually
			n = n-1
			product = product * x
			n = n /2
			x = x*x
	return product


def main():
	big_num = power(2,1000)
	digits = [int(i) for i in str(big_num)]
	print(sum(digits))
	print(sum([int(i) for i in str(fast_power(2,1000))]))

if __name__ == "__main__":
    main()