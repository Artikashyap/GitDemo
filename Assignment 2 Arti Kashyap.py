""""
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.
"""

num=int(input("enter a number: "))
if num % 2== 0:
       print(num, "is an even number.")
else:
       print(num, "is an odd number.")
       

"""
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
"""





total = 0

for i in range(1, 51):
    total += i

print("The sum of numbers from 1 to 50 is:", total)

