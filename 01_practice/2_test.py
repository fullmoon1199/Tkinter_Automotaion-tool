import tkinter as tk
from tkinter import ttk

def on_right_click(event):
    # 컨텍스트 메뉴를 표시
    context_menu.post(event.x_root, event.y_root)

def paste_from_clipboard():
    # 클립보드에서 내용 읽기
    clipboard_content = root.clipboard_get()
    
    # 읽은 내용을 엔트리에 삽입
    input_entry.insert(tk.END, clipboard_content)

root = tk.Tk()

textframe2 = ttk.Frame(root)
textframe2.pack()

# 엔트리 위젯 생성
input_entry = ttk.Entry(textframe2, font=('Courier', 12), width=100)
input_entry.pack(pady=10)

# 엔트리 위젯에 우클릭 이벤트에 대한 핸들러 추가
input_entry.bind("<Button-3>", on_right_click)

# 컨텍스트 메뉴 생성
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="붙여넣기", command=paste_from_clipboard)

root.mainloop()
