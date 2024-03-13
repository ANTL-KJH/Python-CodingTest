def solution(my_string):
    lowerS = my_string.lower()
    lowerL = list(lowerS)
    lowerL.sort()
    answer = "".join(lowerL)
    return answer