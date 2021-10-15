print('##### GUESS THE NUMBER BETWEENS 1 TO 10 #####')


import random
guess=1
number=random.randint(1,10)
guess_number=int(input('Enter the number you have guesssed::'))
game_over=False
while not game_over:
    if number==guess_number:
        
        print(f'you won,You have guessed correcct in {guess} times')
        game_over=True
    else:
     if guess_number>number:
        print('Too high:!')
        guess+=1
        guess_number=int(input('enter again::'))
    if guess_number<number:
        print('to low::!')
        
        guess+=1
        
        guess_number=int(input('enter again::'))