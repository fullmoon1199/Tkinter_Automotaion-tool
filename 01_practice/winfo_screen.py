import tkinter as tk

# Tkinter 윈도우 생성
root = tk.Tk()

# 화면 해상도 얻기
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 창 크기 설정 (해상도의 절반으로 설정)
window_width = screen_width // 2
window_height = screen_height // 2
root.geometry(f"{window_width}x{window_height}+{screen_width//4}+{screen_height//4}") # 창을 화면의 가운데로 이동

# 윈도우 루프 시작
root.mainloop()
