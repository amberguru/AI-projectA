#!/usr/bin/python3
import tkinter as tk
from PIL import Image, ImageTk

def change_background(image_path):
    global bg_image
    new_image = tk.PhotoImage(file=image_path)
    canvas.itemconfig(bg_image_id, image=new_image)
    canvas.image = new_image  # Keep a reference to avoid garbage collection

root = tk.Tk()
root.title("Change Background Image")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Load initial background image
bg_image = tk.PhotoImage(file="background1.png")  # Replace with your image file
bg_image_id = canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

# Button to change background image
button1 = tk.Button(root, text="Change Background 1", command=lambda: change_background("/home/kish/AI-ML-production_optimizer/DCS_images/cover_page.png"))
button1.pack()

button2 = tk.Button(root, text="Change Background 2", command=lambda: change_background("/home/kish/AI-ML-production_optimizer/DCS_images/overview_page.png"))
button2.pack()

root.mainloop()
