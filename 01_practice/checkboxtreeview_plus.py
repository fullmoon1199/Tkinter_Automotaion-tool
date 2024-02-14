import tkinter as tk
from tkinter import ttk

class CustomCheckboxTreeview(ttk.Treeview):
    def __init__(self, master=None, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        self.bind('<ButtonPress-1>', self._draw_lines)

    def _draw_lines(self, event):
        self.delete('lines')
        for item_id in self.get_children():
            self._draw_child_lines(item_id)

    def _draw_child_lines(self, item_id):
        node_bbox = self.bbox(item_id)
        if node_bbox:
            x0 = node_bbox[0]
            y0 = node_bbox[1]
            x1 = node_bbox[2]
            y1 = node_bbox[3]

            self.create_line(x0, y0, x1, y0, tags='lines')
            self.create_line(x0, (y0 + y1) // 2, x1, (y0 + y1) // 2, tags='lines')
            
            for child_id in self.get_children(item_id):
                self._draw_child_lines(child_id)

if __name__ == "__main__":
    root = tk.Tk()
    
    tree = CustomCheckboxTreeview(root)
    tree.pack(fill='both', expand=True)
    
    tree.insert("", "end", "1", text="Parent")
    tree.insert("1", "end", "2", text="Child")
    tree.insert("2", "end", "3", text="Grandchild")

    root.mainloop()
