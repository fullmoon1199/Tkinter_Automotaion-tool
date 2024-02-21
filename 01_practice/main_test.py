import tkinter as tk

class Cont1:
    def __init__(self, window):
        self.frame_1 = tk.Frame(window, relief="solid", bd=6)
        self.frame_1.place(relx=0.0, rely=0.15, relwidth=0.25, relheight=0.85)

class Cont2:
    def __init__(self, window):
        self.frame_2 = tk.Frame(window, relief="solid", bd=6)
        self.frame_2.place(relx=0.25, rely=0.15, relwidth=0.25, relheight=0.85)

class MyApp:
    def __init__(self, window):
        self.window = window
        self.container1 = Cont1(window)
        self.container3 = Cont2(window)
    
    def run(self):
        self.window.mainloop()

    # 예시로 각 컨테이너에 접근할 수 있는 메서드를 추가
    def get_container1(self):
        return self.container1

    def get_container3(self):
        return self.container3

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Example")

    app = MyApp(window)
    app.run()
