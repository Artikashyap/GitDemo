"""
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.
"""
'''

students = {'Raj': 45 , 'Ram': 86 , 'Shyam' : 98 , 'Kiran' : 99}

name = input("Enter the student's name: ")
if name in students :
    print(f"{name}'s marks is {students[name]}.")
else:
    print("Student not found")
   '''

'''
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''
orignal_list = list(range(1,11))
print("orignal list = ",orignal_list)
extracted_list = orignal_list[ :5]
print("extracted first five elements = ",extracted_list)
reserved_list = extracted_list[ ::-1]
print("reserved list = ",reserved_list)
both = extracted_list + reserved_list
print("Both extracted and reserved list = ",both)