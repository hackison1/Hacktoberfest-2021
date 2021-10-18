import random
s=random.choice(['R','P','S'])
i=0

y=0
c=0
while i<5:
    a=input("R for rock,P for paper and S for scissors\n")
    if s=='S' and a=='P':
        print("Computer = S")
        c=c+1
        print("Computer-",c)
        print("You-",y)
    elif s=='P' and a=='R':
        print("Computer = P")
        c=c+1
        print("Computer-",c)
        print("You-",y)
    elif s=='R' and a=='S':
        print("Computer = R")
        c=c+1
        print("Computer-",c)
        print("You-",y)
    elif s=='R' and a=='P':
        print("Computer = R")
        y=y+1
        print("Computer-",c)
        print("You-",y)
    elif s=='P' and a=='S':
        print("Computer = P")
        y=y+1
        print("Computer-",c)
        print("You-",y)
    elif s=='S' and a=='R':
        print("Computer = S")
        y=y+1
        print("Computer-",c)
        print("You-",y)
    elif s=='S' and a=='S':
        print("Computer = S")
        print("Same")
        
        print("Computer-",c)
        print("You-",y)
    elif s=='P' and a=='P':
        print("Computer = P")
        print("Same")
        
        print("Computer-",c)
        print("You-",y)
    elif s=='R' and a=='R':
        print("Computer = R")
        print("Same")
        
        print("Computer-",c)
        print("You-",y)
    else:
        pass
    i=i+1
if c>y:
    print("----------Computer won the game------------")
elif c==y:
    print("------------------Draw---------------------")
else:
    print("-------------U won the game----------------")
    
