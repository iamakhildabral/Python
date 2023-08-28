########## Here we are implemention a correct input taking program#######

while True:
         try:
                number = int(input("Enter your roll number :"))
                print("the roll number entered by you is:",number)
                break;
         except(ValueError,TypeError):
                               print("Invalid Input, try again")
