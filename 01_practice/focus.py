import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

def on_entry_focus_in(event):
    print("focus in")
    def on_up_arrow(event):
        print("hi")

    entry.bind("<Up>", on_up_arrow)

def on_entry_focus_out(event):
    print("focus out")

entry = tk.Entry(root)
entry.pack()
entry2 = tk.Entry(root)
entry2.pack()

entry.bind("<FocusIn>", on_entry_focus_in)
entry.bind("<FocusOut>", on_entry_focus_out)

root.mainloop()
