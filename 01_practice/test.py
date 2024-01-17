import socket

def find_available_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        if result != 0:
            return port
    return None

# 사용 예시
start_port = 8000
end_port = 8100
available_port = find_available_port(start_port, end_port)

if available_port:
    print(f"사용 가능한 포트: {available_port}")
else:
    print("사용 가능한 포트를 찾을 수 없습니다.")
