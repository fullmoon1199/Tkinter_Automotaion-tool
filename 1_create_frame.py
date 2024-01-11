import tkinter as tk
from tkinter import ttk

def populate_treeview(tree, data):
    for category, category_data in data.items():
        category_id = tree.insert("", "end", text=category)
        for item in category_data["items"]:
            item_id = tree.insert(category_id, "end", text=item["name"])
            for command in item["tc"]["list"]:
                command_id = tree.insert(item_id, "end", text=command["cmd"])
            for criterion in item["tc"]["criterion"]:
                criterion_id = tree.insert(item_id, "end", text=f"Criterion: {criterion['type']} - Result: {criterion['rslt']}")

# JSON 데이터
json_data = {
    "Linux": {
        "items": [
            {
                "id": "0001",
                "name": "TC-INSYS-LIN-0003",
                "tc": {
                    "list": [...],
                    "criterion": [...]
                }
            },
            # ... (이하 생략)
        ]
    },
    "Android": {
        "items": [
            {
                "id": "0001",
                "name": "TC-INSYS-AND-0006",
                "tc": {
                    "list": [...],
                    "criterion": [...]
                }
            },
            # ... (이하 생략)
        ]
    }
}

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("JSON Data Treeview")

# 트리뷰 생성
tree = ttk.Treeview(window)
tree.pack(fill="both", expand=True)

# 트리뷰에 데이터 추가
populate_treeview(tree, json_data)

# 스크롤바 추가
tree_scrollbar = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
tree.configure(yscroll=tree_scrollbar.set)
tree_scrollbar.pack(side="right", fill="y")

# 윈도우 실행
window.mainloop()
