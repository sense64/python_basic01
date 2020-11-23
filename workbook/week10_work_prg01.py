### 변수선언
score = [70, 56, 89, 100, 60, 80, 65, 88]
hap, hap2 = 0, 0
iMax, iMin = score[0], score[0]

for i in range(len(score)) :
    hap += score[i]
    if iMax < score[i] :
        iMax = score[i]
    if iMin > score[i] :
        iMin = score[i]
avg = hap/len(score)
for i in range(len(score)) :
    hap2 += (score[i]-avg)**2
variance = hap2 / len(score)

print("합 = %d, 평균 = %5.2f, 분산 = %5.2f, 최대값 = %d, 최소값 = %d, 범위 = %d" % (hap, avg, variance, iMax, iMin, (iMax-iMin)))