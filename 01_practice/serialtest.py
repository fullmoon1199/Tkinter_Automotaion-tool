import serial
import threading
import asyncio

async def read_serial(serial):
    while True:
        data = serial.readline().decode('utf-8').strip()
        if data:
            print(f"수신된 데이터: {data}")

async def user_input(serial):
    while True:
        user_input = await asyncio.to_thread(input, "송신할 데이터 입력 (종료하려면 'exit' 입력): ")
        if user_input.lower() == 'exit':
            break
        serial.write(user_input.encode('utf-8'))

async def main(serial_port, baud_rate):
    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=0.5)
        print(f"시리얼 포트 {serial_port} 열림")

        # asyncio 코루틴들을 실행
        await asyncio.gather(
            read_serial(ser),
            user_input(ser),
        )

    except serial.SerialException as e:
        print(f"시리얼 포트 오류: {e}")

    finally:
        ser.close()
        print(f"시리얼 포트 {serial_port} 닫힘")

if __name__ == "__main__":
    serial_port = "COM22"
    baud_rate = 115200

    asyncio.run(main(serial_port, baud_rate))
