# Q: Find the sum of the digits in the number 100!
# A: Use recursion + function call stack to lazily calculate n!

	
from timeit import *
from mpmath import sqrt,power

def find_factorial(n):
	if n == 0 or n ==1 :
		return 1
	else:
		return n*find_factorial(n-1)



factorials  = [0]*1000

def find_factorial_dynamic(n):
	if n == 0 or n ==1 :
		return 1
	else:
		if factorials[n] != 0:
			return factorials[n]
		else:
			factorials[n] = (n * find_factorial(n-1))
			return factorials[n]



# ex_025.py
# Q: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def fibonacci(n, index, digit_count):
	if n== 0 or n==1:
		return 1
	else:
		return fibonacci(n-1, index,digit_count) + fibonacci(n-2, index, digit_count)

index = 0
digit_count = 0

def count_fib(n, index, digit_count):
	digit_count = len(str((n-1)))
	if (n== 0) or (n==1):
		return 1
	else:
		return fibonacci(n-1, index, digit_count) + fibonacci(n-2, index, digit_count)
	while digit_count < n:
		fib_number = fibonacci(index,index,digit_count)
		digit_count = count_digits(fib_number)
		index +=1
	return index


def count_digits(n):
	return len(str(n))

#off by 1 error depending on if you start the sequence at f0 or f1
#dynamic programming using tabulation to calculate fib w/o recursion
def find_fibonacci_digit(n):
	Fibonacci_numbers = [0,1,1]
	digit_count = 0
	i = 3
	while digit_count < n:
		next_term = Fibonacci_numbers[i-1] + Fibonacci_numbers[i-2]
		digit_count = count_digits(next_term)
		Fibonacci_numbers.append(next_term)
		i+=1
	return i


def find_fibonacci_exact(n):
	phi = (1+sqrt(5))/2
	phi_inv = (1-sqrt(5))/2

	dc= 0
	i = 100
	while dc< n:
			fn = int((power(phi,i) - power(phi_inv,i))/sqrt(5))
			dc = count_digits(fn)
			i+=1
	return i


if __name__ == '__main__':
	import timeit

	mysetup = '''from __main__ import find_fibonacci_exact 
from mpmath import sqrt,power'''

	#print(timeit.timeit("find_factorial(100)", setup="from __main__ import find_factorial", number=10000))
	#print(timeit.timeit("find_factorial_dynamic(100)", setup="from __main__ import find_factorial_dynamic", number=10000))
	print(timeit.timeit("find_fibonacci_digit(100)", setup="from __main__ import find_fibonacci_digit", number=1000))


	print(timeit.timeit("find_fibonacci_exact(100)", setup=mysetup, number=1000))


