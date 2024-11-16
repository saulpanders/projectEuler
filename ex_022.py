# @saulpanders
# ex_022.py
# Q: what is the total of all the "name scores" in names.txt?

def get_word_score(word):
	total = 0
	for x in word:
		total += (ord(x) - 64)
	return total


def main():
	with open("names.txt") as f:
		contents = f.read().replace('"','').split(',')

	contents.sort()

	full_name_scores = 0
	counter = 1

	for name in contents:
		word_score = get_word_score(name)
		name_score = counter * word_score
		full_name_scores += name_score
		counter +=1

	print(full_name_scores)


	
if __name__ == "__main__":
    main()
