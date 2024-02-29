import tkinter as tk

 

window=tk.Tk()

window.title("test")

window.geometry("640x480+100+100")

window.resizable(False, False)

 

command_listbox = []

global count

count = len(command_listbox)

def command_list(self):

    command_listbox.append(entry.get())

    print(f'command list: {command_listbox}')

    entry.delete(0,'end')


 

def previous_command(event):

    global count

    if command_listbox:

            count +=1

            command_listbox[len(command_listbox)-count]

            entry.insert(tk.END, command_listbox[len(command_listbox)-count])

       

def next_command(event):

    global count

    if command_listbox:

            count -=1

            command_listbox[len(command_listbox)-count]

            entry.insert(tk.END, command_listbox[len(command_listbox)-count])

           

 

entry=tk.Entry(window)

entry.bind("<Return>", command_list)

entry.bind("<Up>", previous_command)

entry.bind("<Down>", next_command)

entry.pack()

 

window.mainloop()