class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeinput():
    l=[int(x) for x in input().split(' ')]
    head=None
    tail=None
    for i in l:
        if i==-1:
            break
        new=Node(i)
        if head is None:
            head=new
            tail=new
        else:
            tail.next=new
            tail=new
    return head
def lenll(head):
    c=0
    while head is not None:
        c+=1
        head=head.next
    return c
def lenll(head):
    c=0
    while head is not None:
        c+=1
        head=head.next
    return c
def rll(head,n):
    if n == 0 or head is None : 
        return head 
    curr=head
    fast=head
    c=1
    while c<n and curr.next is not None:
        curr=curr.next
        c+=1
    if curr is None:
        return head
    d=curr
    while curr.next is not None:
        curr=curr.next
    head=d.next
    d.next=None
    curr.next=fast
    return head
def printll(head):
    while head is not None :
        print(head.data, end = " ")
        head = head.next
print("ENTER THE SINGLY LIST :",end=" ")
head=takeinput()
i=int(input("ENTER HOW MUCH YOU WANT TO ROTATE THE LINKED LIST : "))
head=rll(head,i)
print("ROTATED LINKED LIST IS :",end=" ")
printll(head)