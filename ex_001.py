# @saulpanders
# ex_1.py
# 
# Q: Find the sum of all the multiples of 3 or 5 below 1000.

s = 0

for i in range (1, 1000):
	if ((i % 3) == 0 or (i%5) == 0 ):
		s = s + i

print(s)