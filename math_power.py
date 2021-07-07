"""
PROBLEM 2:
Take two numbers from the users. Calculate the result of second number power of the first number.

HINTS:
To power, you will need to use two asterisks symbols (two multiplication symbols).
For example 4 to the power 3 will be

"""

# inputted two numbers...........................

number1 = int(input('First number is: '))
number2 = int(input('Second number is: '))

# formula is ....................................
result = number1 ** number2

# display the result..............................
print('Result is: ', result)