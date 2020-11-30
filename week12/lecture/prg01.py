def hap(a ):
    h = 0
    for val in a:
        h += val

    return h

data1 = (70, 30,20, 50, 60, 100)
data2 = ( 5, 30, 20, 12, 20, 40, 50, 70)
print(hap(data1) )
print(hap(data2))
