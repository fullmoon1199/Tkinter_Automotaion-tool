import openpyxl
from collections import OrderedDict
import json

excel_file_path = 'D:\\03.Test\\v620\\9R_231207\\ori_ExynosAutoV620_Validation_IR231207_070011.xlsx'

wb = openpyxl.load_workbook(excel_file_path)
sheet = wb['Validation Result']

data_list = []

for rownum in range(6, 223):
    data = OrderedDict()
    column_value = [cell.value for cell in sheet[rownum]]
    data['Number'] = column_value[0]
    data['TC Number'] = column_value[1]
    data['Category'] = column_value[2]
    data['BL'] = column_value[9]
    data['BA'] = column_value[10]
    data['LA'] = column_value[11]
    Command = column_value[25]
    Criterion = column_value[26]

    if Command:
        Command = Command.split('\n')
    else:
        Command = []

    if Criterion:
        Criterion = Criterion.split('\n')
    else:
        Criterion = []
        
    data['Command'] = Command
    data['Criterion'] = Criterion

    data_list.append(data)

for i in range(len(data_list)):
    print(data_list[i])

json_file_path = 'F:\\tkinter\\test.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

print(f"JSON 파일이 성공적으로 저장되었습니다: {json_file_path}")