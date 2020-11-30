from tkinter import * #tkinter import함
from tkinter import messagebox #messagebox 모듈을 가져옴

def fun_ok() :
    lblInfo["text"] = "안녕하세요~~ Ok 버튼을 클릭했습니다."

def fun_cancel() :
    lblInfo["text"] = "Cancel버튼을 클릭했습니다."
def fun_mess():
    messagebox.showerror("정보확인", "안녕하세요 홍길동입니다")
def fun_question() :
    result = messagebox.askquestion("선호도", "파이썬을 좋아하나요")
    #print(result)
    if result=='yes' :
        lblInfo.configure(text="파이썬을 사랑합니다")
    else :
        lblInfo["text"]="ㅠㅠㅠ 슬퍼요"

window = Tk() #창을 생성
window.geometry("300x150")
lblInfo = Label(window, text="알림입니다")
btnOk = Button(window, text="Ok", fg="blue", command=fun_ok)  #Button 위젯(콤포넌트)를 생성
btnCancel = Button(window, text="Cancel", fg="#ff0000",command=fun_cancel)
btnMessage = Button(window, text="message", command= fun_mess)
btnAsk = Button(window, text="파이썬선호도", command=fun_question)
lblInfo.pack()
btnOk.place(x=100,y=0) #배치
btnCancel.pack(side=LEFT, ipadx=5, ipady=5)
btnMessage.pack(side=RIGHT,padx=5, pady=5)
btnAsk.pack(side=RIGHT,padx=5, pady=5)

window.mainloop() #이벤트 루프 생성하기(대기)


