import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")

root.geometry("640x1000")
# root.geometry("640x480+300+100") # 가로 x 세로 + x좌표 + y좌표

root.resizable(False, True) # x너비, y높이 값 변경 불가 (창 크기 변경 불가)

btn1 = Button(root, text='버튼1')
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text='버튼2') # pad는 버튼의 여백를 조정할 수 있음
btn2.pack() # pack을 해야 mainloop에 포함을 할 수 있음

btn3 = Button(root, padx=10, pady=5, text='버튼3')
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") #width랑 height는 버튼의 크기를 고정함
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

buttonimage = PhotoImage(file="buttonImage.png")
btn6 = Button(root, image=buttonimage)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="buttonImage.png")

label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요") #config는 바꾸는 것

    global photo2
    photo2 = PhotoImage(file="buttonImage2.png")
    label2.config(image=photo2)

btn8 = Button(root, text="클릭", command=change)
btn8.pack()

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력하세요")

def btncmd2():
    #내용 출력
    print(txt.get("1.0", END)) #1 : 첫 번째 라인, 0 : 0 번째 column 위치
    print(e.get())

    #내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd2)
btn.pack()

def btncmd3():
    #맨 뒤 항목 삭제
    # listbox.delete(END)

    #갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    #항목 확인(시작 indx, 끝 indx)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0.2))

    #선택된 항목 확인 (위치로 반환)
    print("선택된 항목 : ", listbox.curselection())
    
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

btn9 = Button(root, text="클릭", command=btncmd3)
btn9.pack()

def btncmd4():
    print(chkvar.get()) # 0 : 체크 해체, 1 : 체크
    print(chkvar2.get())

chkvar = IntVar()
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar,command=btncmd4)
chkbox.pack()
chkbox.select()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 보지 않기", variable=chkvar2, command=btncmd4)
chkbox2.pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value = 1, variable=burger_var)
btn_burger2 = Radiobutton(root, text="치즈버거", value = 2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="불고기버거", value = 3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라",  variable=drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value="사이다",  variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd5():
    print(burger_var.get())
    print(drink_var.get())

btn10 = Button(root, text="주문", command=btncmd5)
btn10.pack()

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.pack()
readonly_combobox.set("카드 결제일")

def btncmd6():
    print(combobox.get())
    print(readonly_combobox.get())

btn11 = Button(root, text="선택", command=btncmd6)
btn11.pack()

root.mainloop()
