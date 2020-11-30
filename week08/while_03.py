num1, num2, num3 = 1,1,0
print(num1, "  ", num2, end="  " )
for i in range(1, 51) :
    num3 = num1 + num2
    if num3 > 100 :
        break
    print(num3, end="  ")
    num1 = num2
    num2 = num3
