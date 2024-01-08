#!/usr/bin/python3
import tkinter as tk
from PIL import Image, ImageTk

# Convert the .ico file to .png using PIL
ico_path = '/home/kish/showicon/Icon.ico'
png_path = '/home/kish/showicon/Icon.png'

img = Image.open('/home/kish/showicon/Icon.ico')
#img.save('/home/kish/showicon/Icon.png', 'png')

# Create a Tkinter window and load the .png image
root = tk.Tk()
root.title("Icon")

# Load the .png image using PhotoImage
icon = ImageTk.PhotoImage(file='/home/kish/showicon/Icon.png')

# Create a label to display the icon
label = tk.Label(root, image=icon)
label.pack()

root.mainloop()
