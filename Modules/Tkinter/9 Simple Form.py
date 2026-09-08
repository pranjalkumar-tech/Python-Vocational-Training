# Simple Form

import tkinter as tk

window = tk.Tk()
window.title("Student Form")

tk.Label(window, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

tk.Label(window, text="Age").grid(row=1, column=0)
age_entry = tk.Entry(window)
age_entry.grid(row=1, column=1)

def submit():  # Creates a function
    print("Name:", name_entry.get())
    print("Age:", age_entry.get())

button = tk.Button(window, text="Submit", command=submit)
button.grid(row=2, column=1)

window.mainloop()