menu={'Americano':3000, 'Ice Americano':3500, 'Cappuccino':4000, 'Caffe Latte' : 4500, 'Espresso':3600} # 딕셔너리 변수로 선언
while(True) :
    for k in menu.keys() :
        print("%12s      : 가격 %5s 원" %(k, menu[k]))
    choice = input("위의 메뉴를 선택하시오")
    if choice in menu :
        print("<%s>는 <%s>입니다 결재부탁드립니다."%(choice,menu.get(choice)))
    elif choice.upper() =='END' :  #upper()함수는 대문자로 변환하는 함수
        break
    else :
        print("미안합니다.%s은 메뉴는 없습니다"%choice)