student_tuple=(('20101', '홍길동', '011-123-4567'), ('20102', '이순신', '010-234-4545'),
               ('20103', '성춘향', '010-345-0987'))
list1=[]
list2=[]
for i in range(3) :
    list1.append(student_tuple[i][0])
    list2.append(student_tuple[i][1])
student_dict = dict(zip(list1, list2))
print(student_dict)


