#!/usr/bin/python3
import tkinter as tk

def get_mouse_position(event):
    x = event.x_root
    y = event.y_root
    print(f"Mouse clicked at X: {x}, Y: {y}")

# Create a Tkinter window
app = tk.Tk()
app.title("Get Mouse Click Position")

# Set the window to be transparent (may vary depending on OS)
app.wm_attributes("-type", "None")
app.wm_attributes("-alpha", 0.5)

# Make the window full-screen
app.attributes('-fullscreen', True)

# Define a frame to capture mouse clicks
frame = tk.Frame(app, bg='white')  # Set background color to white
frame.bind("<Button-1>", get_mouse_position)
frame.pack(fill=tk.BOTH, expand=True)

# Start the main loop
app.mainloop()
