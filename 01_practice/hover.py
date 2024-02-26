# import tkinter as tk

# def on_enter(event):
#     global enter_timer_id
#     enter_timer_id = root.after(500, create_description_window)

# def create_description_window():
#     global description_window
#     description_window = tk.Toplevel(root)
#     description_window.geometry('150x50+300+300')
#     description_label = tk.Label(description_window, text="This is a button")
#     description_label.pack()

# def on_leave(event):
#     if enter_timer_id:
#         root.after_cancel(enter_timer_id)
#     if description_window:
#         description_window.destroy()

# def hi():
#     print('hi')

# root = tk.Tk()
# root.title("Mouse Hover Example")

# button1 = tk.Button(root, command=hi, text="Hover me!")
# button1.pack(pady=20)

# description_window = None  # Global variable declaration
# enter_timer_id = None  # Global variable declaration

# # Event binding for when the mouse enters and leaves the button
# button1.bind("<Enter>", on_enter)
# button1.bind("<Leave>", on_leave)

# root.mainloop()
import tkinter as tk

def on_enter(event):
    # Schedule the creation of the description window after 1 second
    root.after(500, create_description_window)

def create_description_window():
    # Create a small window
    description_window = tk.Toplevel(root)
    description_window.geometry('150x50+500+500')
    description_label = tk.Label(description_window, text="This is a button")
    description_label.pack()

def on_leave(event):
    # Close the small window when the mouse leaves the button
    for widget in root.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()

root = tk.Tk()
root.title("Mouse Hover Example")

button1 = tk.Button(root, text="Hover me!")
button1.pack(pady=20)

# Event binding for when the mouse enters and leaves the button
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

root.mainloop()
