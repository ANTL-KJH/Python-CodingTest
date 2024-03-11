import math
def solution(n):
    sqrtn = int(math.sqrt(n))
    answer = 0
    for i in range(1,sqrtn+1):
        if n % i ==0:
            answer +=1
    answer *=2
    if sqrtn*sqrtn == n:
        answer -=1
    return answer