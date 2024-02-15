import tkinter as tk
import serial
from tkinter import ttk
from tkinter import *
from tkinter import Frame, X, N
from tkinter import simpledialog
from ttkwidgets import CheckboxTreeview
import json
from collections import OrderedDict
from tkinter import filedialog
import serial.tools.list_ports
import threading
import openpyxl

def pass_func(response,hello):
    response = response
    hello = hello
    
    

def check_open_ports():
    open_ports = []
    for port in serial.tools.list_ports.comports():
        try:
            # 시리얼 포트를 시도하여 열린 경우 open_ports 리스트에 추가
            serial_port = serial.Serial(port.device)
            serial_port.close()
            open_ports.append(port.device)
        except serial.SerialException:# 예외처리
            pass
    return open_ports

def on_search_port(combo):
    ports = serial.tools.list_ports.comports()
    port_device_mapping = {p.device: p.description for p in ports}  # 포트 번호와 디바이스 이름 매핑
    print("\nPort-Device mapping:", port_device_mapping)  # 포트-디바이스 매핑 출력
    available_ports = [p.description for p in ports]
    combo['values'] = available_ports  # 콤보박스에 사용 가능한 포트 목록 설정

def update_combobox():
    on_search_port(container1.combo)

def on_open():
    selected_port_name = container1.combo.get()  # 선택된 포트 이름 가져오기
    ports = serial.tools.list_ports.comports()
    port_device_mapping = {p.device: p.description for p in ports}  # 포트 번호와 디바이스 이름 매핑

    # 선택된 포트 이름과 매핑된 포트 번호 찾기
    global serial_port
    for port, device_name in port_device_mapping.items():
        if device_name == selected_port_name:
            serial_port = port
            break

    if serial_port is not None:
        print("Selected port:", serial_port)
    else:
        print("Selected port not found.")
    if serial_port:  # 선택된 포트가 있는지 확인
        try:
            serial_port = serial.Serial(serial_port, baudrate=115200)  # 선택된 포트 열기
            print(f"Serial port {serial_port} opened successfully.")
            # 시리얼 통신 작업 수행
        except serial.SerialException as e:
            print(f"Error initializing serial port: {e}")
            serial_port = None

    read_thread = threading.Thread(target=container7.read_serial, daemon=True)
    read_thread.start()

   
def on_close():
    # TODO: Close 동작 구현
    pass

def on_start_tc():
    get_checked_ids = container6.tree.get_checked()  # 체크된 아이템의 ID를 가져옴
    checked_item_names = []  # 체크된 아이템의 이름을 저장할 리스트

    # 각 체크된 아이템의 ID를 순회하면서 이름을 가져와서 리스트에 추가
    for item_id in get_checked_ids:
        item_text = container6.tree.item(item_id, "text")  # ID로부터 아이템의 텍스트를 가져옴
        checked_item_names.append(item_text)  # 가져온 텍스트를 리스트에 추가

    print(checked_item_names) 
  #240207 여기서부터 시작
    with open('F:\\tkinter\\00_project\\TestSequence.json') as file:
        data = json.load(file)
        for item_name in checked_item_names:
            target_tc_number = f"{item_name}"
            found_data = next((item for item in data if item["TC Number"] == target_tc_number), None)
            # ToolSequence에서 명령어들을 읽어와서 '#' 또는 '^'로 시작하는 경우에 따라 리스트에 추가
            # print(type(found_data))
            for command in found_data["ToolSequence"]: 
                if command.startswith("#"):
                    content = command.split(' ', 1)[-1]
                    serial_port.write(content.encode())
                    serial_port.write('\r'.encode())               
                elif command.startswith("^"):
                    print(command)

def separate_commands(data):
    hash_commands = []
    hash_criterion = []

    # ToolSequence에서 명령어들을 읽어와서 '#' 또는 '^'로 시작하는 경우에 따라 리스트에 추가
    for command in data["ToolSequence"]:
        if command.startswith("#"):
            hash_commands.append(command)
        elif command.startswith("^"):
            hash_criterion.append(command)
    
def on_stop_tc():
    # TODO: Stop TC 동작 구현
    pass

def on_su(con):
    serial_port.write(('su' + '\r').encode())

# root 동작 구현
def on_root(con):
    serial_port.write(('root' + '\r').encode())

def on_shift_f2():
    serial_port.write(b" [24~")
    serial_port.write('\r'.encode("utf-8"))  

def on_shift_f3():
    serial_port.write(b" [25~")
    serial_port.write('\r'.encode("utf-8")) 

def choised_radiobutton(con):
    selected_value = con.radio_var.get()  # 현재 선택된 버튼의 value 값을 가져옴

    if selected_value == 1:
        selected_button = "Bearmetal_Linux"
    elif selected_value == 2:
        selected_button = "Bearmetal_Android"
    elif selected_value == 3:
        selected_button = "Linux_Android_VM"
    else:
        selected_button = "No selection"

    return selected_button

