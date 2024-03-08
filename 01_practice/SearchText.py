import tkinter as tk

from tkinter import Text, Scrollbar, END

 

search_list = []

 

def get_text(var, indx, mode):

    word = my_var.get()

    search_list.clear()

    start = '1.0'

    results_text.tag_remove('next', '1.0', END)

    results_text.tag_remove('found', start, END)

    global matches_found

    matches_found = 0

    if word:

        while 1:

            start = results_text.search(word, start, regexp=True, nocase=1, stopindex=END)

            if not start:

                break

            last = '%s+%dc' % (start, len(word))

            results_text.tag_add('found', start, last)

            matches_found += 1

            start = last

            results_text.tag_config('found', background='yellow')

    total_label.config(text=f"0:{str(matches_found)}")

 

def next_match():

    results_text.tag_remove('next', '1.0', END)

    end_search_label.config(text="")

    word = find_entry.get()

    count_pos = 0

    if word:

        start = "1.0" if search_list == [] else search_list[-1]

        start = results_text.search(word, start, nocase=1, stopindex=END)

        last = '%s+%dc' % (start, len(word))

        try:

            results_text.tag_add('next', start, last)

            results_text.tag_config('next', background='cyan', foreground='black', underline=1)

            counter_list = start.split('.')

            results_text.mark_set("insert", "%d.%d" % (int(counter_list[0]), int(counter_list[1])))

            results_text.see(float(int(counter_list[0])))

            search_list.append(last)

            for i in search_list:

                count_pos += 1

            total_label.config(text=f"{str(count_pos)}:{str(matches_found)}")

        except:

            end_search_label.config(text="Search complete. No further matches", anchor='w')

            search_list.clear()

 

# The rest of your code remains unchanged


 

# Create a simple Tkinter window

root = tk.Tk()

root.title("Text Search Example")

 

# Create widgets

my_var = tk.StringVar()

find_entry = tk.Entry(root, textvariable=my_var, width=30)

search_button = tk.Button(root, text="Search", command=lambda: get_text(my_var, 0, 0))

next_button = tk.Button(root, text="Next", command=next_match)

results_text = Text(root, wrap="word", height=10, width=40)

scrollbar = Scrollbar(root, command=results_text.yview)

results_text.config(yscrollcommand=scrollbar.set)

total_label = tk.Label(root, text="0:0")

end_search_label = tk.Label(root, text="", anchor='w')

 

# Grid layout

find_entry.pack(padx=10, pady=5)

search_button.pack(padx=5, pady=5)

next_button.pack(padx=5, pady=5)

results_text.pack(padx=10, pady=5, fill = "both", expand = True)

scrollbar.pack(pady=5, fill="y", side="right")

total_label.pack(padx=10, pady=5)

end_search_label.pack(padx=10, pady=5)

 

# Start the Tkinter event loop

root.mainloop()