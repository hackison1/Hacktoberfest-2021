# program to check if a string or a number is palindrome or not
s = str(input("Enter a string or number : "))
new_s = s[::-1]
if s==new_s:
    print("Yes")
else:
    print("No")