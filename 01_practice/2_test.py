import re

def extract_color_tags(text):
    # 정규 표현식을 사용하여 이스케이프 시퀀스를 찾음
    escape_sequences = re.findall(r'\x1b\[[0-9;]+m', text)
    
    color_tags = []
    for seq in escape_sequences:
        # 색상 태그인 경우에만 추출
        if '\x1b[38;5;' in seq or '\x1b[48;5;' in seq:
            color_tags.append(seq)
    
    return color_tags

def apply_color_tags(text):
    # 색상 태그 추출
    color_tags = extract_color_tags(text)
    
    # 색상 태그를 제거한 텍스트 생성
    clean_text = re.sub(r'\x1b\[[0-9;]+m', '', text)
    
    colored_text = clean_text
    for tag in color_tags:
        # 색상 태그에서 색상 코드 추출
        color_code = re.findall(r'\d+', tag)[0]
        # 텍스트에 해당 색상 적용
        colored_text = f"\033[{color_code}m{colored_text}"
    
    # 모든 색상을 리셋하여 기본으로 변경
    colored_text += '\033[0m'
    
    return colored_text

# 테스트를 위한 문자열
test_string = "\x1b[38;5;196mRed text\x1b[0m and \x1b[48;5;12mBlue background\x1b[0m"

# 색상 태그 적용
colored_text = apply_color_tags(test_string)
print(colored_text)
