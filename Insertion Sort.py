#### Insertion Sort for Python ######

array = [ 22 , 33 , 55 , 3 , 1]

for index in range(1,len(array)):
         #current_value = array[index]
         position = index

         while position > 0 and array[position-1] > array[position]:
                  temp = array[position-1]
                  array[position-1] = array[position]
                  array[position] = temp
                  position = position -1
                  

print("The array after sorting is ")
print(array)
