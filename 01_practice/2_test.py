import re

def extract_color_codes(text):
    # 정규 표현식을 사용하여 ANSI 이스케이프 시퀀스에서 숫자 부분을 추출합니다.
    color_codes = re.findall(b'\x1b\[\d+;\d+m', text)
    extracted_numbers = []
    for code in color_codes:
        # 숫자 부분만 추출하여 리스트에 추가합니다.
        numbers = re.findall(b'\d+', code)
        extracted_numbers.extend(map(int, numbers))
    return extracted_numbers

def return_value_based_on_number(number):
    # 각 숫자에 따라 다른 값을 반환합니다.
    if number == 0:
        return "Reset"
    elif number >= 30 and number <= 39:
        return "Foreground Color"
    elif number >= 40 and number <= 49:
        return "Background Color"
    else:
        return "Unknown"

def analyze_color_codes(text):
    color_codes = extract_color_codes(text)
    analyzed_results = [return_value_based_on_number(num) for num in color_codes]
    return analyzed_results

# 테스트용 문자열
test_string = "b'[\x1b[0;32m  OK  \x1b[0m] Started \x1b[0;1;39mSystem Logging Service\x1b[0m.'"

# 이스케이프 시퀀스에서 추출한 숫자들과 해당하는 리턴값들을 출력합니다.
color_codes = analyze_color_codes(test_string)
for code, result in zip(extract_color_codes(test_string), color_codes):
    print(f"Code: {code}, Result: {result}")
