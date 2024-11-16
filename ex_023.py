# @saulpanders
# ex_023.py
# 
'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of would be , which means that

is a perfect number.

A number
is called deficient if the sum of its proper divisors is less than and it is called abundant if this sum exceeds

.

As 12 is the smallest abundant number the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than

28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Q: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''

# fact: all multiples of abundant numbers are abundant!

# fact: all even numbers above 46 can be written as the sum of two abundant numbers, so we can remove them from our list!
# https://oeis.org/wiki/Abundant_numbers

#abundant numbers between 12 and 46: 12, 18, 20, 24, 30, 36, 40, 42

from itertools import combinations, combinations_with_replacement 

def is_abundant(n):
	sum_of_factors = 0
	half = (n//2) + 1
	for i in range(1, half):
		if n % i == 0:
			sum_of_factors +=i
	if sum_of_factors > n:
		return True
	else:
		return False



	

def main():
	#abundant_nums = [12, 18, 20, 24, 30, 36, 40, 42]
	abundant_nums = []
	for i in range(2, 28124):
		if is_abundant(i):
			abundant_nums.append(i)

	combos = list(combinations_with_replacement(abundant_nums, 2))
	abundant_combo_sums = set([ sum(combos[x]) for x in range(len(combos))])
	numberlist = [ i for i in range(1,28124)]

	non_abundant_nums = list(set(numberlist).difference(abundant_combo_sums))

	print(sum(non_abundant_nums))





if __name__ == "__main__":
    main()