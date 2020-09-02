vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
str = input('Enter the string:- ')

for i in str:
    if i in vowel:
        print(str+'ay')
    else:
        print(str[1:] + str[0] + 'ay')
    break