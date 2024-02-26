import serial

def serial_open(con):
    selected_port_name = con.combo.get()  # 선택된 포트 이름 가져오기
    ports = serial.tools.list_ports.comports()
    port_device_mapping = {p.device: p.description for p in ports}  # 포트 번호와 디바이스 이름 매핑
    print(type(port_device_mapping))
    print("\nPort-Device mapping:", port_device_mapping)  # 포트-디바이스 매핑 출력

    # 선택된 포트 이름과 매핑된 포트 번호 찾기
    for port, device_name in port_device_mapping.items():
        if device_name == selected_port_name:
            serial_port = port
            break

    if serial_port is not None:
        print("Selected port:", serial_port)
    else:
        print("Selected port not found.")
    if serial_port:  # 선택된 포트가 있는지 확인
        try:
            serial_port = serial.Serial(serial_port, baudrate=115200, timeout=1)  # 선택된 포트 열기
            print(f"Serial port {serial_port} opened successfully.")
            # 시리얼 통신 작업 수행
        except serial.SerialException as e:
            print(f"Error initializing serial port: {e}")
            serial_port = None

    return serial_port
    
