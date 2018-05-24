######### Palindrome through simple coding #########

user_string = input("Enter the string to check whether palindorme or not:")

user_char_string = [a for a in user_string]

rev_str = []

for i in user_char_string:
       rev_str.insert(0,i)

if rev_str == user_char_string:
       print("Yes , it's a Palindrome :")
else:
       print("No, it's not a Palindrome :")
