import tkinter as tk
import re

root = tk.Tk()

txt = tk.Text(root)
txt.pack()

def change_color():
    # 텍스트 상에서 정규 표현식을 사용하여 "[ ]" 사이의 텍스트를 찾습니다.
    content = txt.get("1.0", tk.END)
    matches = re.finditer(r'\[(.*?)\]', content)
    for match in matches:
        start_index = match.start()
        end_index = match.end()
        # "[ ]" 사이의 텍스트를 찾았으면 해당 부분에 태그를 추가합니다.
        txt.tag_add("highlight", f"1.0+{start_index}c", f"1.0+{end_index}c")
    
    # 태그된 부분의 색상을 변경합니다.
    txt.tag_config("highlight", background='white', foreground='red')
    print(content)

color = tk.Button(root, text="Change color", command=change_color)
color.pack()

root.mainloop()
