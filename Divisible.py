"""
Problem 6:

For a given number, find all the numbers smaller than the number.
Numbers should be divisible by 3 and also by 5.

Hints:
So, you have to check two conditions: make sure the number is divisible by 3, and also by 5.
Hence, you will need to use two conditions.

"""


def divisible(num):
    result = []
    for i in range(num):
        if i % 5 == 0 and i % 3 == 0:
            result.append(i)
    return result


num = int(input('Inter a number: '))
result = divisible(num)
print('Result is: ', result)
