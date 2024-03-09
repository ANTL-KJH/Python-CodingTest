def solution(intStrs, k, s, l):
    answer = [int(st[s:s+l]) for st in intStrs if int(st[s:s+l]) > k]
    return answer