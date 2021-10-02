n=12
print("You have only five chances.\n\t","Play Carefully")
i=1
while i<=5:
	thenum=int(input("Type Your Number of Two Digits Between 10----20\n\n\t"))
	if thenum>12:
		print("!!!please enter smaller number!!!")
	elif thenum<12:
		print("!!!please enter bigger number!!!")
	else:
		print("!!!HURRAY!!!\n","YOU WON")
		print("Your point is :",i)
		break
	print(5-i,"chances left")
	i=i+1
if i>5:
	print("Game over")