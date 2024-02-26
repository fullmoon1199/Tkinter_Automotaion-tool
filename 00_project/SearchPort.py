import serial.tools.list_ports

def on_search_port(combo):
    ports = serial.tools.list_ports.comports()
    port_device_mapping = {p.device: p.description for p in ports}  # Mapping port numbers to device names
    print("\nPort-Device mapping:", port_device_mapping)  # Print port-device mapping
    available_ports = [p.description for p in ports]
    combo['values'] = available_ports  # Set the combo box values to the available ports list

    if available_ports:  # Check if there are available ports
        combo.current(0)  # Automatically select the first element in the combo box
