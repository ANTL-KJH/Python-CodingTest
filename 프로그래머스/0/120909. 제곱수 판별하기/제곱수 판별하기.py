import math
def solution(n):
    sqrtn =int(math.sqrt(n))
    answer = 1 if sqrtn*sqrtn == n else 2
    return answer