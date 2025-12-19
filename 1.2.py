###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

#letter read from the keyboard
letter = input('Letter: ')
print(letter)

#number representing the string "20303"
string = str('20303')
print(string, int(string))

#binary string representing decimal number 304
dec = 304
x = bin(dec)
print(str(x))

#hexadecimal string representing decimal number 304
y = hex(dec)
print(str(y))

#integer representing the Unicode code of the € sign
print(ord('€'))

#absolute value of -17
print(abs(-17))