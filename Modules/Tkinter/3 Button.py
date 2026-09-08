# Button

import tkinter as tk
window = tk.Tk()

def say_hello():  # Creates a function for the button
    print("Hello, World!")

button = tk.Button(window, text="Click Me", command=say_hello)  # Creates a button
button.pack()

window.mainloop()