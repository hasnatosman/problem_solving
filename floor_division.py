"""
PROBLEM 4:
Find the floor division of two numbers.
HINTS:
Just use two // instead of one.
"""

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

result = num1 // num2
print("Result is: ", result)

"""
Explanation:
When you divide one number by another you get two things. One is called the integer part of the division. 
Another is the remainder.

To get the quotient (result without the remainder), you can use two-division symbols.
"""

"""
import math
result = math.floor(3.4)
print(result)

"""