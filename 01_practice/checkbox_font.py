import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

class YourApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CheckboxTreeview Example")

        # Create CheckboxTreeview
        self.cd_tree = ttk.Treeview(root)
        self.cd_tree.pack()

        # Create checkboxes images
        self.checkboxes = self.make_checkboxes(row_height=20, outc='black', fillc='white', chkc='deepskyblue')

        # Configure tags with checkbox images
        self.cd_tree.tag_configure("unchecked", image=self.checkboxes[0])
        self.cd_tree.tag_configure("tristate", image=self.checkboxes[1])
        self.cd_tree.tag_configure("checked", image=self.checkboxes[2])

        # Insert items with tags
        self.cd_tree.insert("", "end", text="Item 1", tags=("unchecked",))
        self.cd_tree.insert("", "end", text="Item 2", tags=("checked",))
        self.cd_tree.insert("", "end", text="Item 3", tags=("tristate",))

    def make_checkboxes(self, row_height, outc, fillc, chkc):
        print("make_checkboxes")

if __name__ == "__main__":
    root = tk.Tk()
    app = YourApp(root)
    root.mainloop()
