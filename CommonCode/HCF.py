num1,num2 = map(int,input("Enter two numbers to find out HCF:").split())

if num1 > num2:
       smaller = num2
       if num1 % smaller == 0:
              print("The HCF of both the numbers is:",smaller)
       else:
              for i in range(2,(smaller//2)+1):
                     if num1% i == 0:
                            print("The HCF is: ",i)
                            break
                            
else:
       smaller = num1
       if num2 % smaller == 0:
              print("The HCF of both the numbers is:",smaller)
       else:
              for i in range(2,(smaller//2)+1):
                     if num2% i == 0:
                            print("The HCF is: ",i)
                            break


