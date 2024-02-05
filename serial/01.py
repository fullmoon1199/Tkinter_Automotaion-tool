import serial
import time
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
    tmp = ''.join(data)
    print(tmp)

# 비동기적으로 사용자 입력을 받는 함수
async def async_input():
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, input)

# 본 쓰레드
def readThread(ser):
    global line
    global exitThread

    while not exitThread:
        for c in ser.read():
            # line 변수에 차곡차곡 추가하여 넣는다.
            line.append(chr(c))

            if c == 10:  # 라인의 끝을 만나면..
                # 데이터 처리 함수로 호출
                parsing_data(line)

                # line 변수 초기화
                del line[:]

        try:
            # 비동기적으로 사용자 입력을 받음
            user_input = asyncio.run(async_input())
            if user_input.lower() == 'q':
                print('Serial comm stop !!!')
                exitThread = True
        except asyncio.CancelledError:
            pass
        except KeyboardInterrupt:
            pass

if __name__ == "__main__":
    # 종료 시그널 등록
    signal.signal(signal.SIGINT, handler)

    # 시리얼 열기
    ser = serial.Serial(port, baud, timeout=0)

    # 시리얼 읽을 쓰레드 생성
    thread = threading.Thread(target=readThread, args=(ser,))

    # 시작!
    thread.start()
