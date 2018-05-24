############ FACTORIAL PROGRAM ###################3
import sys

def factorial(x):
       if x == 0:
              return 1
       sys.stdout.write(str(x))
       if not(x == 1) :
              sys.stdout.write(' x ')
       factorial(x-1)
       return zip

if __name__ == "__main__":
       fact = int(input("Enter the no till where you \
wanna see the factorial value:"))
       print("I said find factorial of "+str(fact)) 
       factorial(fact);
       #print("the value of factorial is :"+str(value))
       
