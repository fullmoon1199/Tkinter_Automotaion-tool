import json

try:
    with open('F:\\tkinter\\01_practice\\sample.json') as file:
        datas = json.load(file)
        boot_list = datas['Linux']['boot']
        
        # 각 boot의 name 값을 가져와 리스트로 만듭니다.
        json_test = [boot['name'] for boot in boot_list]
        
        print(json_test)
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
except FileNotFoundError:
    print("File not found.")
