#!/usr/bin/python3
from tkinter import *
#from PIL import Image, ImageTK
import sqlite3

root = Tk()
root.title('Dropdown Menu')
root.geometry("400x400")

# create a database that connect to others
conn = sqlite3.connect('')
# Create a variable for the cursor
c = conn.cursor()

# Create Tables in the database !!! Noter run only once to create the table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")

# Commit Changes
conn.commit()

# Close connection to the database
conn.close

root.mainloop()
