import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(title="Choose a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_widget.insert(tk.END, content)

# Tkinter 창 생성
root = tk.Tk()
root.title("Text File Viewer")

# Text 위젯 생성
text_widget = tk.Text(root, wrap="word", width=40, height=10)
text_widget.pack(expand=True, fill="both")

# "Open" 버튼 생성
open_button = tk.Button(root, text="Open File", command=open_file)
open_button.pack()

# Tkinter 이벤트 루프 시작
root.mainloop()
