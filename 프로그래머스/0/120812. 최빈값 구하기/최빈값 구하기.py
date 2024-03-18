def solution(array):
    setArray = set(array)
    dictArray = {n:array.count(n) for n in setArray}
    maxCount = max(dictArray.values())
    cnt = 0
    answer = -1
    for n in setArray:
        if dictArray[n] == maxCount:
            cnt += 1
            answer = n
    if cnt != 1:
        answer = -1
    return answer