import tkinter as tk
from tkinter import ttk
from ttkwidgets import CheckboxTreeview

def count_checked_items():
    checked_items = tree.selection()
    count = len(checked_items)
    print(f"체크된 항목 개수: {count}")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("CheckboxTreeview 예제")

# CheckboxTreeview 생성
tree = ttk.CheckboxTreeview(root)
tree["columns"] = ("Name", "Value")

# 트리에 열 추가
tree.column("#0", width=0, stretch=tk.NO)
tree.column("Name", anchor=tk.W, width=120)
tree.column("Value", anchor=tk.W, width=80)

# 트리에 헤더 추가
tree.heading("#0", text="", anchor=tk.W)
tree.heading("Name", text="이름", anchor=tk.W)
tree.heading("Value", text="값", anchor=tk.W)

# 트리에 아이템 추가
item1 = tree.insert("", "end", text="항목 1")
item2 = tree.insert("", "end", text="항목 2")
item3 = tree.insert("", "end", text="항목 3")

# 체크박스 활성화
tree.item(item1, values=("값 1"))
tree.item(item2, values=("값 2"))
tree.item(item3, values=("값 3"))

# 버튼 추가하여 체크된 항목 개수 확인
button = tk.Button(root, text="체크된 항목 개수 확인", command=count_checked_items)
button.pack(pady=10)

# 윈도우 실행
root.mainloop()
