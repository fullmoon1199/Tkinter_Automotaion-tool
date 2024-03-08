import tkinter as tk
import re

def get_color_from_escape_sequence(text):
    # ANSI 이스케이프 시퀀스에서 색상 코드를 추출합니다.
    color_codes = re.findall(r'\x1b\[0;(\d+)m', text)
    print(color_codes)
    for code in color_codes:
        # 색상 코드에 따라 색상을 반환합니다.
        if code == '30':
            return 'black'
        elif code == '31':
            return 'red'
        elif code == '32':
            return 'green'
        elif code == '33':
            return 'yellow'
        elif code == '34':
            return 'blue'
        elif code == '39':
            return 'default'
    # 색상 코드가 없으면 기본값을 반환합니다.
    return 'default'


def print_color():
    color = get_color_from_escape_sequence(test_string)
    print("Color:", color)  # 색상을 출력합니다.
    return color

# 테스트용 바이트 문자열
test_string = "b'[\x1b[0;31m  OK  \x1b[0m] Reached target \x1b[0;1;39mLocal File Systems\x1b[0m.'"

# 함수를 호출하여 색상을 얻습니다.
color = get_color_from_escape_sequence(test_string)
print("Color:", color)  # 색상을 출력합니다.

def process_and_display(text):
    matches = re.finditer(r'\x1b\[[0-9;]*m(.*?)\x1b\[[0-9;]*m', text)

    color1 = print_color()

    txt.tag_config("color_change", foreground=f"{color1}")
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
    colored_text = "b'[\x1b[0;32m  OK  \x1b[0m] Created\x1b[0m] slice \x1b[0;1;39mUser and Session Slice\x1b[0m.'b'[\x1b[0;32m  OK  \x1b[0m] Created\x1b[0m] slice \x1b[0;1;39mUser and Session Slice\x1b[0mqweqeqwewqe.'"

    txt.tag_config("color_change", foreground="red")
    process_and_display(colored_text)



if __name__ == "__main__":
    root = tk.Tk()

    txt = tk.Text(root)
    txt.pack()

    color = tk.Button(root, text="Change color", command=change_color)
    color.pack()
    color2= tk.Button(root, text="print color", command=print_color)
    color2.pack()

    root.mainloop()



