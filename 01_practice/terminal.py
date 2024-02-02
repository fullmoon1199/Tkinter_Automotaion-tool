import tkinter as tk
from tkinter import scrolledtext
import serial
import threading
import chardet

class SerialCommunicationApp:
    def __init__(self, master):
        self.master = master
        master.title("Serial Communication App")

        # 텍스트 입력 상자
        self.input_entry = tk.Entry(master)
        self.input_entry.pack(pady=10)

        # 전송 버튼
        self.send_button = tk.Button(master, text="전송", command=self.send_command)
        self.send_button.pack()

        # 스크롤 텍스트 상자 (로그 표시)
        self.log_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.log_text.pack(pady=10)

        # 시리얼 통신 설정
        self.ser = serial.Serial('COM19', 115200)  # 포트와 전송 속도 설정
        self.receive_thread = threading.Thread(target=self.receive_data)
        self.receive_thread.start()

    def send_command(self):
        command = self.input_entry.get()
        self.ser.write(command.encode('utf-8'))
        self.input_entry.delete(0, tk.END)  # 입력 창 비우기

    def receive_data(self):
        while True:
            if self.ser.in_waiting > 0:
                received_data = self.ser.readline()
                detected_encoding = self.detect_encoding(received_data)
                data = received_data.decode(detected_encoding)
                self.log_text.insert(tk.END, data)
                self.log_text.yview(tk.END)  # 로그 표시 업데이트

    def detect_encoding(self, data):
        result = chardet.detect(data)
        return result['encoding']

    def on_close(self):
        self.ser.close()
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SerialCommunicationApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)  # 닫기 버튼 이벤트 처리
    root.mainloop()
