aa = [70, 80, 100, 45, 70, 66, 80, 90, 75, 68, 99] #리스트에 값 선언
#print(aa[1]) #리스트 원소 출력
#hap = aa[0] + aa[1] + aa[2] + aa[3] + aa[4] + aa[5]
hap = 0
for i in range(len(aa)) :
    hap += aa[i]
print("합 = %d, 평균 = %f" %(hap, hap/len(aa)))



