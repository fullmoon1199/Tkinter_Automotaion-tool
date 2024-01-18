# https://dibrary.tistory.com/137 c참고자료
import json

try:
    with open('F:\\tkinter\\01_practice\\sample.json') as file:
        datas = json.load(file)
        json_test = datas['Linux']['boot']
        print(type(json_test))
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
except FileNotFoundError:
    print("File not found.")
except KeyError:
    print("KeyError: 'boot' key not found in the specified path.")

