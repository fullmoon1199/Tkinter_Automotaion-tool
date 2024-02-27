import serial
import threading

def read_serial(ser):
    while True:
        try:
            data = ser.readline().decode('utf-8').strip()  # Decode the received data as UTF-8
            if data:
                print('\n')
                print(f'{data}')
        except Exception as e:
            print(f"Error reading serial data: {e}")
            break

def main():
    # serial_port = input("Enter serial port (e.g. COM1, /dev/ttyUSB0): ")
    # baud_rate = int(input("Enter baud rate (e.g. 9600): "))

    ser = serial.Serial('COM22', '115200')

    # Start a separate thread for reading serial data
    serial_thread = threading.Thread(target=read_serial, args=(ser,), daemon=True)
    serial_thread.start()

    try:
        while True:
            user_input = input("Enter text to send over serial (press Enter to quit): ")
            ser.write(user_input.encode())  # UTF-8로 인코딩하지 않음
            ser.write(b'\n')
    except KeyboardInterrupt:
        pass
    finally:
        ser.close()

if __name__ == "__main__":
    main()
