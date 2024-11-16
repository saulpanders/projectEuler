# @saulpanders
# ex_2.py
# 
# Q:By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

n1 = 0
n2 = 1
count = 0

while True:
	new_number = n1 + n2
	n1 = n2
	n2 = new_number
	if(n2 >= 4000000):
		break
	if (n2 % 2 ==0):
		count = count + n2


print(count)