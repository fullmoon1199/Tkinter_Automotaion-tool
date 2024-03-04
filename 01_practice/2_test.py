import tkinter as tk
from tkinter.constants import END, MOVETO
window = tk.Tk()  # Define the window

t = tk.Text(window)
t.pack()
for i in range(100):
    t.insert(END, "{}\n".format(i))
def get_y():
    global y
    y = t.yview()
b = tk.Button(window, text="get y", command=get_y)
b.pack()
b1 = tk.Button(window, text="set y", command=lambda: t.yview(MOVETO, y[0]/y[1]))
b1.pack()

window.mainloop()  # Start the window's main loop