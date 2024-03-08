import tkinter as tk
import Window_Title_function as wtf
from tkinter import *

class Window_Title:
    def __init__(self, window):
        self.buttonframe = Frame(window, bg='red')
        self.buttonframe.pack(fill=X, anchor=N)

        self.combo = tk.Combobox(self.buttonframe, width=60, state="readonly", style="TCombobox")
        self.combo.pack(padx=10, pady=18, anchor=tk.NW, side=tk.LEFT)

        self.search_port_button = tk.Button(self.buttonframe, text="Search Port", command=wtf.update_combobox, width=15, height=4)
        self.search_port_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)
        # hover color
        self.search_port_button.bind("<Enter>", lambda event, widget=self.search_port_button: wtf.on_enter(widget))
        self.search_port_button.bind("<Leave>", lambda event, widget=self.search_port_button: wtf.on_leave(widget))

        self.open_button = tk.Button(self.buttonframe, text="Open", command=wtf.on_open, width=15, height=4)
        self.open_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.close_button = tk.Button(self.buttonframe, text="Close", command=wtf.on_close, width=15, height=4)
        self.close_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.start_tc_button = tk.Button(self.buttonframe, text="Start TC", command=wtf.on_start_tc, width=15, height=4)
        self.start_tc_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.stop_tc_button = tk.Button(self.buttonframe, text="Stop TC", command=wtf.on_stop_tc, width=15, height=4)
        self.stop_tc_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.su_button = tk.Button(self.buttonframe, text="SU", command=lambda: wtf.on_su(container7), width=8, height=4)
        self.su_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.root_button = tk.Button(self.buttonframe, text="Root", command=lambda: wtf.on_root(container7), width=8, height=4)
        self.root_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.shift_f2_button = tk.Button(self.buttonframe, text="Shift+F2", command=wtf.on_shift_f2, width=15, height=4)
        self.shift_f2_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.shift_f3_button = tk.Button(self.buttonframe, text="Shift+F3", command=wtf.on_shift_f3, width=15, height=4)
        self.shift_f3_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

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

        

        self.open_excel_button = tk.Button(self.buttonframe, text="Open Excel", command=wtf.n_open_excel, width=15, height=4)
        self.open_excel_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)

        self.exit_button = tk.Button(self.buttonframe, text="Exit", command=window.quit, width=5, height=3, bg='red', fg='white',font=("Helvetica", 8, "bold"))
        self.exit_button.pack(padx=5, pady=0, anchor=tk.NW, side=tk.LEFT)





