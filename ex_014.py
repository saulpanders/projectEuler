# @saulpanders
# ex_014.py
# 
# Q: What is the longest collatz chain under 1 million for starting seed


def next_collatz_term(n):
	if n%2 ==0:
		return n/2
	else:
		return 3*n + 1

#this algorithm has a pretty bad time complexity
def find_longest_chain(start, end):
	max_chain_length=0
	max_chain_index = 0
	for i in range(start, end+1):
		current_chain_length=0
		index = i
		while index > 1:
			index = next_collatz_term(index)
			current_chain_length +=1
		if current_chain_length > max_chain_length:
			max_chain_length = current_chain_length
			max_chain_index = i

	return max_chain_index

def main():
	max_chain_length = find_longest_chain(1,1000000)
	print(max_chain_length)
	


if __name__ == "__main__":
    main()