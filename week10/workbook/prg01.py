list1 = list()
for num in range(2, 10) :
    is_Prime = True
    for i in range(2, num) :
        if num % i == 0:
            is_Prime = False
            break
    if is_Prime :
        list1.append(num)
print(list1)
