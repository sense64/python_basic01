### 전역변수와 지역변수 ####
def func1() :
    a = 10 #함수내에 변수를 선언하면 지역변수
    print("func1() a값", a, b)

def func2() :
    global b  #전역변수
    b = '동아대학교'
    print("func2() a값", a, b)
### 전역변수
a = 777
### 메인 코드

func2()
func1()