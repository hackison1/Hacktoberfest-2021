"""stack operations"""

def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False
def Push(stk,item):
    stk.append(item)
    top=len(stk)-1
def Pop(stk):
    if isEmpty(stk):
        return 'underflow'
    else:
        item=stk.pop()
        if len(stk)==0:
            top= None
        else:
            top=len(stk)-1
        return item
def Peek(stk):
    if isEmpty(stk):
        return 'underflow'
    else:
        top=len(stk)-1
        return stk[top]
def Display(stk):
    if isEmpty(stk):
        print('stack is empty')
    else:
        top=len(stk)-1
        print(stk[top],'<-- top')
        for i in range(top-1,-1,-1):
            print(stk[i])
stack=[1,2,3,4]
top='None'
c='y'
while True:
    print('STACK OPERATIONS')
    print('1.PUSH')
    print('2.POP')
    print('3.PEEK')
    print('4.DISPLAY')
    print('5.EXIT')
    ch=int(input('Enter the choice from 1-5: '))
    if ch==1:
        item=int(input('enter item: '))
        Push(stack,item)
        print('INSERTED',item)
        continue
    elif ch==2:
        item=Pop(stack)
        if item=='underflow':
            print('stack is empty')
        else:
            print(item,'WAS POPPED')
    elif ch==3:
        item=Peek(stack)
        if item=='underflow':
            print('stack is empty')
        else:
            print('ELEMENT AT THE TOP IS',item)
    elif ch==4:
        Display(stack)
    elif ch==5:
        break
    else:
        print('INVALID CHOICE')
