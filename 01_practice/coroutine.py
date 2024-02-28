# import asyncio
# import time
# async def coroutine_func():
#     print("Coroutine is starting")
#     for i in range(3):
#         print(f"asyncio : {i}" )
#         await asyncio.sleep(1)
#     print("Coroutine is done")

# async def main():
#     print("Main function is starting")

    
    
#     for i in range(3):
#         time.sleep(1)
#         print(i)
#     await coroutine_func()  # 코루틴 호출
#     print("Main function is done")

# asyncio.run(main())  # Python 3.7부터 도입된 asyncio.run() 함수를 사용하여 이벤트 루프를 실행

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(4, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
