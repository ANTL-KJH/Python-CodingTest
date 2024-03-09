def dateCompare(d1,d2):
    if d1[0]<d2[0]:
        return 1
    if d1[0] == d2[0] and d1[1]<d2[1]:
        return 1
    if d1[0] == d2[0] and d1[1] == d2[1] and d1[2]<d2[2]:
        return 1
    return 0

def solution(date1, date2):
    answer = dateCompare(date1, date2)
    return answer