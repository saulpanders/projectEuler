
# @saulpanders
# ex_025.py
# Q: What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


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

	


def main():
	print("the n for F_n with greater than 1000 digits: ")
	print(find_fibonacci_digit(1000))

if __name__ == "__main__":
    main()