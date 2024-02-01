import serial

def send_shift_f2():
    # Open the serial port
    ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with the appropriate port name

    # Send the Shift+F2 input
    ser.write(b'\x1b[OQ')

    # Close the serial port
    ser.close()

# Call the function to send the Shift+F2 input
send_shift_f2()
