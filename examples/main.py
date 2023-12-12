#!/usr/bin/python3
import tkinter as tk
import pyautogui

def get_mouse_position(event):
    x, y = pyautogui.position()
    print(f"Mouse clicked at X: {x}, Y: {y}")

# Create a Tkinter window
root = tk.Tk()
root.title("Get Mouse Click Position")

# Make the window transparent
root.attributes("-alpha", 0.0)  # Set window transparency (0.0 = fully transparent, 1.0 = fully opaque)

# Make the window full screen
root.attributes('-fullscreen', True)

# Bind mouse click event to get_mouse_position function
root.bind("<Button-1>", get_mouse_position)

# Start the main loop
root.mainloop()

