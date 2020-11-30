n = 6
for i in range(n) :
    for j in range(i+1) :
        print(' ', end='')
    for j in range(n-i) :
        print('@', end='')
    print()


