# @saulpanders
# ex_6.py
# 
# Q: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.?
# i.e. difference of (1 + ... + 100)^2 and 1^2+ ... 100^2

# note that by induction, sum of squares == n(n+1)(2n+1)/6
def sum_of_squares(n):
	return (n*(n+1)*(2*n+1)/6)

def main():
	sum_of_range = sum(range(1,101))
	difference = sum_of_squares(100) - (sum_of_range*sum_of_range)
	print(difference)

if __name__ == "__main__":
    main()