user_input = "My name, I dont wanna tell"

d = user_input.split(" ")[::-1]

for each in d:
       f = each.split(",")
       i = len(f)
       for x in f:
              if i>1:
                     print(",")
              print(f)
              i=0


              
