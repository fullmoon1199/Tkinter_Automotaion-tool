import tkinter as tk

def update_labels(*args):
    i_label.config(text=f"pass : {pass_value.get()} fail : {fail_value.get()} remain : {remain_value.get()}")

root = tk.Tk()

pass_value = tk.StringVar(value= 0)
fail_value = tk.StringVar(value= 0)
remain_value = tk.StringVar(value= 0)

i_label = tk.Label(root, text=f"pass : {pass_value.get()} fail : {fail_value.get()} remain : {remain_value.get()}")
i_label.pack()

i_entry = tk.Entry(root, textvariable=pass_value)
i_entry.pack()

j_entry = tk.Entry(root, textvariable=fail_value)
j_entry.pack()

k_entry = tk.Entry(root, textvariable=remain_value)
k_entry.pack()

pass_value.trace("w", update_labels)
fail_value.trace("w", update_labels)
remain_value.trace("w", update_labels)

root.mainloop()