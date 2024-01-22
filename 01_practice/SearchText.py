import tkinter as tk
from tkinter import simpledialog

class Textview:
    def __init__(self, window):
        self.window = window
        self.window.title("Text Viewer")

        self.textframe = tk.Frame(self.window)
        self.textframe.pack(expand=True, fill='both')

        self.textview = tk.Text(self.textframe, bg="silver")
        self.textview.pack(padx=5, pady=5, fill='both', anchor=tk.NW, side=tk.LEFT, expand=True)

        # Bind Ctrl+F to the search function
        self.textview.bind('<Control-f>', self.search_text)

        # Insert some sample text
        sample_text = "This is a sample text for demonstration purposes. You can search for specific words using Ctrl+F."
        self.textview.insert(tk.END, sample_text)

        # Initialize search dialog variable
        self.search_dialog = None

    def search_text(self, event):
        if not self.search_dialog:
            self.search_dialog = SearchDialog(self.window, self)
        else:
            self.search_dialog.focus_set()

class SearchDialog(tk.Toplevel):
    def __init__(self, parent, textview_instance):
        tk.Toplevel.__init__(self, parent)
        self.title("Search")
        self.textview_instance = textview_instance

        self.search_term = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.search_term)
        entry.pack(padx=10, pady=10)

        search_button = tk.Button(self, text="Search", command=self.search_text)
        search_button.pack(pady=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def search_text(self):
        search_term = self.search_term.get()
        if search_term:
            # Remove previous search tags
            self.textview_instance.textview.tag_remove("search", "1.0", tk.END)

            start = "1.0"
            while True:
                start = self.textview_instance.textview.search(search_term, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(search_term)}c"
                self.textview_instance.textview.tag_add("search", start, end)
                self.textview_instance.textview.tag_config("search", background="yellow")
                start = end

    def on_close(self):
        # Remove search tags when closing the search dialog
        self.textview_instance.textview.tag_remove("search", "1.0", tk.END)
        self.textview_instance.search_dialog = None
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Textview(root)
    root.mainloop()
