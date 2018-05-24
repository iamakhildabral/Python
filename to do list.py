from tkinter import *

#class Application(Frame):
root = Tk()
root.title("To Do List")
root.geometry("500x500")
app = Frame(root)
app.grid()
Status = Label(app,text="Status") #Font and Placements of Label needs to be correcctatus.grid()

Description = Label(app,text="Description of Task")
Description.grid()

root.mainloop()
