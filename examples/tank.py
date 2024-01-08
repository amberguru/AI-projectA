#!/usr/bin/python3
import tkinter as tk

def fill_tank(fill_percentage):
    root = tk.Tk()
    root.title("Tank Filling")

    canvas = tk.Canvas(root, width=200, height=300, bg="white")
    canvas.pack()

    tank_height = 200  # Height of the tank
    tank_width = 100   # Width of the tank
    tank_x = 50        # X position of the tank
    tank_y = 50        # Y position of the tank

    tank = canvas.create_rectangle(tank_x, tank_y, tank_x + tank_width, tank_y + tank_height, outline="black")

    fill_height = tank_height * fill_percentage / 100
    filled_area = canvas.create_rectangle(tank_x, tank_y + tank_height - fill_height,
                                          tank_x + tank_width, tank_y + tank_height,
                                          outline="", fill="blue")

    root.mainloop()

# Call the function with the desired fill percentage (e.g., 80%)
fill_tank(45)
