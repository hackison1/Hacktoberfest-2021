#function to sovle scence problem
def solve(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                print("all three are zero")
            else:
                print("no solution")
        else:
            x=c/b
            print("x=",x)
    else:
        d=b**2-4*a*c
        if d>0:
            x1=(-b+d**0.5)/(2*a)
            x2=(-b-d**0.5)/(2*a)
            print("x1=",x1,"x2=",x2)
        elif d==0:
            x=-b/(2*a)
            print("x=",x)
        else:
            print("no solution")

#main function
def main():
    a=int(input("enter a"))
    b=int(input("enter b"))
    c=int(input("enter c"))
    solve(a,b,c)


if __name__=="__main__":
    main()

def solve(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                print("all three are zero")
            else:
                print("no solution")
        else:
            x=c/b
            print("x=",x)
    else:
        d=b**2-4*a*c
        if d>0:
            x1=(-b+d**0.5)/(2*a)
            x2=(-b-d**0.5)/(2*a)
            print("x1=",x1,"x2=",x2)
        elif d==0:
            x=-b/(2*a)
            print("x=",x)
        else:
            print("no solution")

# chemistry problem
def solve(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                print("all three are zero")
            else:
                print("no solution")
        else:
            x=c/b
            print("x=",x)
    else:
        d=b**2-4*a*c
        if d>0:
            x1=(-b+d**0.5)/(2*a)
            x2=(-b-d**0.5)/(2*a)
            print("x1=",x1,"x2=",x2)
        elif d==0:
            x=-b/(2*a)
            print("x=",x)
        else:
            print("no solution")

#python chemistry problem solver
def h2so4(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                print("all three are zero")
            else:
                print("no solution")
        else:
            x=c/b
            print("x=",x)
    else:
        d=b**2-4*a*c
        if d>0:
            x1=(-b+d**0.5)/(2*a)
            x2=(-b-d**0.5)/(2*a)
            print("x1=",x1,"x2=",x2)
        elif d==0:
            x=-b/(2*a)
            print("x=",x)
        else:
            print("no solution")