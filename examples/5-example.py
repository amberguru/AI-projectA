#!/usr/bin/python3
from tkinter import *

root = Tk()

e = Entry(root, width=80, borderwidth=4)
e.pack()

# Define a function to use the button
def myClick():
    myLabel = Label(root, text="Look! I clicked a Button")
    myLabel.pack()

# The shape and size of the button is defined below. we used the command=myClick to call the function then fg and bg to set the text and background colors. 
myButton = Button(root, text="click me!", padx=50, pady=50, command=myClick, fg="blue", bg="grey")

# Places the button at the top Center position
myButton.pack()

root.mainloop()
