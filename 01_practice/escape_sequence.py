import tkinter as tk

root = tk.Tk()
text_widget = tk.Text(root)
text_widget.pack()

# ANSI 이스케이프 시퀀스를 텍스트 위젯에 추가
text_widget.insert(tk.END, "\033[1;32mThis text is green\033[m")

root.mainloop()
