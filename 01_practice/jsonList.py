import json

try:
    with open('F:\\tkinter\\01_practice\\sample.json') as file:
        datas = json.load(file)
        boot_data = datas['Linux']['boot']
        for entry in boot_data:
                print(entry)
                # Access other properties as needed
                print(entry['id'])
                print(entry['name'])
                print(entry['tc'])
                # Access the 'list' and 'criterion' arrays if needed
                if 'list' in entry['tc']:
                    print(entry['tc']['list'])
                if 'criterion' in entry['tc']:
                    print(entry['tc']['criterion'])
        else:
            print("Invalid JSON structure. Missing 'Linux' or 'boot' key.")
except json.JSONDecodeError as e:
    print(f"JSON decoding error: {e}")
except FileNotFoundError:
    print("File not found.")

# import json

# # 주어진 JSON 데이터

# with open('F:\\tkinter\\01_practice\\sample.json') as file:
#         datas = json.load(file)

# # Linux의 모든 하위 항목의 이름 가져오기
# linux_subitems = datas.get("Linux", {})
# subitem_names = []

# # boot와 secure 아이템들을 가져와서 이름 추출
# for category, items in linux_subitems.items():
#     if isinstance(items, list):
#         for item in items:
#             subitem_names.append(item.get("name", ""))
            
# # 결과 출력
# print(subitem_names)