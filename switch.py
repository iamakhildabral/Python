##### Sample Switch Programs ######

def fun1():
       print("Fun1")

def fun2():
       print("Fun2")

def fun3():
       print("Fun3")


tup = [fun1,fun2,fun3]

print("Press 1 for function 1 ,\n and press 2 for function2 and 3 for fun3")
user_number = int(input("enter the choice"))

tup[user_number-1]()

