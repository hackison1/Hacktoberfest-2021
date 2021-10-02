//simply program to reverse the digits of any number
a=int(input("enter the number:"))
b=0
c=0
while a!=0:
        b=int(b*10)
        c=int(a%10)
        b=b+c
        a=int(a/10)
        

print(b)        
