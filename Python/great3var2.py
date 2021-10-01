def greatest():
    num1 = input('num1: ')
    num2 = input('num2: ')
    if num1 > num2:
        num2 = input("num3: ")
        if num1 > num2:
            print(num1)
        else:
            print(num2)

    else:
        num1 = input("num3: ")
        if num2 > num1:
            print(num2)
        else:
            print(num1)
if __name__ == '__main__':
    greatest()


    