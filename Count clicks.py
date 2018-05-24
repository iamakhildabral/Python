#########    Count No of Clicks on GUI Interface Sample Program    #######

from tkinter import *

class GUI(Frame):
         "This gonna create a Button "
         def __init__(self,master):
                  """Initialising  the frame """
                  super(GUI,self).__init__(master)
                  self.grid()
                  self.button_clicks = 0     # Initialising the count with 0
                  self.create_widget()

         def create_widget(self):
                  " This will create a button along with a text "
                  self.button = Button(self)
                  self.button["text"] = "Click to know my name:"
                  self.button["command"] = self.update_count
                  self.button.grid()

         def update_count(self):
                  "This will update button clicks count with user "
                  #self.button_clicks += 1
                  #self.button["text"] = "No of Clicks: "+str(self.button_clicks)
                  self.button["text"] = "Welcome to Hogwarts \n My name is Lord Voldemort"

root = Tk()
root.title("Counts as you click")
root.geometry("500x700")
root = GUI(root)
root.mainloop()
