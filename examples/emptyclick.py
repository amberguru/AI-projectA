#!/usr/bin/python3
import tkinter as tk

def get_mouse_position(event):
    x = event.x
    y = event.y
    print(f"Mouse clicked at X: {x}, Y: {y}")

# Create a Tkinter window
root = tk.Tk()
root.title("Get Mouse Click Position")

# Define a frame to capture mouse clicks
frame = tk.Frame(root, width=300, height=200)
frame.bind("<Button-1>", get_mouse_position)
frame.pack()

# Start the main loop
root.mainloop()
