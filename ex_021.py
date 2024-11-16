# @saulpanders
# ex_021.py
# 
# 
#
#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.




import math

divisor_sum_array = [0]*10001


## crudely calculates sum of divisors of n
def sum_of_divisors(n):
	sum_of_factors = 0
	half = (n//2) + 1
	for i in range(1, half):
		if n % i == 0:
			sum_of_factors +=i
	return sum_of_factors

  
# fill global array with sumofdivisors(i) in spot i
def fill_divisor_array(range_list):
	for i in range(len(divisor_sum_array)):
		divisor_sum_array[i] = sum_of_divisors(i)


# iterate through main array, populate it, and pull out any amicable pairs into sum_array
def main():
	sum_array = []
	fill_divisor_array(divisor_sum_array)

	for i in range(len(divisor_sum_array)):
		compare = divisor_sum_array[i]
		if compare <= len(divisor_sum_array) and divisor_sum_array[divisor_sum_array[i]] == i and divisor_sum_array[i] != i:
			sum_array.append(i)
	
	print(sum(sum_array))



if __name__ == "__main__":
    main()

