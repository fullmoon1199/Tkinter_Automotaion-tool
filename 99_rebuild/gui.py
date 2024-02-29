import tkinter as tk

class Window_Title:
    def __init__(self, win, title):
        self.win = win
        self.win.title(title)
        self.win.geometry("1650x900+30+30")

        self.label = tk.Label(self.win, text="Queue")
        self.label.pack(pady=10)

win = tk.Tk()
Window_Title(win, "Queue")
win.mainloop()


