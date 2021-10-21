
def simple_interest(p,t,r):
	print('The principal is equal to', p)
	print('The time period is equal to', t)
	print('The rate of interest is equal to',r)
	
	si = (p * t * r)/100
	
	print('The Simple Interest is equal to', si)
	return si
	
simple_interest(8, 6, 8)
