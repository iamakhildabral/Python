class Student:
       __name = None   ##Private Member Declaration
       __age = None                       
       sex = None    ##Simple Memebre Declaration

       def getinfo(self):
              self.__name = input("Enter the value of name:")
              self.__age = input("Enter the age of student:")

       def show_info(self):
              print("The name of the student is :",self.__name)
              print("The Age of the student is :",self.__age)



S = Student()
S.getinfo()
S.show_info()
S._Student__name = "Akhil Dabral"
print(S._Student__name)
S.sex = "M"
print(S.sex)
