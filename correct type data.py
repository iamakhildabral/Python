# check user input till we get coreect data:
password = input("Enter an integer value:")
while password:
         if type(password == int):
                  print("You entered correct data")
                  break
         else:
                  print("You have entered value other than integer")
                  password = input("Enter an integer value:")
                  continue
 
