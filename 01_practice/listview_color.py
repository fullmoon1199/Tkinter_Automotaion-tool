import ttkwidgets as tw
import tkinter as tk
from tkinter import *
from ttkwidgets import CheckboxTreeview

def one_fuction():
    tree.tag_add("LA-0008", "fail")
    tree.tag_add("LA-0009", "pass")

def changebutton():
    tree.tag_add("LA-0001", "pass")
    tree.tag_add("LA-0002", "pass")
class CheckboxTreeview(tw.CheckboxTreeview):
   
    def __init__(self, master=None, **kw):
        tw.CheckboxTreeview.__init__(self, master, **kw)
        # disabled tag to mar disabled items
        self.label=tk.Label(root, text=len(self.get_checked()), width=5, height=2)
        self.label.pack()
        
root = tk.Tk()
tree = CheckboxTreeview(root)
tree.pack()

button_one = Button(root, text="one", command = one_fuction)
button_one.pack()

change_tag = Button(root, text="change", command = changebutton)
change_tag.pack()

tree.insert("", "end", "LinyxAndroid", text="LinyxAndroid")
tree.insert("LinyxAndroid", "end", "Internal System", text="Internal System", )
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
tree.tag_configure("pass", background="light green")
tree.tag_configure("fail", background="pink")

root.geometry("280x330")
root.resizable(True, True)
root.mainloop()