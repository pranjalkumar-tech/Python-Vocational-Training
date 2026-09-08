# Pack

import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Hello")
label.pack()  # Places the widget in the window

button = tk.Button(window, text="Click")
button.pack()

window.mainloop()