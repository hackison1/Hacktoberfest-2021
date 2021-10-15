import random

upper_case='ABCDEFGHIJKLMNOP'
lower_case='abcdefghijklmnopqrstuvwxyz'
number='123456789'
symbols='!@#$%^&*()>":;'

all=" "

upper_letter,lower_letter,num,sym=True,True,True,True
if upper_letter:
    all+=upper_case
if lower_letter:
    all+=lower_case
if num:
    all+=number
if sym:
    all+=symbols

amount=input('How many password you want to generate:')
length=input('How long you want password to be::')
amount=int(amount)
length=int(length)
for i in range(amount):
    password=''.join(random.sample(all,length))
    print(password)