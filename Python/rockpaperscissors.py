# This is a game of rock paper scissors
# I hope you all enjoy it !!! :)

import random

rock = '''    

ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''

PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''

SCISSORS
    _______
---'   ____)____    
          ______)
       __________)
      (____)
---.__(___)

'''

game = [rock, paper, scissors]
user_choice = input("\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
user_choice = int(user_choice)
print("\nYou chose:\n" + game[user_choice])
computer_choice = random.randint(0,2)
print("\nComputer chose:\n" + game[computer_choice])

if (computer_choice==0 and user_choice==0) or (computer_choice==1 and user_choice==1) or (computer_choice==2 and user_choice==2) :
    print("Its a tie")
elif (computer_choice==0 and user_choice==1) or (computer_choice==1 and user_choice==2) or (computer_choice==2 and user_choice==0) :
    print("You won")
else:
    print("You lose")