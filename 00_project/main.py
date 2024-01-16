import tkinter as tk
import socket
import serial
import threading
import queue
from tkinter import ttk
from tkinter import *
from typing import Any
from tkinter import Frame, X, N
from tkinter import Frame, Text, Scrollbar



def on_search_port(): 
    import serial.tools.list_ports
    ports = serial.tools.list_ports.comports()
    available_ports = []
    for p in ports:
        available_ports.append(p.device)
    return available_ports

def on_open(self):
        selected_port = self.combo.get()
        if selected_port:
            try:
                self.serial_port = serial.Serial(selected_port, baudrate=9600, timeout=1)
                print(f"Serial port {selected_port} opened successfully.")
            except Exception as e:
                print(f"Failed to open serial port {selected_port}. Error: {e}") #hi

def on_close():
    # TODO: Close 동작 구현
    pass

def on_start_tc():
    # TODO: Start TC 동작 구현
    pass

def on_stop_tc():
    # TODO: Stop TC 동작 구현
    pass

def on_su():
    # TODO: SU 동작 구현
    pass

def on_root():
    # TODO: Root 동작 구현
    pass

def on_shift_f2():
    # TODO: Shift+F2 동작 구현
    pass

def on_shift_f3():
    # TODO: Shift+F3 동작 구현
    pass

def on_import_json():
    # TODO: Import Json 동작 구현
    pass

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("V920 SADK Verification Program")

# 윈도우 크기 설정
window.geometry("1550x900")

# 상단 텍스트 추가
title_label = tk.Label(window, text="V920 SADK Verification Program", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

class Cont1:
    def __init__(self, window):
        self.buttonframe = Frame(window)
        self.buttonframe.pack(fill=X, anchor=N)

        self.combo = ttk.Combobox(self.buttonframe, values=on_search_port(), state="readonly", style="TCombobox")
        self.combo.pack(padx=10, pady=18, anchor=tk.NW, side=tk.LEFT)

        self.search_port_button = tk.Button(self.buttonframe, text="Search Port", command=on_search_port, width=15, height=3)
        self.search_port_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.open_button = tk.Button(self.buttonframe, text="Open", command=on_open, width=15, height=3)
        self.open_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)
        self.close_button = tk.Button(self.buttonframe, text="Close", command=on_close, width=15, height=3)
        self.close_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.layout = tk.Label(self.buttonframe)
        self.layout.pack(padx=10 ,anchor=tk.NW, side=tk.LEFT)

        self.start_tc_button = tk.Button(self.buttonframe, text="Start TC", command=on_start_tc, width=15, height=3)
        self.start_tc_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.stop_tc_button = tk.Button(self.buttonframe, text="Stop TC", command=on_stop_tc, width=15, height=3)
        self.stop_tc_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.layout = tk.Label(self.buttonframe)
        self.layout.pack(padx=10 ,anchor=tk.NW, side=tk.LEFT)

        self.su_button = tk.Button(self.buttonframe, text="SU", command=on_su, width=15, height=3)
        self.su_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.root_button = tk.Button(self.buttonframe, text="Root", command=on_root, width=15, height=3)
        self.root_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.shift_f2_button = tk.Button(self.buttonframe, text="Shift+F2", command=on_shift_f2, width=15, height=3)
        self.shift_f2_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.shift_f3_button = tk.Button(self.buttonframe, text="Shift+F3", command=on_shift_f3, width=15, height=3)
        self.shift_f3_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.layout = tk.Label(self.buttonframe)
        self.layout.pack(padx=15 ,anchor=tk.NW, side=tk.LEFT)

        self.import_json_button = tk.Button(self.buttonframe, text="Import Json", command=on_import_json, width=15, height=3)
        self.import_json_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)



class Cont2: # 진행바 컨테이너
    def __init__(self, window):
        self.progressframe = Frame(window)
        self.progressframe.pack(fill=X, anchor=N)

        self.progressbar = ttk.Progressbar(self.progressframe, maximum=100, length=1400)
        self.progressbar.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.progress_label = tk.Label(self.progressframe, text="진행률: 0%", font=("Helvetica", 12))
        self.progress_label.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

    def update_progress(self, value):
        self.progressbar['value'] = value
        self.progress_label.config(text=f"진행률: {value}%")

