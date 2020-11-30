aa=[[3, 50, 20],
    [90, 30, 70, 90, 10],
    [60, 20, 40, 20]]

s= [0,0,0]

for r in range(len(aa)) :
    for c in range(len(aa[r])) :
        s[r] += aa[r][c]

## 결과 출력
for i in range(len(aa)) :
    print(" %d 행의 합= %d 평균= %5.2f"%(i+1, s[i],s[i]/len(aa[i])))

