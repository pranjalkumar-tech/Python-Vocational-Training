# Grid

import tkinter as tk

window = tk.Tk()

label1 = tk.Label(window, text="Name")
label1.grid(row=0, column=0)  # Places the label in a grid

entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

label2 = tk.Label(window, text="Age")
label2.grid(row=1, column=0)

entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

window.mainloop()