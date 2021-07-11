"""
PROBLEM 5:
Swap two variables.

To swap two variables: the value of the first variable will become the value of the second variable.
On the other hand, the value of the second variable will become the value of the first variable.

HINTS:
To swap two variables, you can use a temp variable.

"""
# here is the two variable
a = 5
b = 7

print('a, b', a, b)

# here is a temporary variable
temp = a  # temp = 5
a = b  # a = 7
b = temp  # b = 5

print('a, b', a, b)
