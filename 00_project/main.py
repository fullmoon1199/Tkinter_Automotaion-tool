import tkinter as tk
import serial
from tkinter import ttk
from tkinter import *
from tkinter import Frame, X, N
from tkinter import simpledialog
from ttkwidgets import CheckboxTreeview
import json
import openpyxl
from collections import OrderedDict
from tkinter import filedialog
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

def on_open_excel():
    file_path = filedialog.askopenfilename()
    excel_file_path = file_path

    wb = openpyxl.load_workbook(excel_file_path)
    sheet = wb['Validation Result']

    data_list = []

    for rownum in range(6, 223):
        data = OrderedDict()
        column_value = [cell.value for cell in sheet[rownum]]
        data['Number'] = column_value[0]
        data['TC Number'] = column_value[1]
        data['Category'] = column_value[2]
        data['BL'] = column_value[9]
        data['BA'] = column_value[10]
        data['LA'] = column_value[11]
        Command = column_value[25]
        Criterion = column_value[26]

        if Command:
            Command = Command.split('\n')
        else:
            Command = []

        if Criterion:
            Criterion = Criterion.split('\n')
        else:
            Criterion = []
        
        data['Command'] = Command
        data['Criterion'] = Criterion

        data_list.append(data)

    for i in range(len(data_list)):
        print(data_list[i])

    json_file_path = 'F:\\tkinter\\test.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4, ensure_ascii=False)

    print(f"JSON 파일이 성공적으로 저장되었습니다: {json_file_path}")



#hover 색상변경 기능5
def on_enter(widget):
    widget.config(bg='lightblue')
def on_leave(widget):
    widget.config(bg='white')


# Tkinter 윈도우 생성
window = tk.Tk()
window.title("V920 SADK Verification Program")

# 윈도우 크기 설정
window.geometry("1650x900+30+30")
# 상단 텍스트 추가
title_frame = tk.Frame(window)
title_frame.pack(fill=X, anchor=N)
title_label1 = tk.Label(title_frame, text="V920 SADK Verification Program", font=("Calibri", 16, "bold"))
title_label2 = tk.Label(title_label1, text="Ver.0.0.1", font=("Helvetica", 10,))
title_label1.pack(pady=12 ,fill=X)
title_label2.pack(side=tk.RIGHT)

class Cont1:
    def __init__(self, window):
        self.buttonframe = Frame(window)
        self.buttonframe.pack(fill=X, anchor=N)

        self.combo = ttk.Combobox(self.buttonframe,width=30, values=on_search_port(), state="readonly", style="TCombobox")
        self.combo.pack(padx=10, pady=18, anchor=tk.NW, side=tk.LEFT)

        self.search_port_button = tk.Button(self.buttonframe, text="Search Port", command=on_search_port, width=15, height=3)
        self.search_port_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)
        # hover 색상변경 기능
        self.search_port_button.bind("<Enter>", lambda event, widget=self.search_port_button: on_enter(widget))
        self.search_port_button.bind("<Leave>", lambda event, widget=self.search_port_button: on_leave(widget))

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

        self.open_excel_button = tk.Button(self.buttonframe, text="Open Excel", command=on_open_excel, width=15, height=3)
        self.open_excel_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.exit_button = tk.Button(self.buttonframe, text="Exit", command=window.quit, width=5, height=3, bg='red', fg='white',font=("Helvetica", 8, "bold"))
        self.exit_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)
        
