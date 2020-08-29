a= 1000
b =78.95
#서식문자가 없는 경우
print(a, "   ", b)

#서식문자가 있는 경우 
print("%d" % a)
print("%5d" % a)
print("%05d" % a)

print("%f" % b)
print("%7.1f" % b)
print("%7.3f" % b)

print("%s" % "동아대학교")
print("%10s" % "경영정보학과")

#format() 함수 사용

print("{1}, {0}" .format(a, b))
print("{1:5.1f} {0:5d}" .format(a, b))
