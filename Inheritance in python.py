########## class Inheritance #######

class Parent:
       Father = "FF"

       def __init__(self):
              self.Father = "Akhil"
              print("Parent Class Constructor:")
       def show_name(self):
              print("This is Parent Class")


class Child(Parent):
       kid = None;

       def __init__(self):
              self.kid = "Chid"
              print("Child class contructor:")

       def show(self):
              print("The value of Parent Class variable is:"+Parent.Father)


c = Child()
c.show()

