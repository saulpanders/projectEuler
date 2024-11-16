# @saulpanders
# ex_015.py
# 
# Q: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner. How many such routes are there through a 20×20 grid?

'''
there is a natural combinatorial connection between lattice paths and rows of pascal's triangle

specifically, if you look at the pathing symbolically (i.e. R = go right, D = go down), we want to count the distinct comibnations of these symbols, provided that #R = #D

see wikipedia for more: https://en.wikipedia.org/wiki/Lattice_path
'''

import math


def calculate_grid_paths(n):
	nth = math.factorial(n)
	two_nth = math.factorial(2*n)
	return two_nth / (nth * nth)




def main():
	p =calculate_grid_paths(20)
	print(p)



if __name__ == "__main__":
    main()