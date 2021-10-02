def gettime():
	import datetime
	return datetime.datetime.now()
task=int(input("Choose 1 for add and 2 for Show stored data:\n"))
if task==1:
	g=int(input("Choose 1 for Aayush\n 2 for Razol\n 3 for Preyans:"))
	if (g==1):
		p=int(input("Choose 1 for food and 2 for exercise\n"))
		if p==1:
			m=open("aayush_food.txt","a")
			FOOD=input("ENTER YOUR FOOD:")
			m.write(f"[{str(gettime())}]")
			m.write(f"{FOOD}\n")
			print("Sucessfully saved your data ")
		elif p==2:
			m=open("aayush_exercise.txt","a")
			Exercise=input("Enter your exercise:/n")
			m.write(f"[{str(gettimme())}]")
			m.write(f"{Exercise}\n")
			print("Sucessfully saved your data ")
	elif(g==2):
		p=int(input("Choose 1 for food and 2 for exercise:\n"))
		if p==1:
			m=open("Razol_food.txt","a")
			FOOD=input("ENTER YOUR FOOD:")
			m.write(f"[{str(gettime())}]")
			m.write(f"{FOOD}\n")
			print("Sucessfully saved your data ")
		elif p==2:
			m=open("Razol_exercise.txt","a")
			Exercise=input("Enter your exercise:/n")
			m.write(f"[{str(gettimme())}]")
			m.write(f"{Exercise}\n")
			print("Sucessfully saved your data ")
	elif (g==3):
		p=int(input("Choose 1 for food and 2 for exercise:\n"))
		if p==1:
			m=open("Preyans_food.txt","a")
			Exercise=input("Enter your exercise:/n")
			m.write(f"[{str(gettimme())}]")
			m.write(f"{Exercise}\n")
			print("Sucessfully saved your data ")
		elif p==2:
			m=open("Preyans_exercise.txt","a")
			Exercise=input("Enter your exercise:/n")
			m.write(f"[{str(gettimme())}]")
			m.write(f"{Exercise}\n")
			print("Sucessfully saved your data ")
	else:
		print("ERRROR::\t!!!You pressed wrong key!!!")
elif task==2:
	joker=int(input("Press 1 for Aayush\n 2 for Razol \n 3 for Preyans"))
	if joker==1:
		joker1=int(input("1 for food , 2 for exercise"))
		if joker1==1:
			k=open("aayush_food.txt")
			i=k.read()
			print(i)
		elif joker1==2:
			k=open("aayush_exercise.txt")
			i=k.read()
			print(i)
	elif joker==2:
		joker1=int(input("Press 1 for food and 2 for exercise:\n"))
		if joker1==1:
			k=open("Razol_food.txt")
			i=k.read()
			print(i)
		elif joker1==2:
			k=open("Razol_exercise.txt")
			i=k.read()
			print(i)
	elif joker ==3:
		joker1=int(input("Press 1 for food and 2 fpr exercise:\n"))
		if joker1==1:
			k=open("Preyans_food.txt")
			i=k.read()
			print(i)
		elif joker1==2:
			k=open("Preyans_exercise.txt")
			i=k.read()
			print(i)
		else:
			print("You pressed wrong key.Please cooperate according to the commands.\n !!!Thank You!!!")