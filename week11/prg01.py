#학번 이름
#dictionary
student1 = {'학번' : 1000, '이름' : '홍길동', '학과' : '경영정보학과'}
student2 = {'학번' : 2000, '이름' : '이순신', '학과' : '경영학과'}
print(student1)
print(student1['이름'])
print(student1.get('이름'))
student1['tel'] = '010-5550-1234' #추가
student1['이름'] = '성춘향' #수정
print(student1)
del(student1['tel'])
print(student1)
print(student2)
print(student1.keys())
print(student1.values())