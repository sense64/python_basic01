count = 0

for a in range(2,101) :
    for b in range(2, a+1):
        if a%b==0:
         break

    if a==b:
        print("%5d" %a, end='')
        count+=1

        if count%10==0:
            print('')

print("\n\n소수의 개수 :", count)
