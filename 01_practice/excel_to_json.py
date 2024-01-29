import openpyxl
from collections import OrderedDict
import json

excel_file_path = 'D:\\03.Test\\v620\\9R_231207\\ori_ExynosAutoV620_Validation_IR231207_070011.xlsx'

wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

data_list = []

for rownum in range(1, 223):
    data = OrderedDict()
    column_value = [cell.value for cell in sheet[rownum]]
    data['Number'] = column_value[0]
    data['TC Number'] = column_value[1]
    data['Category'] = column_value[2]
    data['BL'] = column_value[3]
    data['BA'] = column_value[4]
    data['LA'] = column_value[5]
    data_list.append(data)

for i in range(0, len(data_list)):
    print(data_list[i])

json_file_path = 'D:\\03.Test\\v620\\9R_231207\\test.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

# 저장한 JSON 파일 경로 출력
print(f"JSON 파일이 성공적으로 저장되었습니다: {json_file_path}")