class Cont2: # 진행바 컨테이너
    def __init__(self, window):
        self.progressframe = Frame(window)
        self.progressframe.pack(fill=X, anchor=N)

        self.progressbar = ttk.Progressbar(self.progressframe, maximum=100, length=1500)
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

        auto = 0
        manual = 0
    
        Checklist_LargeFrame = tk.Frame(window, bg = 'white')
        Checklist_LargeFrame.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)
        # Create a frame to hold the CheckboxTreeview and scrollbar
        frame = tk.Frame(Checklist_LargeFrame, bg='white')
        frame.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        frame2 = tk.Frame(Checklist_LargeFrame, bg='white')
        frame2.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        # Create the CheckboxTreeview
        title_label = tk.Label(frame, text=f"Auto TC : # 선택개수 / {auto}개", font=("Helvetica", 10, "bold"),bg='white')
        title_label.pack()
        self.tree = CheckboxTreeview(frame)
        self.tree.pack(side=tk.LEFT, fill='y')

        title_label2 = tk.Label(frame2, text=f"Manual TC : # 선택개수 / {manual}개", font=("Helvetica", 10, "bold"),bg='white')
        title_label2.pack()
        self.tree2 = CheckboxTreeview(frame2)
        self.tree2.pack(side=tk.LEFT, fill='y')

        # Create the scrollbar
        scrollbar = tk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        scrollbar2 = tk.Scrollbar(frame2, orient='vertical', command=self.tree2.yview)
        scrollbar2.pack(side=tk.RIGHT, fill='y')

        with open('F:\\tkinter\\01_practice\\sample2.json') as file:
            datas = json.load(file)
            linux_feature = list(datas['Linux'].keys())
            android_feature = list(datas['Android'].keys())
            la_feature = list(datas['LinuxAndroid'].keys())
        # Configure the CheckboxTreeview to use the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree2.configure(yscrollcommand=scrollbar2.set)

        parent_id = ""
        #insert root node
        Linux = str(1)
        Android = str(2)
        LA = str(3)

        #tree node insert
        self.tree.insert(parent_id, "end", Linux, text='Linux')
        self.tree.insert(parent_id, "end", Android, text='Android')
        self.tree.insert(parent_id, "end", LA, text='LinuxAndroid')
        self.tree2.insert(parent_id, "end", Linux, text='Linux')
        self.tree2.insert(parent_id, "end", Android, text='Android')
        self.tree2.insert(parent_id, "end", LA, text='LinuxAndroid')

        #하위 nood insert
        for i in range(0, linux_feature.__len__()):
            node_id = f"{i}1"
            self.tree.insert(Linux, "end", node_id, text=linux_feature[i])
            self.tree2.insert(Linux, "end", node_id, text=linux_feature[i])
            sublist = datas['Linux'][linux_feature[i]]
            json_test = [feature['name'] for feature in sublist]

            for j in range(json_test.__len__()):
                find_mode = [feature['mode'] for feature in sublist]
                if find_mode[j] == 'auto':
                    self.tree.insert(node_id, "end", f"{i}2_{j}", text=json_test[j])
                    auto += 1
                else:
                    self.tree2.insert(node_id, "end", f"{i}2_{j}", text=json_test[j])
                    manual += 1

        for i in range(0, android_feature.__len__()):
            node_id2 = f"{i}2"
            self.tree.insert(Android, "end", node_id2, text=android_feature[i])
            self.tree2.insert(Android, "end", node_id2, text=android_feature[i])
            sublist2 = datas['Android'][android_feature[i]]
            json_test2 = [feature['name'] for feature in sublist2]
            
            for j in range(json_test2.__len__()):
                find_mode = [feature['mode'] for feature in sublist]
                if find_mode[j] == 'auto':
                    self.tree.insert(node_id2, "end", f"{i}3_{j}", text=json_test2[j])
                    auto += 1
                else:
                    self.tree2.insert(node_id2, "end", f"{i}3_{j}", text=json_test2[j])
                    manual += 1

            
        for i in range(0, la_feature.__len__()):
            node_id3 = f"{i}3"
            self.tree.insert(LA, "end", node_id3, text=la_feature[i])
            self.tree2.insert(LA, "end", node_id3, text=la_feature[i])
            sublist3 = datas['LinuxAndroid'][la_feature[i]]
            json_test3 = [feature['name'] for feature in sublist3]
            
            for j in range(json_test3.__len__()):
                find_mode = [feature['mode'] for feature in sublist]
                if find_mode[j] == 'auto':
                    self.tree.insert(node_id3, "end", f"{i}4_{j}", text=json_test3[j])
                    auto += 1
                else:
                    self.tree2.insert(node_id3, "end", f"{i}4_{j}", text=json_test3[j])
                    manual += 1

        title_label.config(text=f"Auto TC : # 선택개수 / {auto}개")
        title_label2.config(text=f"Auto TC : # 선택개수 / {manual}개")       

        def get_checked_bind():   
            get_checked = self.tree.get_checked()
            get_checked2 = self.tree2.get_checked()
            print(len(get_checked))
            print(len(get_checked2))
            title_label.config(text=f"Auto TC : # {len(get_checked)}개 / {auto}개")
            title_label2.config(text=f"Maunal TC : # {len(get_checked2)}개 / {manual}개")  
        
        button = tk.Button(frame2, text="Click Me", command=get_checked_bind)
        button.pack()
        
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
        canvas.place(x=248,y=40)

        canvas = tk.Canvas(window,width=2, height= 70, bg="silver")
        canvas.place(x=640,y=40)

        canvas = tk.Canvas(window,width=2, height= 70, bg="silver")
        canvas.place(x=915,y=40)

        canvas = tk.Canvas(window,width=2, height= 70, bg="silver")
        canvas.place(x=1445,y=40)

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


