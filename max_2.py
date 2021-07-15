"""
Problem 6:
Find the max between two numbers,


"""

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))

if number1 == number2:
    print('Both are same', number1, number2)
else:
    if number1 < number2:
        print('Max one is ', number2)
    print('Max one is', number1)

"""
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
if (num2 >= num1):
    largest = num2
else:
    largest = num1
print("Largest number you entered is: ", largest)
"""

"""
num1 = int(input("First number: "))
num2 = int(input("Second number: "))
largest = max(num1, num2)
print("Largest number you entered is: ", largest)

"""

