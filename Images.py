from tkinter import *
from PIL import Image, ImageTk
window = Tk()
window.geometry("1000x1000")
window.title("Ball")
upload = Image.open("Scenery.jpg")
image = ImageTk.PhotoImage(upload)
label = Label(window,image = image, height = 1044, width = 1650)
label.place(x=50, y= 0)
label1 = Label(window, text = "This is a football.")
label1.place(x=40, y=360)
window.mainloop()
