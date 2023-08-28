###########  Fibonnaci Series  ##############

def fib(n):
       if n == 0:
              return 0
       else:
              if n == 1:
                     return 1
              else:
                     return fib(n-1) + fib(n-2)

if __name__ == "__main__":
       upper_range = int(input("Enter the Upper Limit:"))
       lower_range = int(input("Enter the Lower Range:"))
       print(fib(upper_range))
       
