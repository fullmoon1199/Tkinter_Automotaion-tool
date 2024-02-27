import tkinter as tk
import tkinter.ttk as ttk

class ListQueue(object):    
    def __init__(self):
        self.queue_len = 10
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        pass
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None
        
    def printQueue(self):
        print(self.queue)
        
class window:
    def __init__(self, master):
        self.master = master
        self.master.title("Queue")
        self.master.geometry("300x500")
        self.master.resizable(False, False)
        self.master.config(bg="lightgray")

        self.queue = ListQueue()

        self.label = tk.Label(self.master, text="Queue")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)

        self.button = tk.Button(self.master, text="Enter", command=self.enter_button)
        self.button.pack(pady=10)

        self.button = tk.Button(self.master, text="Command List", command=self.commandlist_button)
        self.button.pack(pady=10)

    def enter_button(self):
        if len(self.queue.queue) >= 10:
            self.queue.dequeue()
            item = self.entry.get()
            self.queue.enqueue(item)
            self.entry.delete(0, 'end')
        else:
            item = self.entry.get()
            self.queue.enqueue(item)
            self.entry.delete(0, 'end')

    def commandlist_button(self):
        top = tk.Toplevel(self.master)
        top.title("Queue Contents")
        top.geometry("300x300")
        top.resizable(False, False)
        top.config(bg="lightgray")

        queue_list = self.queue.queue

        listbox = ttk.Treeview(top, columns=("item"), show="headings")
        listbox.heading("item", text="command list")
        listbox.pack(pady=10)

        for item in queue_list:
            words = item.split() 
            listbox.insert("", "end", values=(words,))

        def item_double_clicked(event):
            item = listbox.selection()[0]
            self.entry.delete(0, tk.END) 
            self.entry.insert(0, listbox.item(item, "values")[0])
            top.destroy()


        listbox.bind("<Double-1>", item_double_clicked)

if __name__ == "__main__":
    root = tk.Tk()
    app = window(root)
    root.mainloop()
