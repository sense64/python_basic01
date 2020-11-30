dic={} # 딕셔너리 변수로 선언
dic['경영'] = 'management'
dic['정보'] = 'information'
dic['자료'] = 'data'
dic['틀'] = 'frame'
dic['초점'] = 'focus'
while(True) :
    myDic = input(str(list(dic.keys()))+ "중 찾고 싶은 단어는?")
    if myDic in dic :
        print("<%s>의 영어단어는 <%s>입니다 "%(myDic,dic.get(myDic)))
    elif myDic.upper() =='END' :  #upper()함수는 대문자로 변환하는 함수
        break
    else :
        print("해당하는 단어를 찾을 수 없습니다.")