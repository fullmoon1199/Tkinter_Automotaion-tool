import tkinter as tk
from tkinter import filedialog

def save_text():
    text = text_entry.get("1.0", "end-1c")  # 텍스트 입력란에서 텍스트 가져오기

    file_path = filedialog.asksaveasfilename(defaultextension=".txt")  # 저장할 파일 경로 선택

    if file_path:
        with open(file_path, "w") as file:
            file.write(text)  # 텍스트 파일에 텍스트 저장
            print("텍스트가 성공적으로 저장되었습니다.")

# tkinter 윈도우 생성
window = tk.Tk()

# 텍스트 입력 위젯 생성
text_entry = tk.Text(window)
text_entry.pack()

# 저장 버튼 생성
save_button = tk.Button(window, text="저장", command=save_text)
save_button.pack()

# tkinter 이벤트 루프 시작
window.mainloop()