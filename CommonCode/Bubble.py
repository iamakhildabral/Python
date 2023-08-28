#############   Bubble Sort Program in Python     ###################


arr = [22,11,55,9,2]

for i in range(1,5):
       for j in range(0,(5-i)):
              if arr[j] > arr[j+1]:
                     temp = arr[j+1]
                     arr[j+1] = arr[j]
                     arr[j] = temp

print("The array after sorting is :")
for i in range(5):
       print("\n",arr[i])
                     
