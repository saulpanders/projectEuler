# @saulpanders
# ex_017.py
# 
# Q: If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

one_to_nine = [0,3,3,5,4,4,3,5,5,4]
ten_to_nineteen = [3,6,6,8,8,7,7,9,8,8]
twenty_to_ninety = [6,6,5,5,5,7,6,6]

hundred = 7
hundred_and = 10

# hundred = 7
# one thousand = 8 + 3 = 11
# and = 3


def count_letters(n):
	ones_sum = sum(one_to_nine)
	ten_to_nineteen_sum = sum(ten_to_nineteen)
	twenty_to_ninety_sum = 10*sum(twenty_to_ninety) + 8*ones_sum
	tens_sum = ten_to_nineteen_sum + twenty_to_ninety_sum + ones_sum
	hundreds_sum = 100 * ones_sum + 9 * tens_sum + 891 * hundred_and + 9 * hundred
	print(hundreds_sum)
	final_num = hundreds_sum + 11 + tens_sum
	return final_num

def main():
	count = count_letters(99)
	print(count)


if __name__ == "__main__":
    main()