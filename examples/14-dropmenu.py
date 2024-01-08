#!/usr/bin/python3
from tkinter import *
#from PIL import Image, ImageTK

root = Tk()
root.title('Dropdown Menu')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()

clicked = StringVar()
clicked.set("Monday")
drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednessday", command=show)
drop.pack()

#myButton = Button(root, text="show selection", command=show)
#Button.pack()
root.mainloop()
