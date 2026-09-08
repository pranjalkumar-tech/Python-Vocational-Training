# Label

import tkinter as tk

window = tk.Tk()
window.title("Label")

label = tk.Label(window, text="Hello, World!")  # Creates a label
label.pack()  # Displays the label

window.mainloop()