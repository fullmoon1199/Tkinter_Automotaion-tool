import serial
import serial.tools.list_ports as sp



list = sp.comports()

connected = []



for i in list:

    connected.append(i.device)

print("Connected COM ports: " + str(connected))

select_comport = input('select:')

ser = serial.Serial("COM22", 115200, timeout = 1)


while True:

    print("insert op :", end='')

    op = input()

    delimiter = '\r\n'

    op = op+delimiter

    print(op)

    ser.write(op.encode())

    res = ser.readline()
    if res:
        print("Response:", res.decode().strip())

    # res_packet = res.decode()[:len(res)-1]

    # print(res_packet)

    print('\n')

    if op is 'q':

        ser.close()