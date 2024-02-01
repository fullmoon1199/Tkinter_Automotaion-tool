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
        data['Linux'] = column_value[9]
        data['Android'] = column_value[10]
        data['LinuxAndroid'] = column_value[11]
        data['Mode'] = column_value[25]
        Command = column_value[7]
        Criterion = column_value[5]

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

    json_file_path = 'F:\\tkinter\\test.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4)

    print(f"JSON 파일이 성공적으로 저장되었습니다: {json_file_path}")

    add_node_callback()

def add_node_callback():
    container6.add_node()   

#hover color change function
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

#button GUI 
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

# progress bar GUI  
class Cont2: 
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

#checkbox GUI 
class Checklist:
    auto = 0
    manual = 0
    def __init__(self, window):
        
        Checklist_LargeFrame = tk.Frame(window, bg = 'white')
        Checklist_LargeFrame.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)
        # Create a frame to hold the CheckboxTreeview and scrollbar
        frame = tk.Frame(Checklist_LargeFrame, bg='white')
        frame.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        frame2 = tk.Frame(Checklist_LargeFrame, bg='white')
        frame2.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        # Create the CheckboxTreeview
        title_label = tk.Label(frame, text=f"Auto TC : # 선택개수 / {self.auto}개", font=("Helvetica", 10, "bold"),bg='white')
        title_label.pack()
        self.tree = CheckboxTreeview(frame)
        self.tree.pack(side=tk.LEFT, fill='y')

        title_label2 = tk.Label(frame2, text=f"Manual TC : # 선택개수 / {self.manual}개", font=("Helvetica", 10, "bold"),bg='white')
        title_label2.pack()
        self.tree2 = CheckboxTreeview(frame2)
        self.tree2.pack(side=tk.LEFT, fill='y')

        # Create the scrollbar
        scrollbar = tk.Scrollbar(frame, orient='vertical', command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill='y')

        scrollbar2 = tk.Scrollbar(frame2, orient='vertical', command=self.tree2.yview)
        scrollbar2.pack(side=tk.RIGHT, fill='y')

        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree2.configure(yscrollcommand=scrollbar2.set)
        title_label.config(text=f"Auto TC : # 선택개수 / {self.auto}개")
        title_label2.config(text=f"Man TC : # 선택개수 / {self.manual}개")      

        def get_checked_bind():
            # Get checked items from the CheckboxTreeviews
            get_checked = self.tree.get_checked()
            get_checked2 = self.tree2.get_checked()

            # Filter items with level 2
            level_2_checked = [item for item in get_checked if self.tree.parent(item) != ""]
            level_2_checked2 = [item for item in get_checked2 if self.tree2.parent(item) != ""]

            # Print and update labels with the count of level 2 checked items
            print(len(level_2_checked))
            print(len(level_2_checked2))

            title_label.config(text=f"Auto TC : # {len(level_2_checked)}개 / {self.auto}개")
            title_label2.config(text=f"Manual TC : # {len(level_2_checked2)}개 / {self.manual}개")


