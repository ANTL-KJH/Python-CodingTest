def solution(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    answer = max(int(ab), int(ba))
    return answer