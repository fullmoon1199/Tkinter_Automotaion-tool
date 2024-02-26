import tkinter as tk
from tkinter import ttk
import serial
import threading

class SerialApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Serial Communication")

        self.create_widgets()
        self.init_serial()

    def create_widgets(self):
        self.output_text = tk.Text(self.master, wrap=tk.WORD, state=tk.DISABLED)
        self.output_text.pack(padx=10, pady=10)

        self.input_entry = ttk.Entry(self.master, font=('Courier', 12))
        self.input_entry.pack(pady=10)

        send_button = ttk.Button(self.master, text="Send", command=self.send_command)
        send_button.pack()

    def init_serial(self):
        try:
            self.serial_port = serial.Serial('COM22', baudrate=115200, timeout=1)  # 5초 timeout으로 변경

        except serial.SerialException as e:
            print(f"Error initializing serial port: {e}")
            self.serial_port = None

    def send_command(self):
        if self.serial_port:
            command = self.input_entry.get() + '\n'
            self.input_entry.delete(0, tk.END)
            self.serial_port.write(command.encode())
            print(f"Sent: {command}")

    def read_serial(self):
        while True:
            if self.serial_port:
                try:
                    serial_output = self.serial_port.readline().decode('utf-8', errors='replace').strip()
                    if serial_output:
                        self.show_output(f"{serial_output}\n")
                except UnicodeDecodeError as e:
                    print(f"Error decoding serial data: {e}")

    def show_output(self, text):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.insert(tk.END, text)
        self.output_text.yview(tk.END)
        self.output_text.config(state=tk.DISABLED)

def run_serial_app():
    window = tk.Tk()
    app = SerialApp(window)
    # Start a separate thread for reading serial data
    read_thread = threading.Thread(target=app.read_serial, daemon=True)
    read_thread.start()
    
    window.mainloop()

if __name__ == "__main__":
    run_serial_app()

