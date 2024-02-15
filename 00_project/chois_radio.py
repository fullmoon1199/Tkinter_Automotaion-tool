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
import serial
import threading

def choised_radiobutton(con):
    selected_value = con.radio_var.get()  # 현재 선택된 버튼의 value 값을 가져옴

    if selected_value == 1:
        selected_button = "BL"
    elif selected_value == 2:
        selected_button = "BA"
    elif selected_value == 3:
        selected_button = "LA"
    else:
        selected_button = "No selection"
    print(selected_button)