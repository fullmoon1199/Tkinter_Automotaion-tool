import chardet

# 파일 경로 설정
file_path = 'F:\\tkinter\\test.json'

# 파일 인코딩 확인
with open(file_path, 'rb') as file:
    result = chardet.detect(file.read())

# 결과 출력
print(f"The detected encoding is: {result['encoding']}")