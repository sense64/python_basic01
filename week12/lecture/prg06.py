def sum_avg(list1) :
    hap=0
    for i in range(0, len(list1)) :
        hap += list1[i]
    avg = hap.len(list1)
    return hap, avg

n_list=(50, 20, 50, 10, 100, 20)
result1, result2 = sum_avg(n_list)
## 에러난다
print("합=%d, 평균 = %f" %(result1,result2))

