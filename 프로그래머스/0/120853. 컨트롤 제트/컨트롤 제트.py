def solution(s):
    sL = list(s.split())
    answer = 0
    for i in range(len(sL)):
        answer += int(sL[i]) if sL[i] != "Z" else -int(sL[i-1])
    return answer