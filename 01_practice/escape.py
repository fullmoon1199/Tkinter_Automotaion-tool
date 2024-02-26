
import serial
import time
import signal
import threading
import keyboard as key

line = []  # 라인 단위로 데이터 가져올 리스트 변수

port = 'COM32'  # 시리얼 포트
baud = 115200  # 시리얼 보드레이트(통신속도)

exitThread = False   # 쓰레드 종료용 변수

cmdSendReayStatus = True


def gotoLKshell():
    global cmdSendReayStatus
    print(f"cmdSendReayStatus : {cmdSendReayStatus}")

    while cmdSendReayStatus:
        time.sleep(0.1)
        ser.write("s".encode("utf-8"))
        print("goto LK shell")

    ser.write("\r".encode("utf-8"))
    ser.write("\r".encode("utf-8"))


def switch_colsol():
    while True:
        print("1 step")
        # ser.write(15)  # shift in / out
        ser.write(b" [24~")
        # ser.write(14)  # shift in / out
        ser.write('\r'.encode("utf-8"))    
        time.sleep(2)
        print("1 step end")
        
        print("2 step")
        # ser.write(15)  # shift in / out
        ser.write(b" [25~")
        # ser.write(14)  # shift in / out
        ser.write('\r'.encode("utf-8"))    
        time.sleep(2)
        print("2 step end")
        
        # print("2 step")

        # ser.write(14)  # shift in / out
        # ser.write(b"[25~")
        # ser.write(15)  # shift in / out
        # ser.write('\r'.encode("utf-8"))
        # ser.write('\r'.encode("utf-8"))
        # time.sleep(2)
        # print("2 step end")


# 쓰레드 종료용 시그널 함수
def handler(signum, frame):
    exitThread = True


# 데이터 처리할 함수
def parsing_data(data):
    global cmdSendReayStatus
    # 리스트 구조로 들어 왔기 때문에
    # 작업하기 편하게 스트링으로 합침
    tmp = "".join(data)

    # 출력!
    print("rx_msg : ", tmp)

    if tmp.strip() == "EPBL: v2.6(3a52b8374):v920(evt21)":
        cmdSendReayStatus = True
        print("[consol] booting start")

    if tmp.strip() == "entering main console loop":
        cmdSendReayStatus = False

    del line[:]


# 본 쓰레드
def serial_communication(ser):
    global line
    global exitThread
    global cmdSendReayStatus

    # 쓰레드 종료될때까지 계속 돌림
    while not exitThread:

        # 데이터가 있있다면
        for c in ser.readline():

            # line 변수에 차곡차곡 추가하여 넣는다.
            line.append(chr(c))

            if c == 10:  # \r 라인의 끝을 만나면
                # 데이터 처리 함수로 호출
                parsing_data(line)


if __name__ == "__main__":
    # 종료 시그널 등록
    signal.signal(signal.SIGINT, handler)

    # 시리얼 열기
    ser = serial.Serial(port, baud, timeout=0)

    # 시리얼 읽을 쓰레드 생성
    thread = threading.Thread(target=serial_communication, args=(ser,))

    # 시작!
    thread.start()

    switch_colsol()
