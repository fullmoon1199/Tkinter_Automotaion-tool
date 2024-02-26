# port close

def stop_serial_read_thread():
    global stop_thread
    stop_thread = True
   
def on_close():
    stop_serial_read_thread
    global serial_port
    if serial_port is not None:
        serial_port.close()  # Close the serial port if it is open
        print("Serial port closed.")
    else:
        print("No serial port open.")