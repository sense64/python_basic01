hap, a, b = 0,0,0

while True :
    a = int(input("첫번째 수 입력 =>"))
    b = int(input("두번째 수 입력 =>"))
    hap = a + b
    if hap%2 !=0 :
        continue
    print("%d + %d = %d" %(a,b, hap))