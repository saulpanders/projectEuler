# @saulpanders
# ex_19
#
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#note: years only have 52 or 53 sundays

'''
You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

'''

# note: gonna do this modular arithmetic style, so
# mon = 1
# tues = 2
# wed = 3
# thurs = 4
# fri = 5
# sat = 6
# sun = 0/7
# then partition each year by 7s



def main():

	first_sunday_count = 0
	dayoffset = 2 #starting with a tuesday in 1901
	days = []
	for i in range(1901,2001):
		daycount = 365

		leap = False
		if i%4 == 0:
			daycount += 1
		if (i%100 == 0) and (i%400 != 0):
			daycount -=1 

		days  = [0]*daycount
			

		for x in range(len(days)):
				days[x] = (x+ dayoffset) % 7

		if daycount%2 == 0:
			leap = True

		#partition by month days to check date (will be -1 when comparing cause array indicies)
		for j in range(len(days)):
			# if its a sunday
			if days[j] == 0:
				if leap:
					if j in [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]:
						first_sunday_count +=1
				else:
					if j in  [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]:
						first_sunday_count+=1

		dayoffset = days[-1] +1
				
			
	print(first_sunday_count)



	

if __name__ == "__main__":
    main()