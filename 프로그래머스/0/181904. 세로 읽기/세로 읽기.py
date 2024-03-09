def solution(my_string, m, c):
    my_string = my_string[c-1::m]
    answer = ''.join(my_string)
    return answer