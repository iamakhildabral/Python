user = int(input("Enter the number of three digits"))
arr = list()
count = 0
while user >= 0:
	arr[count] = user%10
	user = user/10
	count += 1

arr.sort(reverse=True)
temp = arr[0]
arr[0] = arr[1]
arr[1] = temp

new = 0
for i in range(3):
	new = new*10 + arr[i]
	