def on_open_excel():

    file_path = filedialog.askopenfilename()
    excel_file_path = file_path

    wb = openpyxl.load_workbook(excel_file_path)
    sheet = wb[choised_radiobutton(container1)]

    data_list = []

    for rownum in range(6, 100):
        if not sheet[rownum][0].value:
            break
        else:
            data = OrderedDict()
            column_value = [cell.value for cell in sheet[rownum]]
            data['Number'] = column_value[0]
            data['TC Number'] = column_value[1]
            data['Category'] = column_value[2]
            data['BL'] = column_value[10]
            data['BA'] = column_value[11]
            data['LA'] = column_value[12]
            data['Automatic'] = column_value[14]
            ToolSequence = column_value[15]

        if ToolSequence:
            ToolSequence = ToolSequence.split('\n')
        else:
            ToolSequence = []

        data['ToolSequence'] = ToolSequence

        data_list.append(data)

    for i in range(len(data_list)):
        print(data_list[i])

    json_file_path = 'F:\\tkinter\\00_project\\TestSequence.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4, ensure_ascii=False)

    print(f"JSON 파일이 성공적으로 저장되었습니다: {json_file_path}")

    add_node(container6)

def add_node(con):

    # Node delete
    for child in con.tree.get_children():
        con.tree.delete(child)
    for child in con.tree2.get_children():
        con.tree2.delete(child)

    # Node insert
    with open('F:\\tkinter\\00_project\\TestSequence.json') as file:
        datas = json.load(file)
    parent_id = ""

    chosen_radio_value = choised_radiobutton(container1)  # Unnecessary function call removed
    if chosen_radio_value == "Bearmetal_Linux":
        bsp_id = "Linux"
    elif chosen_radio_value == "Bearmetal_Android":
        bsp_id = "Android"
    elif chosen_radio_value == "Linux_Android_VM":
        bsp_id = "LinuxAndroid"

    # Tree node insert
    con.tree.insert(parent_id, "end", bsp_id, text=f"{bsp_id}")
    con.tree2.insert(parent_id, "end", bsp_id, text=f"{bsp_id}")

    # Sub node implementation
    Category_list = list(set([item["Category"] for item in datas]))
    print(Category_list)

    for category in Category_list:
        sublist = [item for item in datas if item["Category"] == category]
        sublist_O = [item for item in sublist if item["Automatic"] == "O"]
        sublist_X = [item for item in sublist if item["Automatic"] == "X"]

        # Insert Category node
        tree_node = con.tree.insert(bsp_id, "end", f"{category}", text=f"{category}")
        tree2_node = con.tree2.insert(bsp_id, "end", f"{category}", text=f"{category}")

        # Insert sublist for 'O' Automatic
        for j, item in enumerate(sublist_O):
            con.tree.insert(tree_node, "end", f"{category}_{j}", text=f"{item['TC Number']}")
        
        # Insert sublist for 'X' Automatic
        for j, item in enumerate(sublist_X):
            con.tree2.insert(tree2_node, "end", f"{category}_{j}", text=f"{item['TC Number']}")

    # Delete Category node if it has no children
    for category in Category_list:
        # Check if the category has children
        if not con.tree.get_children(category):
            con.tree.delete(category)
        if not con.tree2.get_children(category):
            con.tree2.delete(category)



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
title_frame = tk.Frame(window,bg='black')
title_frame.pack(fill=X, anchor=N)
title_label1 = tk.Label(title_frame, text="V920 SADK Verification Program", font=("Calibri", 16, "bold"), bg='black', fg='white')
title_label2 = tk.Label(title_label1, text="Ver.0.0.1", font=("Helvetica", 10,),bg='black', fg='white')
title_label1.pack(fill=X)
title_label2.pack(side=tk.RIGHT)

