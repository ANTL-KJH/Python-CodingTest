def solution(before, after):
    beforeL, afterL = list(before), list(after)
    beforeL.sort()
    afterL.sort()
    answer = 1 if beforeL == afterL else 0
    return answer