import tkinter as tk

def on_key(event):
    # 이벤트 핸들러 함수
    print(f'Key pressed: {event.char}')

root = tk.Tk()

entry = tk.Entry(root, width=30)
entry.pack()

# Entry 위젯에 <Key> 이벤트에 대한 핸들러 함수 등록
entry.bind('<Key>', on_key)

root.mainloop()
