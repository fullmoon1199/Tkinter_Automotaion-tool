import ttkwidgets as tw
import tkinter as tk 

class CheckboxTreeview(tw.CheckboxTreeview):
    def __init__(self, master=None, **kw):
        tw.CheckboxTreeview.__init__(self, master, **kw)
        # disabled tag to mar disabled items
        self.label=tk.Label(root, text=len(self.get_checked()), width=5, height=2)
        self.label.pack()

    def _box_click(self, event):                                       # 박스를 체크하거나 해제하였을때 체크된 박스 개수 출력
        """Check or uncheck box when clicked."""
        x, y, widget = event.x, event.y, event.widget
        elem = widget.identify("element", x, y)
        if "image" in elem:
            # a box was clicked
            item = self.identify_row(y)
            if self.tag_has("disabled", item):
                return  # do nothing when disabled
            if self.tag_has("unchecked", item) or self.tag_has("tristate", item):
                self._check_ancestor(item)
                self._check_descendant(item)                
                self.label.configure(text=len(self.get_checked()))
            elif self.tag_has("checked"):
                self._uncheck_descendant(item)
                self._uncheck_ancestor(item)
                self.label.configure(text=len(self.get_checked()))

root = tk.Tk()

tree = CheckboxTreeview(root)
tree.pack()

tree.insert("", "end", "LinyxAndroid", text="LinyxAndroid")                                            # 체크박스 추가
tree.insert("LinyxAndroid", "end", "Internal System", text="Internal System")
tree.insert("LinyxAndroid", "end", "Externel Interface",  text="Externel Interface")

tree.insert("Internal System", "end", "LA-0001", text="LA-0001")
tree.insert("Internal System", "end", "LA-0002", text="LA-0002")
tree.insert("Internal System", "end", "LA-0003", text="LA-0003")
tree.insert("Internal System", "end", "LA-0004", text="LA-0004")
tree.insert("Internal System", "end", "LA-0005", text="LA-0005")

tree.insert("Externel Interface", "end", "LA-0006", text="LA-0006")
tree.insert("Externel Interface", "end", "LA-0007", text="LA-0007")
tree.insert("Externel Interface", "end", "LA-0008", text="LA-0008")
tree.insert("Externel Interface", "end", "LA-0009", text="LA-0009")

root.geometry("280x300")
root.resizable(True, True)

root.mainloop()