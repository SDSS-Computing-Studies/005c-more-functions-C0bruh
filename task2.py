#!python3
"""
Create a function that determines the largest number in a list of values and returns it.
1 input parameter:
list: the numbers to be checked for the largest value

return: float value of the largest number

Sample assertions:
assert largest([3,10,3]) == 10
"""

def largest(list):
    return max(list)

x = largest([0,10,3,8])
print(x)

y = largest([10,50,100,3000.1])
print(y)

assert largest([3,10,3]) == 10