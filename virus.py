from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
root.title("Message Box")
def msg():
    messagebox.showwarning("ALERT!", "STOP, Virus Found")
button = Button(root, text = "Scan For Virus", command = msg)
button.pack()
root.mainloop()