################################### Prime Number Validation #########################################

user_number = int(input("Enter the number to check whether prime or not :"))
flag = 0
for i in range(2,int(user_number/2),1):
       if( int(user_number % i)== 0) :
              flag = 1
              break   
if flag == 1:
       print("No is not prime:")
else:
       print("No is Prime:")
