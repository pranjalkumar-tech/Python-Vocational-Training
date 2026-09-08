# Getting Entry Value

import tkinter as tk

window = tk.Tk()

entry = tk.Entry(window)  # Creates an input box
entry.pack()

def show_name():  # Creates a function
    name = entry.get()  # Gets the value from the entry
    print(name)

button = tk.Button(window, text="Show Name", command=show_name)  # Creates a button
button.pack()

window.mainloop()