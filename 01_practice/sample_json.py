# https://dibrary.tistory.com/137 c참고자료
# import json

# try:
#     with open('F:\\tkinter\\01_practice\\sample.json') as file:
#         datas = json.load(file)
#         json_test = datas['Linux']['boot']['name']
#         print(json_test)
# except json.JSONDecodeError as e:
#     print(f"JSON decoding error: {e}")
# except FileNotFoundError:
#     print("File not found.")
# except KeyError:
#     print("KeyError: 'boot' key not found in the specified path.")
import json

try:
    with open('F:\\tkinter\\01_practice\\sample.json') as file:
        data = json.load(file)
        boot_tests = data.get('Linux', {}).get('boot', [])

        for boot_test in boot_tests:
            name = boot_test.get('name', 'Name not found')
            print(name)

except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
except FileNotFoundError:
    print("File not found.")
