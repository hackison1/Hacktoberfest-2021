#  find the largest number that can be formed from given sum of digits and number of digits.

def findLargest( m, s) :

	if (s == 0) :
	
		if(m == 1) :
			print("Largest number is " , "0",end = "")
		else :
			print("Not possible",end = "")
	
		return

	if (s > 9 * m) :
		print("Not possible",end = "")
		return

	res = [0] * m

	for i in range(0, m) :

		if (s >= 9) :
			res[i] = 9
			s = s - 9

		else :
			res[i] = s
			s = 0
	print( "Largest number is ",end = "")
	
	for i in range(0, m) :
		print(res[i],end = "")

s = 9
m = 3
findLargest(m, s)
