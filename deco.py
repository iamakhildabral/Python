def checker_parent(parent_func) :
       def parent_validator(a):
              print("Checker is running")
              print(10*a)

              if(a > 10) :
                     return parent_func(a)
              else :
                     print("Bakar input")
       
       return parent_validator

def checker_parent2(parent_func) :
       def parent_validator2(a) :
              print(10+a)
              return parent_func(a)
       return parent_validator2

@checker_parent2
def parent(a):
       print("Printing from the parent() function.")
