#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
import subprocess

from PIL import Image, ImageTk

def on_button_click():
    # Replace 'your_script.py' with the actual path to your Python script
    script_path = '1-overviewpage.py'

    # Execute the Python script using subprocess
    subprocess.run(['python', script_path])

# Create the main application window

root = tk.Tk()
root.title("AI/ML Production Optimizer")

# Load the background image and get window dimensions
img = Image.open("/home/kish/AI-ML-production_optimizer/DCS_images/cover_page.png")
window_width, window_height = root.winfo_screenwidth(), root.winfo_screenheight()
img = img.resize((window_width, window_height))

background_image = ImageTk.PhotoImage(img)

# Create a button and associate it with the on_button_click function
button = tk.Button(root, text="Click me", command= on_button_click)
button.pack(padx=20, pady=20)

# Create a canvas to place the background image
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Display the background image at coordinates (0,0)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

root.mainloop()

