def solution(n):
    answer = []
    tmp = 2
    while n !=1:
        if n % tmp == 0:
            if tmp not in answer:
                answer.append(tmp)
            n //= tmp
        else:
            tmp+=1
            
    return answer