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
# import escape_color
# import tkinter as tk
# import re

# root = tk.Tk()

# txt = tk.Text(root)
# txt.pack()

# def remove_escape_sequences(text):
#     # ANSI 이스케이프 시퀀스를 찾는 정규 표현식
#     escape_pattern = re.compile(r'\x1b\[([0-9;]*m)')
#     # 정규 표현식을 사용하여 이스케이프 시퀀스를 제거한 텍스트를 반환
#     return escape_pattern.sub('', text)

# def change_color():
#     colored_text = "\x1b[0;32mAAAA\x1b[0mAAAA"
#     print_text = remove_escape_sequences(colored_text)
#     txt.insert(tk.END, print_text)

#     content = txt.get("1.0", tk.END)
#     matches = re.finditer(r'\x1b\[[0-9;?]*[A-Za-z](.*?)\x1b', content)
#     for match in matches:
#         start_index = match.start(1)  
#         end_index = match.end(1)      
#         txt.tag_add("highlight", f"1.0+{start_index}c", f"1.0+{end_index}c")
#         txt.tag_config("highlight", foreground="blue")

    
# color = tk.Button(root, text="Change color", command=change_color)
# color.pack()

# root.mainloop()

import tkinter as tk
import re

root = tk.Tk()

txt = tk.Text(root)
txt.pack()

def process_and_display(text):
    matches = re.finditer(r'\x1b\[[0-9;]*m(.*?)\x1b\[[0-9;]*m', text)
    start_index = 0
    for match in matches:
        start, end = match.span()
        text_inside_escape = match.group(1)
        txt.insert(tk.END, text[start_index:start])
        txt.insert(tk.END, text_inside_escape, "color_change")
        start_index = end
    if start_index == 0:
        txt.insert(tk.END, text)
    else:
        txt.insert(tk.END, text[start_index:], "color_change")

def change_color():
    colored_text = "b'ssdf sdfsd sdfs sdf sdf sdf sdfdfsfsdf Starting \x1b[0;1;39mCreate list of st\xe2\x80\xa6odes for the current kernel\x1b[0m...'"

    txt.tag_config("color_change", foreground="red")
    process_and_display(colored_text)
    print(colored_text)

color = tk.Button(root, text="Change color", command=change_color)
color.pack()

root.mainloop() 


