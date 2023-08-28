size = int(input("Enter the size :"))
user_list = []
for i in range(size):
    user_list.append(int(input()))

max_occurence = max(user_list, key=user_list.count)
print("The no occured max is :", max_occurence)
