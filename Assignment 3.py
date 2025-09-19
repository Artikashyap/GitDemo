

"""
    1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
    2.   Returns the calculated factorial.
    3.   Calls the function with a sample number and prints the output.
"""
"""
def factorial(n):
    if (n < 2):
        return 1
    else:
        return n * factorial(n - 1)
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("the factorial of the num is : ",result)
"""
"""
    1.   Asks the user for a number as input.
    2.   Uses the math module to calculate the:
    o   Square root of the number
    o   Natural logarithm (log base e) of the number
    o   Sine of the number (in radians)
    3.   Displays the calculated results.
"""

num = int(input("Enter a number: "))

from math import *
result = sqrt(num)
print("the square root of num is : ",result)
result = log(num)
print("the natural logarithm of num is : ",result)
result = radians(num)
print("the sine of num is : ",result)



