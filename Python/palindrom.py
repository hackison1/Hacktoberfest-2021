print('CODE TO CHECK WHETHER THE WORD IS PALINDROM OR NOT')
print("--------------------------------->>>>>>>>><<<<<<<<<<<<<<<<<<<<----------------------------------------------")
words=input('Enter a word to check if it\'s palindrom:')
new_word=words[::-1]
if new_word==words:
    print('It\'s palindrome')
else:
    print('it\'s not palindrome')