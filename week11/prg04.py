oldList =['짜장면', '짬뽕', '탕수육']
newList=[5000, 8000, 15000]
data =list(zip(oldList, newList))
print(data)
a, b = zip(*data)
print(a)
print(b)
