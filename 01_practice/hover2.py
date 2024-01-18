import tkinter as tk

def hover(event):
    # Output "ok" next to the cursor
    root.geometry("100x100")  # Set the size of the window to 100x100
    label.config(text="ok")

root = tk.Tk()

# Create 30 checkbox widgets
checkboxes = []
for _ in range(30):
    checkbox = tk.Checkbutton(root, text="Checkbox")
    checkbox.bind("<Enter>", lambda event: root.after(500, hover, event))
    checkbox.bind("<Leave>", lambda event: label.config(text=""))
    checkboxes.append(checkbox)

# Create a label widget to display the "ok" text
label = tk.Label(root)
label.pack()

# Pack the checkboxes
for checkbox in checkboxes:
    checkbox.pack()

root.mainloop()
