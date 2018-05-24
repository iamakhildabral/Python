########### This is a simple string reversal program in python ######

string = "My name is Akhil Dabral"

rev_str = ""         ## This a new string which we will use to print reverse words

no_of_words = len(string.split())            ## This will count total no of words in a string

""" Now Lets create a touple from existing string so that we can access each word differently """

tup = string.split()

for word in tup:
       word = word[::-1]
       rev_str = rev_str + word + " "


print("The string after reversal is \n"+rev_str)
