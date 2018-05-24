#################    Armstrong Program ###########################

def find_armstrong(user_number):
       
       after_arm = int(0)
       while user_number > 0:
              temp = int(user_number % 10)
              after_arm = after_arm + (temp ** 3)                                                                                    
              user_number = user_number / 10

       return after_arm


if __name__ == "__main__":
       user_number = int(input("Enter the no to find armstrong or not :"))
       after_arm = find_armstrong(user_number)
       if after_arm == user_number:
              print("It is an Armstrong Number:")
       else:
              print("Not an Armstrong Number:")
input("Press key to continue:")