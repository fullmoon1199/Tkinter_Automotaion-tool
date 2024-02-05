import tkinter as tk
from tkinter import ttk

class ExampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CheckboxTreeview with Context Menu")

        self.tree = ttk.Treeview(root, columns=('Name', 'Value'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Value', text='Value')

        # Insert some sample data
        for i in range(5):
            self.tree.insert('', 'end', iid=i, text=str(i), values=('Item ' + str(i), 'Value ' + str(i)))

        # Attach right-click event to show context menu
        self.tree.bind("<Button-3>", self.show_context_menu)

        # Create context menu
        self.context_menu = tk.Menu(root, tearoff=0)
        self.context_menu.add_command(label="Action 1", command=self.action1)
        self.context_menu.add_command(label="Action 2", command=self.action2)

    def show_context_menu(self, event):
        # Select item under cursor
        item_iid = self.tree.identify_row(event.y)

        if item_iid:
            self.tree.selection_set(item_iid)  # Highlight the item
            # Display the context menu at the cursor's location
            self.context_menu.post(event.x_root, event.y_root)

    def action1(self):
        selected_item = self.tree.selection()[0]
        print(f"Performing Action 1 on item {selected_item}")

    def action2(self):
        selected_item = self.tree.selection()[0]
        print(f"Performing Action 2 on item {selected_item}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExampleApp(root)
    root.mainloop()
