####### Insertion Sort #############


size = int(input("Enter the size of the array:"))

array = list()

for i in range(size):
       array.append(int(input("Enter the element")))


print(array)

### Insertion code start from here

for i in range(1,size):
       for j in range(i,size):
              if array[j] < array[j-1]:
                     temp = array[j-1]
                     array[j-1] = array[j]
                     array[j] = temp


print("the array after sorting is:")

print(array)


