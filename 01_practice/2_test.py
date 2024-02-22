import tkinter as tk

def change_text_color(event):
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]  # 색상 리스트
    line_num = int(event.widget.index("insert").split(".")[0])  # 현재 라인 인덱스
    current_color = colors[line_num % len(colors)]  # 현재 라인 인덱스에 따른 색상 선택
    text.tag_config(f"line_color_{line_num}", foreground=current_color)  # 해당 라인 태그 설정
    text.tag_add(f"line_color_{line_num}", f"{line_num}.0", f"{line_num}.end")  # 태그 적용 범위 설정

root = tk.Tk()

text = tk.Text(root)
text.pack()

text.bind("<Return>", change_text_color)  # 줄바꿈 이벤트에 색상 변경 함수 연결

root.mainloop()
