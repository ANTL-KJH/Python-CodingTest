def solution(arr):
    arrLen = len(arr)
    cnt = 0
    while arrLen>=2:
        arrLen/=2
        cnt+=1
    if arrLen != 1:
        cnt +=1
    for _ in range(pow(2,cnt)-len(arr)):
        arr.append(0)

    return arr