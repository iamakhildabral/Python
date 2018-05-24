user_number = int(input("Enter a number of three digits:"))
array = list()
i= 0
while user_number >= 0:
       array[i] = user_number%10
       user_number = user_number /10
       i+= 1
array.sort(reverse=True)
# Lets do some sorting to get second largest
temp = array[0]
array[0] = array[1]
array[1] = temp
# now we are moving the second largest digits from the array to integer
new =0
for i in range(3):
       new = new*10 + array[i]

print("the second largest number is:"+new)
