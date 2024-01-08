#!/usr/bin/python3
import tkinter as tk

def get_mouse_position(event):
    x = event.x_root
    y = event.y_root
    print(f"Mouse clicked at X: {x}, Y: {y}")

# Create a Tkinter window
root = tk.Tk()
root.title("Get Mouse Click Position")

# Set the window to be transparent (may vary depending on OS)
root.attributes("-alpha", 0.5)

# Make the window full-screen
root.attributes('-fullscreen', True)

# Define a frame to capture mouse clicks
frame = tk.Frame(root, bg='white')  # Set background color to white
frame.bind("<Button-1>", get_mouse_position)
frame.pack(fill=tk.BOTH, expand=True)

# Start the main loop
root.mainloop()
