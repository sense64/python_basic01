list1 = []
list2 = []
value = 0
for r in range(5) :
    for c in range(5) :
        list2.append(value)
        value += 3
    list1.append(list2)
    list2= []
print(list1[1][0])
for r in range(5) :
    for c in range(5) :
        print(list1[r][c], end=" ")
    print()