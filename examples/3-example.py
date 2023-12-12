#!/usr/bin/python3
from tkinter import *

root = Tk()

# Creating Label Widget
myButton = Button(root, text="click me!", padx=50, pady=50,  state=DISABLED)
myButton.pack()

root.mainloop()
