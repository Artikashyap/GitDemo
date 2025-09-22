'''
1.  Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''
from ctypes import pythonapi
from logging import exception

'''
try:
    file = open("sample.txt", "r")
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
'''
'''
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''


data = input("Enter text to werite to the file: ")

with open("sample.txt", "w") as file:
    file.write(data + "\n")
print("\ndata successfully written to sample.txt.\n")
extra_data = input("Enter additional text to append: ")

with open("sample.txt", "a") as file:
    file.write(extra_data + "\n")
print("\ndata successfully appended.\n")


print("\nFinal content of sample.txt:\n")
with open("sample.txt", "r") as file:
    for line in file:
        print(line, end="")


