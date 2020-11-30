n = int(input("숫자를 입력하라" ))

is_prime = True
for num in range(2, n) :
    if n % num ==0 :
        is_prime = False
if is_prime==True :
    print(n, "는 솟수입니다.")
else :
    print(n, "는 솟수가 아닙니다.")