#button GUI 
class Cont1:
    def __init__(self, window):
        self.buttonframe = Frame(window, bg='red')
        self.buttonframe.pack(fill=X, anchor=N)

        self.combo = ttk.Combobox(self.buttonframe, width=60, state="readonly", style="TCombobox")
        self.combo.pack(padx=10, pady=18, anchor=tk.NW, side=tk.LEFT)

        self.search_port_button = tk.Button(self.buttonframe, text="Search Port", command=update_combobox, width=15, height=4)
        self.search_port_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)
        # hover 색상변경 기능
        self.search_port_button.bind("<Enter>", lambda event, widget=self.search_port_button: on_enter(widget))
        self.search_port_button.bind("<Leave>", lambda event, widget=self.search_port_button: on_leave(widget))

        self.open_button = tk.Button(self.buttonframe, text="Open", command=on_open, width=15, height=4)
        self.open_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.close_button = tk.Button(self.buttonframe, text="Close", command=on_close, width=15, height=4)
        self.close_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        # self.layout = tk.Label(self.buttonframe)
        # self.layout.pack(padx=10 ,anchor=tk.NW, side=tk.LEFT)

        self.start_tc_button = tk.Button(self.buttonframe, text="Start TC", command=on_start_tc, width=15, height=4)
        self.start_tc_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.stop_tc_button = tk.Button(self.buttonframe, text="Stop TC", command=on_stop_tc, width=15, height=4)
        self.stop_tc_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        # self.layout = tk.Label(self.buttonframe)
        # self.layout.pack(padx=10 ,anchor=tk.NW, side=tk.LEFT)

        self.su_button = tk.Button(self.buttonframe, text="SU", command=lambda: on_su(container7), width=8, height=4)
        self.su_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.root_button = tk.Button(self.buttonframe, text="Root", command=lambda: on_root(container7), width=8, height=4)
        self.root_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.shift_f2_button = tk.Button(self.buttonframe, text="Shift+F2", command=on_shift_f2, width=15, height=4)
        self.shift_f2_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.shift_f3_button = tk.Button(self.buttonframe, text="Shift+F3", command=on_shift_f3, width=15, height=4)
        self.shift_f3_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        # self.layout = tk.Label(self.buttonframe)
        # self.layout.pack(padx=15 ,anchor=tk.NW, side=tk.LEFT)

        self.smallframe = Frame(self.buttonframe)
        self.smallframe.pack(anchor=tk.NW, side=tk.LEFT)

        #BSP radio button
        self.radio_var = tk.IntVar()
        self.bl_button = Radiobutton(self.smallframe, text="BL", value=1, variable=self.radio_var)
        self.ba_button = Radiobutton(self.smallframe, text="BA", value=2, variable=self.radio_var)
        self.la_button = Radiobutton(self.smallframe, text="LA", value=3, variable=self.radio_var)

        self.bl_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.TOP)
        self.ba_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.TOP)
        self.la_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.TOP)

        

        self.open_excel_button = tk.Button(self.buttonframe, text="Open Excel", command=on_open_excel, width=15, height=4)
        self.open_excel_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.exit_button = tk.Button(self.buttonframe, text="Exit", command=window.quit, width=5, height=3, bg='red', fg='white',font=("Helvetica", 8, "bold"))
        self.exit_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

