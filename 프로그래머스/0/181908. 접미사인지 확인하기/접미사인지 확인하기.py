def solution(my_string, is_suffix):
    answer = 1
    if len(my_string)>=len(is_suffix):
        for i in range(-1,-len(is_suffix)-1, -1):
            if my_string[i] != is_suffix[i]:
                answer = 0
                break
    else:
        answer = 0
    return answer