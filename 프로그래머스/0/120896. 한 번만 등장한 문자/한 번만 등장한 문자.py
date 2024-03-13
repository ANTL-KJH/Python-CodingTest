def solution(s):
    sL = [st for st in s if s.count(st)==1]
    sL.sort()
    answer ="".join(sL)
    return answer