# progress bar GUI  
class Cont2: 
    def __init__(self, window):
        self.progressframe = Frame(window, bg='yellow')
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
        
        Checklist_LargeFrame = tk.Frame(window, bg = 'blue')
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

        button = tk.Button(frame2, text="Click Me", command=get_checked_bind)
        button.pack()

        # Attach right-click event to show context menu for tree
        self.tree.bind("<Button-3>", self.show_context_menu_tree)
        self.tree2.bind("<Button-3>", self.show_context_menu_tree2)

        # Create context menu for tree
        self.context_menu_tree = tk.Menu(window, tearoff=0)
        self.context_menu_tree.add_command(label="View", command=self.context_menu_action1)

        self.context_menu_tree2 = tk.Menu(window, tearoff=0)
        self.context_menu_tree2.add_command(label="View", command=self.context_menu_action2)


    def show_context_menu_tree(self, event):
        # Display the context menu for tree at the cursor's location
        item_under_cursor = self.tree.identify_row(event.y)
        if item_under_cursor:
            self.tree.selection_set(item_under_cursor)
            self.context_menu_tree.post(event.x_root, event.y_root)

    def show_context_menu_tree2(self, event):
        # Display the context menu for tree2 at the cursor's location
        item_under_cursor = self.tree2.identify_row(event.y)
        if item_under_cursor:
            self.tree2.selection_set(item_under_cursor)
            self.context_menu_tree2.post(event.x_root, event.y_root)

    def context_menu_action1(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_name = self.tree.item(selected_item[0], 'text')
            print(f"Name: {item_name}")
            with open('F:\\tkinter\\00_project\\TestSequence.json') as file:
                data = json.load(file)

                target_tc_number = f"{item_name}"
                found_data = next((item for item in data if item["TC Number"] == target_tc_number), None)

                commands_text = []
                criterion_text = []

                # ToolSequence에서 명령어들을 읽어와서 '#' 또는 '^'로 시작하는 경우에 따라 리스트에 추가
                for command in found_data["ToolSequence"]: 
                    if command.startswith("#"):
                        commands_text.append(command)
                    elif command.startswith("^"):
                        criterion_text.append(command)

            top = Toplevel(window)
            top.geometry("1400x500")
            top.title("Child Window")
            SubFrame = tk.Frame(top, bg='yellow')
            SubFrame.pack(fill='both', expand=True, anchor=tk.NW, side=tk.LEFT)
            criterion = tk.Text(SubFrame, bg="silver", )
            command = tk.Text(SubFrame, bg="silver")
            criterion.pack(padx=5, pady=5, fill='both', anchor=tk.NW, side=tk.LEFT, expand=True)
            command.pack(padx=5, pady=5, fill='both', anchor=tk.NW, side=tk.LEFT)
            criterion.insert(tk.END,criterion_text)
            command.insert(tk.END,commands_text)

    def context_menu_action2(self):
        selected_item = self.tree2.selection()
        if selected_item:
            item_name = self.tree2.item(selected_item[0], 'text')
            print(f"Name: {item_name}")

#textview GUI 

class Textview:
    def __init__(self, window):
        self.largeframe = tk.Frame(window, bg='green')
        self.largeframe.pack(padx=5, pady=5, fill='both', expand=True, anchor=tk.NW, side=tk.LEFT)

        self.textframe = tk.Frame(self.largeframe, height=600, bg='red')
        self.textframe.pack(padx=5, pady=5, fill='both', expand=True, anchor=tk.NW, side=tk.TOP)
        self.textframe.pack_propagate(False)

        self.textview = tk.Text(self.textframe, bg="silver", state=tk.DISABLED)
        self.textview.pack(padx=5, pady=5, fill='both', anchor=tk.NW, side=tk.LEFT, expand=True)

        self.textview.bind('<Control-f>', self.search_text)
        self.textview.bind('<Down>', self.next_occurrence)  # Bind Down arrow key
        self.textview.configure(font=("Courier", 10))

        # Add scrollbar to textview1
        vbar1 = tk.Scrollbar(self.textframe, orient='vertical', command=self.textview.yview)
        vbar1.pack(side="right", fill='y')
        self.textview.configure(yscrollcommand=vbar1.set)

        self.textframe2 = tk.Frame(self.largeframe, bg='purple')
        self.textframe2.pack(padx=5, pady=5, fill='x', expand=True, anchor=tk.NW, side=tk.TOP)

        self.input_entry = ttk.Entry(self.textframe2, font=('Courier', 12), width=100)
        self.input_entry.pack(pady=10)

        # try:
        #     self.serial_port = serial.Serial('COM22', baudrate=115200, timeout=1)  # 5초 timeout으로 변경
        #     print(f"Serial port {self.serial_port} opened successfully.")
        #     self.serial_port.close()

        # except serial.SerialException as e:
        #     print(f"Error initializing serial port: {e}")
        #     self.serial_port = None

        def on_right_click(event):
            # 컨텍스트 메뉴를 표시
            context_menu.post(event.x_root, event.y_root)

        def paste_from_clipboard():
            # 클립보드에서 내용 읽기
            clipboard_content = window.clipboard_get()

            # 읽은 내용을 엔트리에 삽입
            self.input_entry.insert(tk.END, clipboard_content)
            serial_port.write(clipboard_content.encode())

        # 엔트리 위젯에 우클릭 이벤트에 대한 핸들러 추가
        self.input_entry.bind("<Button-3>", on_right_click)

        # 컨텍스트 메뉴 생성
        context_menu = tk.Menu(window, tearoff=0)
        context_menu.add_command(label="붙여넣기", command=paste_from_clipboard)
        
        # send_button.pack()
        def on_key(event):
            # 이벤트 핸들러 함수
            print(f'Key pressed: {event.char}')
            if (event.char == '\b'):
                serial_port.write('\b'.encode())
            elif event.char == '\r':                
                self.input_entry.delete(0, tk.END)
                serial_port.write('\r'.encode())
            else:
                serial_port.write(event.char.encode())
                

        self.input_entry.bind('<Key>', on_key)

    def read_serial(self):
        if serial_port:  # 시리얼 포트가 열렸는지 확인
            while True:
                try:
                    serial_output = serial_port.readline().decode('utf-8', errors='replace').strip()
                    if serial_output:
                        self.show_output(f"{serial_output}\n")

                except UnicodeDecodeError as e:
                    print(f"Error decoding serial data: {e}")
    
    def show_output(self, text):
        self.textview.config(state=tk.NORMAL)
        if text == "\b":
            # 백스페이스가 입력되면 마지막 글자를 지움
            current_text = self.textview.get("1.0", tk.END)
            if current_text.strip():  # 텍스트가 비어있지 않은 경우에만
                self.textview.delete("end-2c", tk.END)
        else:
            self.textview.insert(tk.END, text)
            self.textview.yview(tk.END)
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
# container2 = space(window)
container3 = Cont2(window)
container3.update_progress(80)
container6 = Checklist(window)
container7 = Textview(window)

# container5 = Cont4(window)


# 윈도우 실행
window.mainloop()

