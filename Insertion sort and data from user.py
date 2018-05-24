###########          Insertion Sort              #########

"""
Here I'll first take inputs from Users in the array and then I'll put them
for sorting
"""

array = []
size = int(input("\nEnter the size of array that you want to sort:"))
for i in range(size):
       array.insert(i,(int(input("Enter the Element:"))))

print("Array entered by you is :",array,"\n")
j = 0
for i in range(1,size,1):
       for j in range((i),(j>=0),-1):
              if array[j-1] > array[j]:
                     temp = array[j-1]
                     array[j-1] = array[j]
                     array[j] = temp


print("The array after Insertion sorting is:")
for i in range(size):
       print(array[i])
       
