def solution(my_string, num1, num2):
    sL = list(my_string)
    sL[num1], sL[num2] = sL[num2], sL[num1]
    answer = ''.join(sL)
    return answer