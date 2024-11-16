# @saulpanders
# ex_020.py
# 
# Q: Find the sum of the digits in the number 100!

#gonna try some dynamic programming here -> save previously calculated factorials in an array so you dont blow up the recursion depth

factorials  = [0]*101

def find_factorial(n):
	if n == 0 or n ==1 :
		return 1
	else:
		if factorials[n] != 0:
			return factorials[n]
		else:
			factorials[n] = (n * find_factorial(n-1))
			return factorials[n]


def main():
	target = find_factorial(100)
	print("factorial: " + str(target))
	print("digit sum: "+ str(sum([int(i) for i in str(target)])))
	


if __name__ == "__main__":
    main()

