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

# description_window = None  # 전역 변수로 선언
# enter_timer_id = None  # 전역 변수로 선언

# # 마우스가 위에 올라왔을 때와 나갔을 때의 이벤트 바인딩
# button1.bind("<Enter>", on_enter)
# button1.bind("<Leave>", on_leave)

# root.mainloop()
import tkinter as tk

def on_enter(event):
    # 1초 후에 작은 창을 생성하도록 스케줄링
    root.after(500, create_description_window)

def create_description_window():
    # 작은 창 생성
    description_window = tk.Toplevel(root)
    description_window.geometry('150x50+500+500')
    description_label = tk.Label(description_window, text="This is a button")
    description_label.pack()

def on_leave(event):
    # 마우스가 버튼에서 벗어날 때 작은 창을 닫음
    for widget in root.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()

root = tk.Tk()
root.title("Mouse Hover Example")

button1 = tk.Button(root, text="Hover me!")
button1.pack(pady=20)

# 마우스가 위에 올라왔을 때와 나갔을 때의 이벤트 바인딩
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)

root.mainloop()
