logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

import os

#Addition
def add(n1,n2):
    return n1+n2

#Subraction
def subtract(n1,n2):
    return n1-n2

#Multiplication
def multiply(n1,n2):
    return n1*n2

#Division
def divide(n1,n2):
    return n1/n2

def calculator():
    print(logo)
    num1 = float(input("Enter first number: "))
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    #For printing all operators
    for operator in operations:
        print(operator)

    #Condition for performing calculation
    calculation_continue = True

    while calculation_continue :
        operator_chosen = input("Pick an operation: ")
        num2 = float(input("Enter next number: "))

        calculation_function = operations[operator_chosen]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operator_chosen} {num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") #for continuing the calculation
        num1 = answer
            
        if choice == 'n':
            calculation_continue = False
            os.system('clear')
            calculator()
            
calculator()
