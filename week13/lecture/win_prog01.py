#학번 이름(윈도우 프로그래밍)
from tkinter import *
## 함수 선언
def fun_ok() :
    label2["text"]="안녕~~~ 홍길동"

w = Tk()
w.title('201020 홍길동')
photo = PhotoImage(file="cat.gif", width=200, height=100)
label1 = Label(w,text="경영정보학과 홍길동")
label2 = Label(w, text="재미있는 파이썬", font=("궁서체", 35), fg="red")
label3 = Label(w, image = photo)
button = Button(w, text="확인", command=fun_ok)
btnQuit = Button(w, text="종료", command=quit)
label1.pack()
label2.pack()
label3.pack()
button.pack()
btnQuit.pack()
w.geometry("500x250")
w.resizable(width=False, height=False)
w.mainloop()