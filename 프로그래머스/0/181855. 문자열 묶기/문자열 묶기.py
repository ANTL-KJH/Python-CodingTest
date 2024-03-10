def solution(strArr):
    lenL = [0 for _ in range(31)]
    for st in strArr:
        lenL[len(st)] += 1
    answer = max(lenL)
    return answer