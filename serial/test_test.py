import serial
import signal
import threading
import asyncio

line = []  # 라인 단위로 데이터 가져올 리스트 변수
port = 'COM22'  # 시리얼 포트
baud = 115200  # 시리얼 보드레이트(통신속도)
exitThread = False  # 쓰레드 종료용 변수

# 쓰레드 종료용 시그널 함수
def handler(signum, frame):
    global exitThread
    exitThread = True

# 데이터 처리할 함수
def parsing_data(data):
    # 리스트 구조로 들어 왔기 때문에
    # 작업하기 편하게 스트링으로 합침
    tmp = ''.join(data)

    # 출력!
    print(tmp)

# 사용자 입력을 받는 함수
async def user_input(serial):
    while True:
        user_input = await asyncio.to_thread(input, "송신할 데이터 입력 (종료하려면 'exit' 입력): ")
        # if user_input.lower() == 'next':
        serial.write(user_input.encode('utf-8'))
        # readThread(ser)

# 본 쓰레드
def readThread(ser):
    global line
    global exitThread

    # 쓰레드 종료될 때까지 계속 돌림
    while not exitThread:
        # 데이터가 있있다면
        for c in ser.read():
            # line 변수에 차곡차곡 추가하여 넣는다.
            line.append(chr(c))

            if c == 10:  # 라인의 끝을 만나면..
                # 데이터 처리 함수로 호출
                parsing_data(line)

                # line 변수 초기화
                del line[:]

if __name__ == "__main__":
    # 종료 시그널 등록
    signal.signal(signal.SIGINT, handler)

    # 시리얼 열기
    ser = serial.Serial(port, baud, timeout=0)

    # 시리얼 읽을 쓰레드 생성
    thread = threading.Thread(target=readThread, args=(ser,))

    # 시작!
    thread.start()

    # asyncio 이벤트 루프 실행
    asyncio.run(user_input(ser))
