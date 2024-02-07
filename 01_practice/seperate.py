

# 주어진 JSON 데이터
data = {
    "Number": 5,
    "TC Number": "BL-INSYS-LIN-0003",
    "Category": "Internal System",
    "BL": "O",
    "BA": "X",
    "LA": "X",
    "Automatic": "O",
    "ToolSequence": [
        "# nproc",
        "^ 10",
        "# echo 0 > /sys/devices/system/cpu/cpu2/online",
        "# echo 0 > /sys/devices/system/cpu/cpu1/online",
        "# nproc",
        "^ 8",
        "# cat /sys/devices/system/cpu/offline",
        "^ 1-2",
        "# echo 1 > /sys/devices/system/cpu/cpu1/online",
        "# echo 1 > /sys/devices/system/cpu/cpu2/online",
        "# nproc",
        "^ 10"
    ]
}

# '#'로 시작하는 명령어들과 '^'로 시작하는 명령어들을 분리하여 저장할 리스트 초기화
hash_commands = []
caret_commands = []

# ToolSequence에서 명령어들을 읽어와서 '#' 또는 '^'로 시작하는 경우에 따라 리스트에 추가
for command in data["ToolSequence"]:
    if command.startswith("#"):
        hash_commands.append(command)
    elif command.startswith("^"):
        caret_commands.append(command)

# 결과 출력
print("Commands starting with '#' :", hash_commands)
print("Commands starting with '^' :", caret_commands)
