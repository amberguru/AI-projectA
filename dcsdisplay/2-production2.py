#!/usr/bin/python3
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("AI/ML Production Optimizer")

# Load the background image and get window dimensions
img = Image.open("/home/kish/AI-ML-production_optimizer/DCS_images/production_page2.png")
window_width, window_height = root.winfo_screenwidth(), root.winfo_screenheight()
img = img.resize((window_width, window_height))

background_image = ImageTk.PhotoImage(img)

# Create a canvas to place the background image
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Display the background image at coordinates (0,0)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

root.mainloop()

