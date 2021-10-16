
# checks if a digits exists in n which is  the average of all other digits

def check (n):

	digits = set()

	t = n
	Sum = 0
	count = 0
	
	while(t > 0):

		Sum += t % 10

		digits.add(t % 10)

		count += 1
		t = t // 10

	if ((Sum % count == 0) and
		((int)(Sum / count) in digits)):
		print("Yes")
	else:
		print("No")

n = 8646

check(n)
