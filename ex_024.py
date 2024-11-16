# @saulpanders
# ex_24
#If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
#The lexicographic permutations of 0, 1 and 2 are:

#012   021   102   120   201   210

#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import math
from itertools import permutations

#dict of key/val, where key - permutation && val = T/F
perm_report = {}

def is_alpha_order(perm):
	for i in range(len(perm)-1):
		if (str(perm[i]) < str(perm[i+1])):
			return True
		else:
			return False

def is_numerical_order(perm):
	for i in range(len(perm)-1):
		if (perm[i] < perm[i+1]):
			return True
		else:
			continue

def main():
	perm = permutations([0,1,2,3,4,5,6,7,8,9])
	#perm = permutations([0,1,2])
	perm_report = {k:True for k in permutations([0,1,2,3,4,5,6,7,8,9])}

	for x in perm_report:
		
		if(is_alpha_order(x)):
			perm_report[x]= is_alpha_order(x)
		
		if(is_numerical_order(x)):
			perm_report[x] = is_numerical_order(x)

	i = 0
	for perm in perm_report:
		if(perm_report[perm] == True):
			i+=1
		if i == 1000000:
			print(perm)


	

if __name__ == "__main__":
    main()