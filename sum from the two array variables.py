a = [1,2,3,4,5]

b = [2,3,6,8]
i =j = 0
user_no = int(input("Enter the number whose sum result you want to check:"))
while i <= len(a) and j <= len(b):
       if a[i] + b[j] == user_no:
              print("These two numbers from the first and second array respectively\
are going to sum into entered user number ",a[i]," ",b[j])
              exit(1)
       else:
              i+= 1
              j+= 1

