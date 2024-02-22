import re

def process_escape_sequences(text):
    # ANSI 이스케이프 시퀀스를 정규표현식으로 찾습니다.
    escape_sequence = re.compile(r'\x1b\[[0-9;]*m')

    # 이스케이프 시퀀스를 빈 문자열로 대체하여 제거합니다.
    processed_text = escape_sequence.sub('', text)
    
    return processed_text

# 테스트를 위한 예시 텍스트
example_text = "b'[\x1b[0;32m  OK  \x1b[0m] Started \x1b[0;1;39mKernel Logging Service\x1b[0m.'"

# 이스케이프 시퀀스를 제거한 텍스트 출력
print(process_escape_sequences(example_text))
