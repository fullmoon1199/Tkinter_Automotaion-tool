import tkinter as tk
from tkinter import simpledialog

class Textview:
    def __init__(self, window):
        # ... (생략) ...

        self.textview = tk.Text(self.textframe, bg="silver", state=tk.DISABLED)
        self.textview.pack(padx=5, pady=5, fill='both', anchor=tk.NW, side=tk.LEFT, expand=True)

        # Bind Ctrl+F to the search function
        self.textview.bind('<Control-f>', self.search_text)

        # ... (생략) ...

    def search_text(self, event):
        search_term = simpledialog.askstring("Search", "Enter text to search")
        if search_term:
            start = "1.0"
            while True:
                start = self.textview.search(search_term, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(search_term)}c"
                self.textview.tag_add("search", start, end)
                self.textview.tag_config("search", background="yellow")
                start = end