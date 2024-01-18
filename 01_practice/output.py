import tkinter as tk

# Create the main window
window = tk.Tk()

# Create the Text widget
output_widget = tk.Text(window)

# Create a Scrollbar widget
scrollbar = tk.Scrollbar(window)

# Configure the Text widget to use the Scrollbar
output_widget.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_widget.yview)

# Add the Text widget and Scrollbar to the window
output_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Run the main loop
window.mainloop()
