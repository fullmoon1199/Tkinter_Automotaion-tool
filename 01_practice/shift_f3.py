import serial

def send_shift_f3():
    # Open the serial port
    ser = serial.Serial('COM1', 112500)  # Replace 'COM1' with the appropriate port name

    # Send the Shift+F3 input
    ser.write(b'\x1b[OR')

    # Close the serial port
    ser.close()

# Call the function to send the Shift+F3 input
send_shift_f3()
