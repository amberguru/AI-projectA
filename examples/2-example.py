#!/usr/bin/python3
from tkinter import *

root = Tk()

# Creating Label Widget
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="Project Alx")

# Shoving it onto the screen
myLabel1.grid(row=0, column= 0)
myLabel2.grid(row=1, column= 0)

root.mainloop()
