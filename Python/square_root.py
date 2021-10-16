# the square root of n.

def squareRoot(n):

		x = n
		y = 1
		
		c = 0.000001
		while(x - y > c):
	
			x = (x + y)/2
			y = n / x
	
		return x


n = 955

print("Square root of", n, "is",
			round(squareRoot(n), 6))


