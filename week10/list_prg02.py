a= list()
aa = list()
value = 0
for r in range(3) :
    for c in range(3) :
        value += 1
        a.append(value)
    aa.append(a)
    a=[]

for r in range(3) :
    for c in range(3) :
        print(aa[r][c], end = "  ")
    print()
