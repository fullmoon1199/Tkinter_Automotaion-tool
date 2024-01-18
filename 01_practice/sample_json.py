import json

try:
    with open('F:\\tkinter\\01_practice\\sample.json') as file:
        datas = json.load(file)
        json_test = datas['Linux']
        print(json_test)
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
except FileNotFoundError:
    print("File not found.")
