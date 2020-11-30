list1 = ["짜장면", "라면", "탕수육", "라조육"]
list2 = [7000, 5000, 15000]
list3 = ['A', 'A', 'C']
for val in zip(list1, list2, list3) :
    print(val)

data = dict(zip(list1, list2))
listData = list(zip(list1, list2, list3))
print(data)
print(data["라면"])
listA, listB, listC = zip(*listData)
print(listA)
print(listB)
print(listC)

