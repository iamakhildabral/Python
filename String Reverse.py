""" This Programs just reverse every word exist in the line """

string = input("Enter the string to reverse:")

tup1 = string.split()

tup1 = tup1[::-1]

reverse_string = ''

for word in tup1:
       reverse_string = reverse_string + word[::-1] + ' '


print("the line after string reversal is:",reverse_string)
