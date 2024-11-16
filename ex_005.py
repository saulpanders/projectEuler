# @saulpanders
# ex_5.py
# 
# Q: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#find least common multiple of X = (x1, x2, ..., xn) -> can do this with repeated application 
#Euclid's algorithm
def gcd(a,b):
	while b != 0:      
		a, b = b, a % b
	return a

#calculate LCM from GCD
def lcm(a,b):
	return (a*b)//gcd(a,b)

#recursive LCM calculation of integer vector X = (x1, .., xn)
def lcm_in_range(numbers):
	if len(numbers) ==2:
		return lcm(numbers[0], numbers[1])
	else:
		current_num = numbers[0]
		args = numbers[1:]
		return lcm(current_num, lcm_in_range(args))

def main():
	numbers = [x for x in range(1,21)]
	print(lcm_in_range(numbers))


if __name__ == "__main__":
    main()