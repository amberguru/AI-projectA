#!/usr/bin/python3
import tkinter as tk

def draw_pipe_valve_tank():
    root = tk.Tk()
    root.title("Pipe, Valve, and Tank")

    canvas = tk.Canvas(root, width=300, height=300, bg="white")
    canvas.pack()

    # Draw a pipe
    canvas.create_rectangle(50, 100, 250, 120, outline="black", fill="gray")

    # Draw a valve
    canvas.create_oval(120, 90, 180, 150, outline="black", fill="gray")
    canvas.create_line(150, 90, 150, 150, fill="black", width=2)

    # Draw a tank
    canvas.create_rectangle(50, 150, 250, 250, outline="black", fill="lightblue")

    root.mainloop()

# Draw pipe, valve, and tank
draw_pipe_valve_tank()

