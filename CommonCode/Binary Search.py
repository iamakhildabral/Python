"""
This program is a Simple Implementation of Search Operation
"""

array = []
size = int(input("Enter the Size of Array to perform\
 search:"))
for i in range(size):
       array.insert(i,int(input("Enter the Value:")))

user_number = int(input("Enter the number that you want to search:"))

if user_number in array:
       print("Number exist in array at index",array.index(user_number))
else:
       print("Not exist in array:")
