#!/usr/bin/python3
from tkinter import *

root = Tk()
root.title('Tkinter Uses')
root.iconbitmap('C:\Users\Miracle Edo Kish\Documents\Online Education\ALX Software Engineer\Alx Short Specializations Content\ALX Specilization\Alx Specialization Project\AI-ML-production_optimizer\icon.ico')

# Creating Label Widget
myLabel = Label(root, text="Hello World!")

# Shoving it onto the screen
myLabel.pack()

root.mainloop()
