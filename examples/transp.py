#!/usr/bin/python3
import tkinter as tk

def record_click(event):
    x, y = event.x, event.y
    print(f"Mouse clicked at X: {x}, Y: {y}")

root = tk.Tk()
root.title("Transparent Click Recorder")

# Main canvas
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Transparent overlay to capture clicks
overlay = tk.Canvas(root, width=400, height=400, bg="", highlightthickness=0)
overlay.pack()

# Bind click events to the overlay
overlay.bind("<Button-1>", record_click)

root.mainloop()
