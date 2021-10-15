print('CODE TO PRINT RANDOM NUMBER OF LUDO')
import random
decission=input('Do you want to toss the dice Y/N::')
if decission.upper()=="Y":
    game_over=False
if decission.upper()=="N":
    game_over=True
    print('OK !!!!!!!!!!')
while not game_over:
    print(random.randint(1,6))
    break
