##################  Function which will find number divisible by 7 and not a mulitple of 5 ###################3
lower_limit = int(input("Enter the Lower Limit:"))
upper_limit = int(input("Enter the Uppper Limit for the Range"))
array = []
start = lower_limit
index = 0
while start <= upper_limit:
	if start % 7 == 0:
		if start % 5 != 0:
				array.insert(index,start)
				index += 1
	start += 1

	
print("The Number divisible by 7 and not a mulitple of 5 are:")
print(array)
