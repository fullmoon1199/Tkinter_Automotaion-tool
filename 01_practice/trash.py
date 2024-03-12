import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("복잡한 Tkinter 어플리케이션")

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.entry_var)
        self.entry.pack()

        self.add_button = tk.Button(self, text="추가", command=self.add_item)
        self.add_button.pack()

        self.listbox1 = tk.Listbox(self)
        self.listbox1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.listbox2 = tk.Listbox(self)
        self.listbox2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.move_button = tk.Button(self, text="이동", command=self.move_item)
        self.move_button.pack()

        self.remove_button = tk.Button(self, text="삭제", command=self.remove_item)
        self.remove_button.pack()

    def add_item(self):
        text = self.entry_var.get()
        if text:
            self.listbox1.insert(tk.END, text)
            self.entry_var.set("")

    def remove_item(self):
        selected_indices = self.listbox1.curselection()
        for index in selected_indices[::-1]:
            self.listbox1.delete(index)

    def move_item(self):
        selected_indices = self.listbox1.curselection()
        for index in selected_indices[::-1]:
            text = self.listbox1.get(index)
            self.listbox1.delete(index)
            self.listbox2.insert(tk.END, text)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
