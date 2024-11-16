# @saulpanders
# ex_009.py
# 
# Q: There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

'''
using algebra identity for a^2 + b^2 = c^2
where
	a = m^2 - n^2
	b = 2mn
	c = m^2 + n^2

and gcd(m,n) = 1
'''

import math

def find_pythagorean_triples(bound):
	#(a,b,c)
	triple = (0,0,0)
	m = 2

	pythag_trips = []

	while triple[2] < bound:
		for n in range(m):
			triple = (m*m - n*n, 2*m*n, m*m + n*n)

			if triple[2] > bound:
				break
			pythag_trips.append(triple)
		m+=1
	return pythag_trips



def main():
	trips = find_pythagorean_triples(1000)
	for x in range(len(trips)):
		if sum(trips[x]) == 1000:
			print(trips[x])
			print(math.prod(trips[x]))


if __name__ == "__main__":
    main()