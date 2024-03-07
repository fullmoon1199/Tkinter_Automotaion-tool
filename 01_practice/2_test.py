import re

def get_color_from_escape_sequence(text):
    # ANSI 이스케이프 시퀀스에서 색상 코드를 추출합니다.
    color_codes = re.findall(r'\x1b\[0;(\d+)m', text)
    print(color_codes)
    for code in color_codes:
        # 색상 코드에 따라 색상을 반환합니다.
        if code == '30':
            return 'black'
        elif code == '31':
            return 'red'
        elif code == '32':
            return 'green'
        elif code == '33':
            return 'yellow'
        elif code == '34':
            return 'blue'
        elif code == '39':
            return 'default'
    # 색상 코드가 없으면 기본값을 반환합니다.
    return 'default'

# 테스트용 바이트 문자열 
test_string = "adasd asd asd asd asdsadb'[\x1b[0;34m  OK  \x1b[0m] Reached target \x1b[0;39mSwap\x1b[0m.'"

# 함수를 호출하여 색상을 얻습니다.
color = get_color_from_escape_sequence(test_string)
print("Color:", color)  # 색상을 출력합니다.

