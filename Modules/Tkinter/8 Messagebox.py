# Messagebox

import tkinter as tk
from tkinter import messagebox  # Imports messagebox

window = tk.Tk()

def show_message():  # Creates a function
    messagebox.showinfo("Message", "Hello, World!")  # Shows a message

button = tk.Button(window, text="Show Message", command=show_message)
button.pack()

window.mainloop()