#######################                      Password Entry GUI Applicatio                         ########################

from tkinter import *
class Longevity(Frame):
         "This is a Longevity program by Input password"
         def __init__(self,master):
                  super(Longevity,self).__init__(master)
                  self.grid()
                  self.create_widgets()

         def create_widgets(self):
                  "This will create Entry Text, Label and Buttons"
                  #Lable Creation
                  self.Lab = Label(self,text="Enter your password here:")
                  #Now provide orientation in Label by Grid Manager
                  self.Lab.grid(row = 0,column = 0,columnspan = 2,sticky = W)

                  #Label Creation
                  self.pwd = Label(self,text="Password:")
                  self.pwd.grid(row = 1,column = 0,sticky = W)

                  #Entry Widget creation
                  self.pswd_entry = Entry(self)
                  self.pswd_entry.grid(row = 1,column = 1,sticky = W)

                  #Submit button creation
                  self.submit = Button(self,text = "Submit",command = self.reveal)
                  self.submit.grid(row = 2,column = 0,sticky = W)

                  #Text Widget for displaying desired data
                  self.secret_text = Text(self,width = 35 ,height = 5,wrap = WORD)
                  self.secret_text.grid(row = 3,column = 0,columnspan = 3,sticky = W)
                  

         def reveal(self):
                  "Display message if password is correct"
                  contents = self.pswd_entry.get()
                  if contents == "secret":
                           message = "This is correct password and you know what "\
                                     "the secret of longevity is eat good and work good"
                  else:
                           message = "That's not the correct password"

                  self.secret_text.delete(0.0,END)
                  self.secret_text.insert(0.0,message)


# Main Programs begins here:

root = Tk()
root.title("Longevity Program:")
root.geometry("500x500")
root.grid()
app = Longevity(root)
root.mainloop()
