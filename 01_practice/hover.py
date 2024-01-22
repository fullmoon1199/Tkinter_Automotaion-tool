import tkinter as tk

def on_enter(event):
    button1.config(bg='lightblue')
    description_label.config(text="This is a button")

def on_leave(event):
    button1.config(bg='white')
    description_label.config(text="")

def hi():
    print('hi')

root = tk.Tk()
root.title("Mouse Hover Example")

button1 = tk.Button(root,command=hi, text="Hover me!")
button1.pack(pady=20)

description_label = tk.Label(root, text="")
description_label.pack()

# 마우스가 위에 올라왔을 때와 나갔을 때의 이벤트 바인딩
button1.bind("<Enter>", lambda event: root.after(500, on_enter, event))
button1.bind("<Leave>", on_leave)

root.mainloop()
