#!/usr/bin/python3
from tkinter import *
#from PIL import Image, ImageTK

root = Tk()
root.title('Dropdown Menu')
root.geometry("400x400")



def show():
    myLabel = Label(root, text=clicked.get())
    myLabel.pack()


options = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
        ]

clicked = StringVar()
clicked.set("Select Options")
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Enter", command=show)
myButton.pack()

root.mainloop()