# ...

        button = tk.Button(frame2, text="Click Me", command=get_checked_bind)
        button.pack()

    #checkbox node insert
    def add_node(self):
        with open('F:\\tkinter\\test.json') as file:
            datas = json.load(file)

        parent_id = ""
        Linux = str(0)
        Android = str(1)
        LA = str(2)
        BSP = [Linux, Android, LA]
        #tree node insert
        self.tree.insert(parent_id, "end", Linux, text='Linux')
        self.tree.insert(parent_id, "end", Android, text='Android')
        self.tree.insert(parent_id, "end", LA, text='LinuxAndroid')
        self.tree2.insert(parent_id, "end", Linux, text='Linux')
        self.tree2.insert(parent_id, "end", Android, text='Android')
        self.tree2.insert(parent_id, "end", LA, text='LinuxAndroid')

        #20240129 여기부터 sub node 구현
        Category_list = list(set([item["Category"] for item in datas]))
        print(Category_list)
        z = 0
        for i in range(0, len(BSP)):
            for j in range(0, len(Category_list)):
                self.tree.insert(BSP[i], "end", f"{Category_list[j]}_{i}", text=Category_list[j])
                self.tree2.insert(BSP[i], "end", f"{Category_list[j]}_{i}", text=Category_list[j])
                if i == 0:
                    sublist = [item for item in datas if item["Category"] == Category_list[j] and item["Linux"] == "O" and item["Mode"] == "auto"]
                    for k in range(0, len(sublist)):
                        self.tree.insert(f"{Category_list[j]}_{i}", "end", f"{Category_list[j]}_{i}_{z}", text=sublist[k]["TC Number"])
                        z += 1
                elif i == 1:
                    sublist = [item for item in datas if item["Category"] == Category_list[j] and item["Android"] == "O" and item["Mode"] == "auto"]
                    for k in range(0, len(sublist)):
                        self.tree.insert(f"{Category_list[j]}_{i}", "end", f"{Category_list[j]}_{i}_{z}", text=sublist[k]["TC Number"])
                        z += 1
                elif i == 2:
                    sublist = [item for item in datas if item["Category"] == Category_list[j] and item["LinuxAndroid"] == "O" and item["Mode"] == "auto"]
                    for k in range(0, len(sublist)):
                        self.tree.insert(f"{Category_list[j]}_{i}", "end", f"{Category_list[j]}_{i}_{z}", text=sublist[k]["TC Number"])
                        z += 1
                
                if i == 0:
                    sublist = [item for item in datas if item["Category"] == Category_list[j] and item["Linux"] == "O" and item["Mode"] == "manual"]
                    for k in range(0, len(sublist)):
                        self.tree2.insert(f"{Category_list[j]}_{i}", "end", f"{Category_list[j]}_{i}_{z}", text=sublist[k]["TC Number"])
                        z += 1
                elif i == 1:   
                    sublist = [item for item in datas if item["Category"] == Category_list[j] and item["Android"] == "O" and item["Mode"] == "manual"]
                    for k in range(0, len(sublist)):
                        self.tree2.insert(f"{Category_list[j]}_{i}", "end", f"{Category_list[j]}_{i}_{z}", text=sublist[k]["TC Number"])
                        z += 1
                elif i == 2:
                    sublist = [item for item in datas if item["Category"] == Category_list[j] and item["LinuxAndroid"] == "O" and item["Mode"] == "manual"]
                    for k in range(0, len(sublist)):
                        self.tree2.insert(f"{Category_list[j]}_{i}", "end", f"{Category_list[j]}_{i}_{z}", text=sublist[k]["TC Number"])
                        z += 1

#textview GUI 

class Textview:
    def __init__(self, window):
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
        self.textview.bind('<Down>', self.next_occurrence)  # Bind Down arrow key
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

        # Bind a function to handle textview2 input
        self.textview2.bind('<Return>', self.update_textview)

        self.search_results = []
        self.current_search_index = 0

    def update_textview(self, event):
        # Get the text from textview2
        new_text = self.textview2.get("1.0", tk.END)

        self.textview2.delete("1.0", tk.END)  # Clear existing text

        # Remove the trailing newline character
        new_text = new_text.strip()

        # Insert the text into textview1
        self.textview.config(state=tk.NORMAL)
        if new_text == "clear":
            self.textview.delete("1.0", tk.END)
        else:
            self.textview.insert(tk.END, new_text + '\n')
        self.textview.config(state=tk.DISABLED)

    # Search text function
    def search_text(self, event):
        search_term = simpledialog.askstring("Search", "Enter text to search")
        if search_term:
            self.search_results = []  # Clear previous search results
            start = "1.0"
            while True:
                start = self.textview.search(search_term, start, stopindex=tk.END)
                if not start:
                    break
                end = f"{start}+{len(search_term)}c"
                self.textview.tag_add("search", start, end)
                self.search_results.append(start)
                start = end

            if self.search_results:
                self.current_search_index = 0
                self.show_next_search_result()

    # Show next search result
    def show_next_search_result(self):
        if self.search_results:
            index = self.current_search_index % len(self.search_results)
            self.textview.tag_remove("search", "1.0", tk.END)
            self.textview.tag_add("search", self.search_results[index], f"{self.search_results[index]}+{len(self.search_results[index])}c")
            self.textview.tag_config("search", background="yellow")
            self.textview.see(self.search_results[index])
            self.current_search_index += 1

    # Color reset function
    def reset_search_color(self, start, end):
        self.textview.tag_remove("search", start, end)
        self.textview.tag_config("search", background="")

    # Move to the next occurrence on Down arrow key press
    def next_occurrence(self, event):
        if self.search_results:
            self.show_next_search_result()


#캔버스 컨테이너
class Cont4: 
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


