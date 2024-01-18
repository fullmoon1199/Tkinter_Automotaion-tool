import unittest
import tkinter as tk
from tkinter import ttk

class TestTreeview(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.tree = ttk.Treeview(self.root, show="tree")
        self.tree.pack()
        self.tree.configure(style="Bold.TCheckbutton")
        self.tree.tag_configure("parent", style="Bold.TCheckbutton")
        self.tree.tag_configure("child", style="TCheckbutton")
        self.tree.bind("<<TreeviewSelect>>", self.on_checkbox_select)
        self.tree.bind("<Button-1>", self.toggle_checkbox)

        self.parent1 = self.tree.insert("", "end", text="Parent 1", values=("Parent 1 Value",), tags=("parent",))
        self.parent2 = self.tree.insert("", "end", text="Parent 2", values=("Parent 2 Value",), tags=("parent",))
        self.child1 = self.tree.insert(self.parent1, "end", text="Child 1", values=("Child 1 Value",), tags=("child",))
        self.child2 = self.tree.insert(self.parent1, "end", text="Child 2", values=("Child 2 Value",), tags=("child",))
        self.child3 = self.tree.insert(self.parent2, "end", text="Child 3", values=("Child 3 Value",), tags=("child",))

    def tearDown(self):
        self.root.destroy()

    def on_checkbox_select(self, event):
        item_id = self.tree.focus()
        item_text = self.tree.item(item_id, "text")
        item_value = self.tree.item(item_id, "values")
        print(f"Selected item: {item_text}, Value: {item_value}")

    def toggle_checkbox(self, event):
        item_id = self.tree.identify_row(event.y)
        current_state = self.tree.item(item_id, "values")
        new_state = not current_state[0]
        self.tree.item(item_id, values=(new_state,))

    def test_checkbox_select(self):
        self.tree.selection_set(self.child1)
        self.on_checkbox_select(None)
        # Add your assertions here

    def test_toggle_checkbox(self):
        self.tree.selection_set(self.child2)
        self.toggle_checkbox(None)
        # Add your assertions here

if __name__ == '__main__':
    unittest.main()