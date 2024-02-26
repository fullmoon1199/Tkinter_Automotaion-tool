import tkinter as tk

def disable_button():
    button.config(state=tk.DISABLED)

root = tk.Tk()

button = tk.Button(root, text="Click Me", command=disable_button)
button.pack()

root.mainloop()