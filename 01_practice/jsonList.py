import tkinter as tk
from tkinter import ttk
import json

# JSON 파일로부터 데이터 읽기
with open("F:\\tkinter\\01_practice\\data.json", encoding="utf-8") as file:
    tree_data = json.load(file)

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("JSON에서 TreeView 만들기")

# Treeview 생성
tree = ttk.Treeview(window)
tree.pack()

# 트리에 아이템 추가하는 재귀적인 함수
def populate_tree(parent, items):
    for item in items:
        if isinstance(item, dict):
            for key, value in item.items():
                item_id = tree.insert(parent, "end", text=key)
                if value:
                    populate_tree(item_id, value)
        elif isinstance(item, list):
            populate_tree(parent, item)
        else:
            item_id = tree.insert(parent, "end", text=str(item))

# 함수 호출을 통해 트리 채우기
populate_tree("", tree_data)

window.mainloop()
