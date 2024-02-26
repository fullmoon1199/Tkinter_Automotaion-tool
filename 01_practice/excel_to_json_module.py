import openpyxl
from collections import OrderedDict
import json
from tkinter import filedialog
def excel_to_json():

    file_path = filedialog.askopenfilename()
    excel_file_path = file_path

    wb = openpyxl.load_workbook(excel_file_path)
    sheet = wb['Bearmetal_Linux']

    data_list = []

    for rownum in range(6, 223):
        data = OrderedDict()
        column_value = [cell.value for cell in sheet[rownum]]
        data['Number'] = column_value[0]
        data['TC Number'] = column_value[1]
        data['Category'] = column_value[2]
        data['BL'] = column_value[10]
        data['BA'] = column_value[11]
        data['LA'] = column_value[12]
        data['Automatic'] = column_value[14]
        ToolSequence = column_value[15]

        if ToolSequence:
            ToolSequence = ToolSequence.split('\n')
        else:
            ToolSequence = []

        data['ToolSequence'] = ToolSequence

        data_list.append(data)

    for i in range(len(data_list)):
        print(data_list[i])

    json_file_path = 'F:\\tkinter\\00_project\\test.json'
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=4, ensure_ascii=False)

    print(f"JSON 파일이 성공적으로 저장되었습니다: {json_file_path}")

