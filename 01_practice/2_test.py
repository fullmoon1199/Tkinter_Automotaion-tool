# import re

# def get_color_from_escape_sequence(text):
#     # ANSI 이스케이프 시퀀스에서 색상 코드를 추출합니다.
#     color_codes = re.findall(r'\x1b\[0;(\d+)m', text)
#     print(color_codes)
#     for code in color_codes:
#         # 색상 코드에 따라 색상을 반환합니다.
#         if code == '30':
#             return 'black'
#         elif code == '31':
#             return 'red'
#         elif code == '32':
#             return 'green'
#         elif code == '33':
#             return 'yellow'
#         elif code == '34':
#             return 'blue'
#         elif code == '39':
#             return 'default'
#     # 색상 코드가 없으면 기본값을 반환합니다.
#     return 'default'

# # 테스트용 바이트 문자열 
# test_string = "adasd asd asd asd asdsadb'[\x1b[0;34m  OK  \x1b[0m] Reached target \x1b[0;39mSwap\x1b[0m.'"

# # 함수를 호출하여 색상을 얻습니다.
# color = get_color_from_escape_sequence(test_string)
# print("Color:", color)  # 색상을 출력합니다.
import ttkwidgets as tw

import tkinter as tk

from tkinter import *

from ttkwidgets import CheckboxTreeview

 

def one_fuction():

    tree.tag_add("LA-0008", "fail")

    tree.tag_add("LA-0009", "pass")

 

def changebutton():

    tree.tag_add("LA-0001", "pass")

    tree.tag_add("LA-0002", "pass")

class CheckboxTreeview(tw.CheckboxTreeview):

   

    def __init__(self, master=None, **kw):

        tw.CheckboxTreeview.__init__(self, master, **kw)

        # disabled tag to mar disabled items

        self.label=tk.Label(root, text=len(self.get_checked()), width=5, height=2)

        self.label.pack()

       

root = tk.Tk()

tree = CheckboxTreeview(root)

tree.pack()

 

button_one = Button(root, text="one", command = one_fuction)

button_one.pack()

 

change_tag = Button(root, text="change", command = changebutton)

change_tag.pack()

 

tree.insert("", "end", "LinyxAndroid", text="LinyxAndroid")

tree.insert("LinyxAndroid", "end", "Internal System", text="Internal System", )

tree.insert("LinyxAndroid", "end", "Externel Interface",  text="Externel Interface")

tree.insert("Internal System", "end", "LA-0001", text="LA-0001")

tree.insert("Internal System", "end", "LA-0002", text="LA-0002")

tree.insert("Internal System", "end", "LA-0003", text="LA-0003")

tree.insert("Internal System", "end", "LA-0004", text="LA-0004")

tree.insert("Internal System", "end", "LA-0005", text="LA-0005")

tree.insert("Externel Interface", "end", "LA-0006", text="LA-0006")

tree.insert("Externel Interface", "end", "LA-0007", text="LA-0007")

tree.insert("Externel Interface", "end", "LA-0008", text="LA-0008")

tree.insert("Externel Interface", "end", "LA-0009", text="LA-0009")

tree.tag_configure("pass", background="light green")

tree.tag_configure("fail", background="pink")

 

root.geometry("280x330")

root.resizable(True, True)

root.mainloop()
