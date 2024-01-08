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

my_img1 = ImageTk.PhotoImage(image.open('/home/kish/showicon/1.png'))
my_img2 = ImageTk.PhotoImage(file='/home/kish/showicon/2.png')
#my_img3 = ImageTk.PhotoImage(file='/home/kish/showicon/3.png')
#my_img4 = ImageTk.PhotoImage(file='/home/kish/showicon/4.png')
#my_img5 = ImageTk.PhotoImage(file='/home/kish/showicon/5.png')


image_list = [my_img1, my_img2] # my_img3, my_img4, my_img5]



# Create a label to display the icon
label = tk.Label(root, image=icon)

my_label = tk.Label(image=my_igm1)
my_label.grid(row=0, column=1, columnspan=3)

label.grid(row=0, column=0)

button_back = Button(root, text="<<")
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_forward = Button(root, text=">>")

button_back.grid(row=1, column=0)
button_back.exit(row=1, column=1)
button_back.forward(row=1, column=2)

root.mainloop()
