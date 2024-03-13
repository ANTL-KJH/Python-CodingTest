def solution(i, j, k):
    answer = 0
    for num in range(i,j+1):
        strNum = str(num)
        answer += strNum.count(str(k))
    
    return answer