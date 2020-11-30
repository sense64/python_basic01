num = int(input("숫자를 입력=>"))
fact = 1
for i in range(1, num+1) :
    fact*=i
    print("%d!=%d"%(i, fact))