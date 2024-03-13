def solution(n):
    factorial = 1
    cnt = 1
    while factorial * cnt <= n:
        factorial *= cnt
        cnt += 1
    cnt -= 1
    return cnt