class Cont3: # 리스트 뷰 컨테이너
    def __init__(self,window):
        self.listviewframe=Frame(window)
        self.listviewframe.pack(fill=X, anchor=N)

        self.list_view = tk.Listbox(self.listviewframe, width=40, height=45)  # 크기 조절은 필요에 따라 수정
        self.list_view.pack(padx=5, pady=3, anchor=tk.NW, side=tk.LEFT)

        self.list_view = tk.Listbox(self.listviewframe, width=180, height=45)  # 크기 조절은 필요에 따라 수정
        self.list_view.pack(padx=5, pady=3, anchor=tk.NW, side=tk.LEFT)
        
        
class Checklist:
    def __init__(self, window):
        global arr
        arr = {}

        self.checkboxframe = tk.Frame(window, width=300, bg='white')
        self.checkboxframe.pack(padx=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        self.canvas = tk.Canvas(self.checkboxframe, bg='white', width=300, height=700)
        self.canvas.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        vbar = tk.Scrollbar(self.checkboxframe, orient='vertical', command=self.canvas.yview)
        vbar.pack(side="right", fill='y')
        self.canvas.config(yscrollcommand=vbar.set)

        f = tk.Frame(self.checkboxframe)
        self.canvas.create_window((50, 0), window=f, anchor="n")

        for i in range(1, 51):
            arr[i] = tk.IntVar()
            tk.Checkbutton(f, text=f"Test Case {i}", variable=arr[i]).pack()

        f.update_idletasks()  # f의 크기 업데이트

        self.canvas.config(scrollregion=self.canvas.bbox("all"))

class Textview:
    def __init__(self, window):
        global arr
        arr = {}

        self.largeframe = tk.Frame(window, bg='white')
        self.largeframe.pack(padx=5, pady=5, fill='both', expand=True, anchor=tk.NW, side=tk.LEFT)

        self.textframe = tk.Frame(self.largeframe,height=600, bg='white')
        self.textframe.pack(padx=5, pady=5, fill='x', expand=True, anchor=tk.NW, side=tk.TOP)
        self.textframe.pack_propagate(False) 

        self.textview = tk.Text(self.textframe, bg="silver", state=DISABLED)
        self.textview.pack(padx=5, pady=5, fill='both', anchor=tk.NW, side=tk.LEFT, expand=True)

        self.textview.configure(font=("Courier", 10))

        vbar = tk.Scrollbar(self.textframe, orient='vertical', command=self.textview.yview)
        vbar.pack(side="right", fill='y')

        self.textframe2 = tk.Frame(self.largeframe,height=50, bg='white')
        self.textframe2.pack(padx=5, pady=5, fill='x', expand=True, anchor=tk.NW, side=tk.BOTTOM)

        self.textview2 = tk.Text(self.textframe2,height=30, bg="silver")
        self.textview2.pack(padx=5, pady=5, fill='x', anchor=tk.SW, side=tk.LEFT, expand=True)

        self.textview2.configure(font=("Courier", 10))

        vbar = tk.Scrollbar(self.textframe2, orient='vertical', command=self.textview2.yview)
        vbar.pack(side="right", fill='y')



class Cont4: #캔버스 컨테이너
    def __init__(self,window):

        canvas = tk.Canvas(window,width=2, height= 70, bg="silver")
        canvas.place(x=178,y=40)

        canvas = tk.Canvas(window,width=2, height= 70, bg="silver")
        canvas.place(x=570,y=40)

        canvas = tk.Canvas(window,width=2, height= 70, bg="silver")
        canvas.place(x=845,y=40)

        canvas = tk.Canvas(window,width=2, height= 70, bg="silver")
        canvas.place(x=1375,y=40)

        canvas = tk.Canvas(window,width=2000, height=2, bg="silver")
        canvas.place(x=0,y=40)

        canvas = tk.Canvas(window,width=2000, height=2, bg="silver")
        canvas.place(x=0,y=110)

class space:
    def __init__(self,window):

        self.spaceframe=Frame(window)
        self.spaceframe.pack(fill=X, anchor=N)
        self.label = tk.Label(self.spaceframe)
        self.label.pack(padx=5, anchor=tk.NW, side=tk.LEFT)

container1 = Cont1(window)
container2 = space(window)
container3 = Cont2(window)
container6 = Checklist(window)
container7 = Textview(window)
container5 = Cont4(window)

container3.progressbar['value'] = 80

# 윈도우 실행
window.mainloop()


