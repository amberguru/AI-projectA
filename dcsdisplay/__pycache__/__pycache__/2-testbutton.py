#!/usr/bin/python3
import tkinter as tk

def show_screen(screen):
    screen.tkraise()

root = tk.Tk()
root.title("Navigation Example")

# Create frames for different screens
frame1 = tk.Frame(root, bg="red", width=400, height=300)
frame2 = tk.Frame(root, bg="blue", width=400, height=300)
frame3 = tk.Frame(root, bg="green", width=400, height=300)

# Pack frames in the root window
for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# Create buttons to navigate between screens
button1 = tk.Button(root, text="Screen 1", command=lambda: show_screen(frame1))
button2 = tk.Button(root, text="Screen 2", command=lambda: show_screen(frame2))
button3 = tk.Button(root, text="Screen 3", command=lambda: show_screen(frame3))

button1.grid(row=1, column=0, pady=10)
button2.grid(row=2, column=0, pady=10)
button3.grid(row=3, column=0, pady=10)

# Show the initial screen
show_screen(frame1)

root.mainloop()

