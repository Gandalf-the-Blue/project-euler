def zeller_congruence(day, month, year):
    
    if month == 1:
        month = 13
        year -= 1
    if month == 2:
        month = 14
        year -=1
    q = day
    m = month
    k = year % 100
    j = year // 100
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7
    return h


answer_list=[]

for year in range(1901,2001):
    for month in range(1,13):
        is_sunday = zeller_congruence(1,month,year)
        if is_sunday==1:
            answer_list.append([1,month,year])

answer = len(answer_list)
print(answer)

#171