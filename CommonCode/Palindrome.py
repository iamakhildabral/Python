######### This is a Plaindrome Program in Python ##########

def Palindrome(word):
       return word == word[::-1]







if __name__ == "__main__":
       Palin = input("Enter the String to check whether Plaindrome or Not:")
       if Palindrome(Palin) :
              print("Yes this is a Palindrome String:")
       else:
              print("No this is not a Palindrome:")

