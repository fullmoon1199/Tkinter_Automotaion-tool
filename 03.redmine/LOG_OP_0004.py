# import tkinter as tk
# import re

# root = tk.Tk()

# txt = tk.Text(root)
# txt.pack()

# def change_color():
#     # 텍스트 상에서 정규 표현식을 사용하여 "[ ]" 사이의 텍스트를 찾습니다.
#     content = txt.get("1.0", tk.END)
#     matches = re.finditer(r'\[(.*?)\]', content)
#     for match in matches:
#         start_index = match.start(1)  # 그룹 1의 시작 인덱스
#         end_index = match.end(1)      # 그룹 1의 끝 인덱스
#         # "[ ]" 사이의 텍스트를 찾았으면 해당 부분에 태그를 추가합니다.
#         txt.tag_add("highlight", f"1.0+{start_index}c", f"1.0+{end_index}c")
    
#     # 태그된 부분의 색상을 변경합니다.
#     txt.tag_config("highlight", background='white', foreground='red')
#     print(content)

# color = tk.Button(root, text="Change color", command=change_color)
# color.pack()

# root.mainloop()
import escape_color
import tkinter as tk
import re

root = tk.Tk()

txt = tk.Text(root)
txt.pack()

def extract_escape_sequence(text):
    # 정규 표현식을 사용하여 이스케이프 시퀀스를 추출합니다.
    escape_sequences = re.findall(r'\x1b\[[0-9;?]*[A-Za-z]', text)
    return escape_sequences

def change_color():
    # 이스케이프 시퀀스를 포함한 텍스트 생성
    colored_text = "b'[\x1b[0;32m  OK  \x1b[0m] Started \x1b[0;1;39mNetwork Name Resolution\x1b[0m.'"
    txt.insert(tk.END, colored_text)

    # 추출한 이스케이프 시퀀스를 출력합니다.
    escape_sequences = extract_escape_sequence(colored_text)
    color = escape_color.colorcode(escape_sequences)

    content = txt.get("1.0", tk.END)
    matches = re.finditer(r'\x1b\[[0-9;?]*[A-Za-z](.*?)\x1b', content)
    for match in matches:
        start_index = match.start(1)  # 그룹 1의 시작 인덱스
        end_index = match.end(1)      # 그룹 1의 끝 인덱스
        # 이스케이프 시퀀스 사이의 텍스트에 태그를 추가합니다.
        txt.tag_add("highlight", f"1.0+{start_index}c", f"1.0+{end_index}c")
    
    # 태그된 부분의 색상을 변경합니다.
    txt.tag_config("highlight", foreground=f"{color}")

color = tk.Button(root, text="Change color", command=change_color)
color.pack()

root.mainloop()
