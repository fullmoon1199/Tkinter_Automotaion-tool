import tkinter as tk
from ttkwidgets import CheckboxTreeview

class Checklist:
    def __init__(self, window):
        self.auto = 0
        self.manual = 0

        self.Checklist_LargeFrame = tk.Frame(window, bg='white')
        self.Checklist_LargeFrame.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        # CheckboxTreeview와 스크롤바를 담을 프레임 생성
        self.frame = tk.Frame(self.Checklist_LargeFrame, bg='white')
        self.frame.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        self.frame2 = tk.Frame(self.Checklist_LargeFrame, bg='white')
        self.frame2.pack(padx=5, pady=5, fill='y', anchor=tk.NW, side=tk.LEFT)

        # CheckboxTreeview 생성
        self.title_label = tk.Label(self.frame, text=f"Auto TC : # 선택개수 / {self.auto}개",
                                    font=("Helvetica", 10, "bold"), bg='white')
        self.title_label.pack()
        self.tree = CheckboxTreeview(self.frame)
        self.tree.pack(side=tk.LEFT, fill='y')

        self.title_label2 = tk.Label(self.frame2, text=f"Manual TC : # 선택개수 / {self.manual}개",
                                     font=("Helvetica", 10, "bold"), bg='white')
        self.title_label2.pack()
        self.tree2 = CheckboxTreeview(self.frame2)
        self.tree2.pack(side=tk.LEFT, fill='y')

        # 스크롤바 설정
        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical', command=self.tree.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill='y')

        self.scrollbar2 = tk.Scrollbar(self.frame2, orient='vertical', command=self.tree2.yview)
        self.scrollbar2.pack(side=tk.RIGHT, fill='y')

        # CheckboxTreeview에 스크롤바 적용
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.tree2.configure(yscrollcommand=self.scrollbar2.set)

    def add_node(self):
        # 실제로 사용할 노드 추가 로직을 여기에 작성
        # 여기서는 간단한 노드를 추가하는 예제를 제공합니다.
        new_node_id = f"dynamic_node_{self.auto + self.manual}"
        self.tree.insert("", "end", new_node_id, text=f"Dynamic Node {new_node_id}")
        self.tree2.insert("", "end", new_node_id, text=f"Dynamic Node {new_node_id}")

        # 카운터 업데이트
        if self.auto % 2 == 0:
            self.auto += 1
        else:
            self.manual += 1

        # 레이블 업데이트
        self.title_label.config(text=f"Auto TC : # 선택개수 / {self.auto}개")
        self.title_label2.config(text=f"Manual TC : # 선택개수 / {self.manual}개")

def add_node_callback(checklist_instance):
    checklist_instance.add_node()

if __name__ == "__main__":
    root = tk.Tk()
    app = Checklist(root)

    # 클래스 외부에 버튼 추가
    button_add_node = tk.Button(root, text="노드 추가", command=lambda: add_node_callback(app))
    button_add_node.pack()

    root.mainloop()
