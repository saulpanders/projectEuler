
#TODO: broken/too slow
from collections import Counter

def compare_lists(list1, list2): 
    return Counter(list1) == Counter(list2)

start = 1000
end = 9999

cnt = 0
primes = []

#get list of all 4 digit primes
for i in range(start,end):
	if i>1:
		for j in range(2,i):
			if(i % j==0):
				break
		else:
			#print(i)
			primes.append(i)
			cnt = cnt + 1
				
print("total: "+ str(cnt))
print(primes)









