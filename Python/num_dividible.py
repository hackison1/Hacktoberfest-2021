#  returns true if all the digits of n divide the sum of the digits of n

def isDivisible(n):

	t = n


	sum = 0
	while (n):
		digit = n % 10
		sum += digit
		n //= 10

	n = t


	while(n):
		digit = n % 10

		if(sum % digit != 0):
			return False

		n //= 10;

	return True

n = 985
if(isDivisible(n)):
	print("Yes")
else:
	print("No")
