import tkinter as tk
import serial
from tkinter import ttk
from tkinter import *
from typing import Any
from tkinter import Frame, X, N
from tkinter import simpledialog
from ttkwidgets import CheckboxTreeview
import json




import serial.tools.list_ports

def on_search_port(): 
    ports = serial.tools.list_ports.comports()
    available_ports = []
    for p in ports:
        available_ports.append(p.description)
    return available_ports

def on_open():
    selected_port = container1.combo.get()
    if selected_port:       
        try:
            container1.serial_port = serial.Serial(selected_port, baudrate=115200, timeout=1)
            print(f"Serial port {selected_port} opened successfully.")
        except Exception as e:
            print(f"Failed to open serial port {selected_port}. Error: {e}")

            
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
window.geometry("1550x900+100+50")

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

# Usage example:
  # Update progress to 50%

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

        Checklist_LargeFrame = tk.Frame(window, bg = 'blue')
        Checklist_LargeFrame.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)
        # Create a frame to hold the CheckboxTreeview and scrollbar
        frame = tk.Frame(Checklist_LargeFrame, bg='')
        frame.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.TOP)

        frame2 = tk.Frame(Checklist_LargeFrame)
        frame2.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.BOTTOM)

        # Create the CheckboxTreeview
        tree = CheckboxTreeview(frame)
        tree.pack(side=tk.LEFT, fill='y')

        tree2 = CheckboxTreeview(frame2)
        tree2.pack(side=tk.LEFT, fill='y')

        # Create the scrollbar
        scrollbar = tk.Scrollbar(frame, orient='vertical', command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        scrollbar2 = tk.Scrollbar(frame2, orient='vertical', command=tree2.yview)
        scrollbar2.pack(side=tk.RIGHT, fill='y')

        with open('F:\\tkinter\\01_practice\\sample.json') as file:
            datas = json.load(file)
            linux_feature = list(datas['Linux'].keys())
            android_feature = list(datas['Android'].keys())
        # Configure the CheckboxTreeview to use the scrollbar
        tree.configure(yscrollcommand=scrollbar.set)

        parent_id = ""
        #insert root node
        Linux = str(1)
        Android = str(2)

        #tree node insert
        tree.insert(parent_id, "end", Linux, text='Linux')
        tree.insert(parent_id, "end", Android, text='Android')
        sub_linuxfeature = linux_feature
        
        #linux 부분 확인 필요
        for i in range(0, linux_feature.__len__()):
            node_id = f"{i}1"
            tree.insert(Linux, "end", node_id, text=linux_feature[i])

            sublist = datas['Linux'][linux_feature[i]]
            json_test = [boot['name'] for boot in sublist]

            for j in range(len(json_test)):
                tree.insert(node_id, "end", f"{i}2_{j}", text=json_test[j])
      
        
        #수동 추가 부분
        for i in range(0, android_feature.__len__()):
            tree.insert(Android, "end", f"{i}2", text=android_feature[i])

        # tree2.configure(yscrollcommand=scrollbar.set)
        # for i in range(1, 11):
        #     parent_id = "" if i % 2 == 1 else str(i // 2)
        #     Linux = str(i)
        #     tree2.insert(parent_id, "end", Linux, text='Linux')
        #     # tree2.insert(Linux, "end", f"{i}1", text=(str(i), f'Item {i}1'))
        #     tree2.insert(Linux, "end", f"{i}2", text=(str(i), f'Item {i}2'))
        #     tree2.insert(f"{i}2", "end", f"{i}21", text=(str(i), f'Item {i}21'))
        
class Textview:
    
    def __init__(self, window):
        global arr
        arr = {}

        self.largeframe = tk.Frame(window, bg='white')
        self.largeframe.pack(padx=5, pady=5, fill='both', expand=True, anchor=tk.NW, side=tk.LEFT)

        self.textframe = tk.Frame(self.largeframe, height=600, bg='white')
        self.textframe.pack(padx=5, pady=5, fill='x', expand=True, anchor=tk.NW, side=tk.TOP)
        self.textframe.pack_propagate(False) 

        self.textview = tk.Text(self.textframe, bg="silver", state=tk.DISABLED)
        self.textview.pack(padx=5, pady=5, fill='both', anchor=tk.NW, side=tk.LEFT, expand=True)

        # Add scrollbar to textview1
        vbar1 = tk.Scrollbar(self.textframe, orient='vertical', command=self.textview.yview)
        vbar1.pack(side="right", fill='y')
        self.textview.configure(yscrollcommand=vbar1.set)

        # Change state to NORMAL, insert text, then change back to DISABLED
        self.textview.config(state=tk.NORMAL)
        self.textview.insert(tk.END, " ")
        self.textview.config(state=tk.DISABLED)

        self.textview.bind('<Control-f>', self.search_text)
        self.textview.configure(font=("Courier", 10))

        self.textframe2 = tk.Frame(self.largeframe, height=50, bg='white')
        self.textframe2.pack(padx=5, pady=5, fill='x', expand=True, anchor=tk.NW, side=tk.BOTTOM)

        self.textview2 = tk.Text(self.textframe2, height=30, bg="silver")
        self.textview2.pack(padx=5, pady=5, fill='x', anchor=tk.SW, side=tk.LEFT, expand=True)

        # Add scrollbar to textview2
        vbar2 = tk.Scrollbar(self.textframe2, orient='vertical', command=self.textview2.yview)
        vbar2.pack(side="right", fill='y')
        self.textview2.configure(yscrollcommand=vbar2.set)

        self.textview2.configure(font=("Courier", 10))
    
    def search_text(self, event):
        search_term = simpledialog.askstring("Search", "Enter text to search")
        if search_term:
            start = "1.0"
            while True:
                start = self.textview.search(search_term, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(search_term)}c"
                self.textview.tag_add("search", start, end)
                self.textview.tag_config("search", background="yellow")
                start = end


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
container3.update_progress(80)
container6 = Checklist(window)
container7 = Textview(window)
container5 = Cont4(window)


# 윈도우 실행
window.mainloop()


