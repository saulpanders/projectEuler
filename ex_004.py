# @saulpanders
# ex_4.py
# 
# Q: Find the largest palindrome made from the product of two 3-digit numbers.

#finds all palindromes in the range (using python range rules); input is upper/lower bound, output is list of palindromes


#checks if a number is palindrome and returns True if so, else False; using string compare (slow I know)
def check_palindrome(n):
	reverse = str(n)[::-1]
	return reverse == str(n)



def main():
	# start in descending order, so largest palidrome is first
	max_pal = 0
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			n = i*j
			if check_palindrome(n) and (n> max_pal):
				max_pal = n
	print(max_pal)
				


if __name__ == "__main__":
    main()